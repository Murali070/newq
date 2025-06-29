"""
Utility functions for JARVIS AI Assistant
"""
import json
import logging
import asyncio
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from .config import config

# Setup logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config.DATA_DIR / 'jarvis.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class FileManager:
    """Manages file operations for JARVIS"""
    
    @staticmethod
    def read_file(file_path: Union[str, Path], default: Any = None) -> Any:
        """Read file content with error handling"""
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return default
            
            if file_path.suffix == '.json':
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return default
    
    @staticmethod
    def write_file(file_path: Union[str, Path], content: Any) -> bool:
        """Write content to file with error handling"""
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            if isinstance(content, (dict, list)):
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(content, f, indent=2, ensure_ascii=False)
            else:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(str(content))
            return True
        except Exception as e:
            logger.error(f"Error writing file {file_path}: {e}")
            return False
    
    @staticmethod
    def append_file(file_path: Union[str, Path], content: str) -> bool:
        """Append content to file"""
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"Error appending to file {file_path}: {e}")
            return False

class StatusManager:
    """Manages application status"""
    
    @staticmethod
    def set_status(status: str) -> None:
        """Set application status"""
        FileManager.write_file(config.STATUS_FILE, status)
        logger.info(f"Status updated: {status}")
    
    @staticmethod
    def get_status() -> str:
        """Get current application status"""
        return FileManager.read_file(config.STATUS_FILE, "Ready")
    
    @staticmethod
    def set_mic_status(enabled: bool) -> None:
        """Set microphone status"""
        FileManager.write_file(config.MIC_FILE, str(enabled))
    
    @staticmethod
    def get_mic_status() -> bool:
        """Get microphone status"""
        status = FileManager.read_file(config.MIC_FILE, "False")
        return status.lower() == "true"

class MessageManager:
    """Manages chat messages and responses"""
    
    @staticmethod
    def load_chat_log() -> List[Dict[str, Any]]:
        """Load chat log from file"""
        return FileManager.read_file(config.CHAT_LOG_FILE, [])
    
    @staticmethod
    def save_chat_log(messages: List[Dict[str, Any]]) -> bool:
        """Save chat log to file"""
        return FileManager.write_file(config.CHAT_LOG_FILE, messages)
    
    @staticmethod
    def add_message(role: str, content: str) -> bool:
        """Add message to chat log"""
        messages = MessageManager.load_chat_log()
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        messages.append(message)
        return MessageManager.save_chat_log(messages)
    
    @staticmethod
    def show_response(text: str) -> None:
        """Display response in GUI"""
        FileManager.write_file(config.RESPONSES_FILE, text)
        logger.info(f"Response displayed: {text[:100]}...")

class ErrorHandler:
    """Centralized error handling"""
    
    @staticmethod
    def handle_api_error(provider: str, error: Exception) -> str:
        """Handle API errors gracefully"""
        error_msg = f"Error with {provider} API: {str(error)}"
        logger.error(error_msg)
        
        fallback_msg = f"I'm experiencing issues with {provider}. Please try again or check your API configuration."
        return fallback_msg
    
    @staticmethod
    def handle_file_error(operation: str, file_path: str, error: Exception) -> None:
        """Handle file operation errors"""
        error_msg = f"File {operation} error for {file_path}: {str(error)}"
        logger.error(error_msg)
    
    @staticmethod
    def handle_automation_error(command: str, error: Exception) -> str:
        """Handle automation errors"""
        error_msg = f"Automation error for '{command}': {str(error)}"
        logger.error(error_msg)
        return f"I couldn't execute '{command}'. Please try again or check the command syntax."

def validate_environment() -> Dict[str, Any]:
    """Validate the environment setup"""
    validation = config.validate_config()
    
    # Additional checks
    try:
        import groq
        validation["groq_available"] = True
    except ImportError:
        validation["groq_available"] = False
        validation["warnings"].append("Groq library not installed")
    
    try:
        import cohere
        validation["cohere_available"] = True
    except ImportError:
        validation["cohere_available"] = False
        validation["warnings"].append("Cohere library not installed")
    
    try:
        import pyttsx3
        validation["tts_available"] = True
    except ImportError:
        validation["tts_available"] = False
        validation["warnings"].append("Text-to-speech library not installed")
    
    return validation

def setup_directories() -> None:
    """Setup required directories"""
    directories = [
        config.DATA_DIR,
        config.FILES_DIR,
        config.DATA_DIR / "voice",
        config.DATA_DIR / "images",
        config.DATA_DIR / "logs"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        logger.info(f"Directory ensured: {directory}")

def cleanup_temp_files() -> None:
    """Clean up temporary files"""
    temp_patterns = [
        config.DATA_DIR / "*.tmp",
        config.DATA_DIR / "voice" / "*.html",
        config.FILES_DIR / "*.temp"
    ]
    
    for pattern in temp_patterns:
        for file_path in pattern.parent.glob(pattern.name):
            try:
                file_path.unlink()
                logger.info(f"Cleaned up: {file_path}")
            except Exception as e:
                logger.warning(f"Could not clean up {file_path}: {e}")

async def async_retry(func, max_retries: int = 3, delay: float = 1.0):
    """Retry async function with exponential backoff"""
    for attempt in range(max_retries):
        try:
            return await func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            await asyncio.sleep(delay * (2 ** attempt))
            logger.warning(f"Retry {attempt + 1}/{max_retries} for {func.__name__}: {e}")

def format_response(text: str, max_length: int = 1000) -> str:
    """Format response text for display"""
    if not text:
        return ""
    
    # Clean up text
    text = text.strip()
    text = ' '.join(text.split())  # Normalize whitespace
    
    # Truncate if too long
    if len(text) > max_length:
        text = text[:max_length - 3] + "..."
    
    return text

def get_system_info() -> Dict[str, Any]:
    """Get system information"""
    import platform
    import psutil
    
    return {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "python_version": platform.python_version(),
        "cpu_count": psutil.cpu_count(),
        "memory_total": psutil.virtual_memory().total,
        "memory_available": psutil.virtual_memory().available,
        "disk_usage": psutil.disk_usage('/').percent if platform.system() != "Windows" else psutil.disk_usage('C:').percent
    }