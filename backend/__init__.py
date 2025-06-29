"""
JARVIS AI Assistant Backend Package
"""

from .config import config
from .utils import (
    FileManager,
    StatusManager,
    MessageManager,
    ErrorHandler,
    validate_environment,
    setup_directories,
    cleanup_temp_files
)

__version__ = "4.0.0"
__author__ = "JARVIS Development Team"

# Initialize backend
setup_directories()

__all__ = [
    "config",
    "FileManager",
    "StatusManager", 
    "MessageManager",
    "ErrorHandler",
    "validate_environment",
    "setup_directories",
    "cleanup_temp_files"
]