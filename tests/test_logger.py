"""Tests for the logger utility."""

import logging
import tempfile
from pathlib import Path

import pytest

from src.utils.logger import setup_logger, get_logger, LoggerContext


class TestLogger:
    """Test suite for logger utilities."""
    
    def test_setup_logger_basic(self):
        """Test basic logger setup."""
        logger = setup_logger("test_logger", level=logging.INFO)
        
        assert logger.name == "test_logger"
        assert logger.level == logging.INFO
        assert len(logger.handlers) > 0
    
    def test_setup_logger_with_file(self):
        """Test logger setup with file handler."""
        with tempfile.TemporaryDirectory() as tmpdir:
            logger = setup_logger(
                "test_file_logger",
                log_file="test.log",
                log_dir=tmpdir
            )
            
            log_path = Path(tmpdir) / "test.log"
            assert log_path.exists()
    
    def test_get_logger(self):
        """Test getting existing logger."""
        logger1 = setup_logger("test_get_logger")
        logger2 = get_logger("test_get_logger")
        
        assert logger1 is logger2
    
    def test_logger_context(self):
        """Test logger context manager."""
        logger = setup_logger("test_context", level=logging.INFO)
        original_level = logger.level
        
        with LoggerContext(logger, logging.ERROR):
            assert logger.level == logging.ERROR
        
        assert logger.level == original_level
    
    def test_logger_no_duplicate_handlers(self):
        """Test that calling setup_logger twice doesn't duplicate handlers."""
        logger1 = setup_logger("test_duplicate")
        handler_count1 = len(logger1.handlers)
        
        logger2 = setup_logger("test_duplicate")
        handler_count2 = len(logger2.handlers)
        
        assert handler_count1 == handler_count2
