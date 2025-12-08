"""Singleton logger for galileo-agents."""
import logging
import sys

_logger = None


def get_logger() -> logging.Logger:
    """Get or create the singleton logger."""
    global _logger
    if _logger is None:
        _logger = logging.getLogger("galileo-agents")
        _logger.setLevel(logging.INFO)
        _logger.propagate = False
        if not _logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            _logger.addHandler(handler)
    return _logger


logger = get_logger()
