"""
Configuration management for JARVIS AI Assistant
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict, Any, Optional

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for JARVIS AI Assistant"""
    
    # Base paths
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    FRONTEND_DIR = BASE_DIR / "frountend"
    GRAPHICS_DIR = FRONTEND_DIR / "Graphics"
    FILES_DIR = FRONTEND_DIR / "Files"
    
    # Ensure directories exist
    DATA_DIR.mkdir(exist_ok=True)
    FILES_DIR.mkdir(exist_ok=True)
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY", "")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
    
    # Default AI Provider
    DEFAULT_AI_PROVIDER = os.getenv("DEFAULT_AI_PROVIDER", "groq")
    
    # User Configuration
    USERNAME = os.getenv("USERNAME", "User")
    ASSISTANTNAME = os.getenv("ASSISTANTNAME", "JARVIS")
    INPUT_LANGUAGE = os.getenv("INPUT_LANGUAGE", "en-US")
    ASSISTANT_VOICE = os.getenv("ASSISTANT_VOICE", "Microsoft David - English (United States)")
    
    # Voice Configuration
    VOICE_RATE = float(os.getenv("VOICE_RATE", "0.9"))
    VOICE_PITCH = float(os.getenv("VOICE_PITCH", "0.6"))
    VOICE_VOLUME = float(os.getenv("VOICE_VOLUME", "0.9"))
    
    # Application Settings
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "info").upper()
    
    # File paths
    CHAT_LOG_FILE = DATA_DIR / "ChatLog.json"
    STATUS_FILE = FILES_DIR / "status.data"
    MIC_FILE = FILES_DIR / "mic.data"
    RESPONSES_FILE = FILES_DIR / "Responses.data"
    DATABASE_FILE = FILES_DIR / "database.data"
    IMAGE_GEN_FILE = FILES_DIR / "imagegenration.data"
    
    @classmethod
    def validate_config(cls) -> Dict[str, Any]:
        """Validate configuration and return status"""
        issues = []
        warnings = []
        
        # Check API keys
        if not cls.GROQ_API_KEY:
            issues.append("GROQ_API_KEY is not set")
        if not cls.COHERE_API_KEY:
            warnings.append("COHERE_API_KEY is not set (optional)")
        if not cls.GEMINI_API_KEY:
            warnings.append("GEMINI_API_KEY is not set (optional)")
        
        # Check directories
        required_dirs = [cls.DATA_DIR, cls.FILES_DIR]
        for dir_path in required_dirs:
            if not dir_path.exists():
                issues.append(f"Required directory does not exist: {dir_path}")
        
        # Check voice settings
        if not (0.1 <= cls.VOICE_RATE <= 2.0):
            warnings.append(f"VOICE_RATE ({cls.VOICE_RATE}) should be between 0.1 and 2.0")
        if not (0.0 <= cls.VOICE_PITCH <= 2.0):
            warnings.append(f"VOICE_PITCH ({cls.VOICE_PITCH}) should be between 0.0 and 2.0")
        if not (0.0 <= cls.VOICE_VOLUME <= 1.0):
            warnings.append(f"VOICE_VOLUME ({cls.VOICE_VOLUME}) should be between 0.0 and 1.0")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings,
            "config": {
                "username": cls.USERNAME,
                "assistant_name": cls.ASSISTANTNAME,
                "input_language": cls.INPUT_LANGUAGE,
                "default_provider": cls.DEFAULT_AI_PROVIDER,
                "debug": cls.DEBUG
            }
        }
    
    @classmethod
    def get_file_path(cls, file_type: str) -> Path:
        """Get file path for specific file types"""
        file_map = {
            "chat_log": cls.CHAT_LOG_FILE,
            "status": cls.STATUS_FILE,
            "mic": cls.MIC_FILE,
            "responses": cls.RESPONSES_FILE,
            "database": cls.DATABASE_FILE,
            "image_gen": cls.IMAGE_GEN_FILE,
        }
        return file_map.get(file_type, cls.DATA_DIR / f"{file_type}.data")

# Global config instance
config = Config()