#!/usr/bin/env python3
"""
JARVIS AI Assistant Launcher
"""
import sys
import os
import argparse
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from backend import validate_environment, setup_directories, config

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config.DATA_DIR / 'jarvis.log'),
            logging.StreamHandler()
        ]
    )

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'groq', 'cohere', 'python-dotenv', 'rich', 'selenium', 
        'webdriver-manager', 'beautifulsoup4', 'requests', 
        'pyttsx3', 'PyQt5'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("Please install them using: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed")
    return True

def run_gui():
    """Run the GUI version"""
    try:
        from frountend.GUI import GraphicalUserInterface
        print("🚀 Starting JARVIS GUI...")
        GraphicalUserInterface()
    except ImportError as e:
        print(f"❌ Error importing GUI: {e}")
        print("Make sure PyQt5 is installed: pip install PyQt5")
    except Exception as e:
        print(f"❌ Error starting GUI: {e}")

def run_web():
    """Run the web version"""
    try:
        import subprocess
        print("🌐 Starting JARVIS Web Interface...")
        subprocess.run(["npm", "run", "dev"], cwd=project_root, check=True)
    except FileNotFoundError:
        print("❌ Node.js/npm not found. Please install Node.js to run the web interface.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting web interface: {e}")

def run_console():
    """Run the console version"""
    try:
        from backend.chatbot import Chatbot
        print("💬 Starting JARVIS Console Mode...")
        print("Type 'exit' to quit")
        
        while True:
            user_input = input("\n🎤 You: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("👋 Goodbye!")
                break
            
            if user_input:
                response = Chatbot(user_input)
                print(f"🤖 JARVIS: {response}")
    
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error in console mode: {e}")

def main():
    """Main launcher function"""
    parser = argparse.ArgumentParser(description="JARVIS AI Assistant")
    parser.add_argument(
        "--mode", 
        choices=["gui", "web", "console", "check"], 
        default="gui",
        help="Run mode (default: gui)"
    )
    parser.add_argument(
        "--debug", 
        action="store_true", 
        help="Enable debug mode"
    )
    parser.add_argument(
        "--setup", 
        action="store_true", 
        help="Run initial setup"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    print("🤖 JARVIS AI Assistant v4.0")
    print("=" * 40)
    
    # Run setup if requested
    if args.setup:
        print("🔧 Running initial setup...")
        setup_directories()
        
        # Create .env file if it doesn't exist
        env_file = project_root / ".env"
        if not env_file.exists():
            example_env = project_root / ".env.example"
            if example_env.exists():
                import shutil
                shutil.copy(example_env, env_file)
                print("📝 Created .env file from template")
                print("Please edit .env file with your API keys")
            else:
                print("⚠️  .env.example not found")
        
        print("✅ Setup complete!")
        return
    
    # Validate environment
    if args.mode != "check":
        validation = validate_environment()
        if not validation["valid"]:
            print("❌ Environment validation failed:")
            for issue in validation["issues"]:
                print(f"  - {issue}")
            print("\nPlease fix these issues before running JARVIS")
            return
        
        if validation["warnings"]:
            print("⚠️  Warnings:")
            for warning in validation["warnings"]:
                print(f"  - {warning}")
    
    # Check dependencies
    if args.mode in ["gui", "console"] and not check_dependencies():
        return
    
    # Run based on mode
    if args.mode == "check":
        validation = validate_environment()
        print("🔍 Environment Check Results:")
        print(f"Valid: {'✅' if validation['valid'] else '❌'}")
        if validation["issues"]:
            print("Issues:")
            for issue in validation["issues"]:
                print(f"  - {issue}")
        if validation["warnings"]:
            print("Warnings:")
            for warning in validation["warnings"]:
                print(f"  - {warning}")
        
    elif args.mode == "gui":
        run_gui()
    elif args.mode == "web":
        run_web()
    elif args.mode == "console":
        run_console()

if __name__ == "__main__":
    main()