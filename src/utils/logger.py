"""Logging utility for the AI Eye Tracking project."""

import logging
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime


def setup_logger(
    name: str = "ai_eye_tracking",
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    log_dir: str = "logs",
    console_output: bool = True
) -> logging.Logger:
    """
    Set up a logger with console and optional file handlers.
    
    Args:
        name: Name of the logger
        level: Logging level (e.g., logging.INFO, logging.DEBUG)
        log_file: Optional specific log file name
        log_dir: Directory to store log files
        console_output: Whether to output logs to console
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent duplicate handlers if logger already exists
    if logger.handlers:
        return logger
    
    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    # File handler
    if log_file or log_dir:
        log_path = Path(log_dir)
        log_path.mkdir(parents=True, exist_ok=True)
        
        if log_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = f"{name}_{timestamp}.log"
        
        file_handler = logging.FileHandler(log_path / log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_logger(name: str = "ai_eye_tracking") -> logging.Logger:
    """
    Get an existing logger or create a new one with default settings.
    
    Args:
        name: Name of the logger
        
    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    
    # If logger doesn't have handlers, set it up with defaults
    if not logger.handlers:
        return setup_logger(name)
    
    return logger


class LoggerContext:
    """Context manager for temporary logger configuration."""
    
    def __init__(self, logger: logging.Logger, level: int):
        """
        Initialize logger context.
        
        Args:
            logger: Logger to temporarily configure
            level: Temporary logging level
        """
        self.logger = logger
        self.level = level
        self.old_level = None
    
    def __enter__(self):
        """Enter context and set temporary level."""
        self.old_level = self.logger.level
        self.logger.setLevel(self.level)
        return self.logger
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context and restore original level."""
        self.logger.setLevel(self.old_level)


if __name__ == "__main__":
    # Example usage
    logger = setup_logger("test_logger", level=logging.DEBUG, log_file="test.log")
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    # Test context manager
    with LoggerContext(logger, logging.ERROR):
        logger.info("This info message won't appear")
        logger.error("This error message will appear")
    
    logger.info("Back to normal logging")
