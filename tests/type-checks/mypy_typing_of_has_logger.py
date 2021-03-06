import logging
from eth_utils import HasLogger, HasExtendedDebugLogger, ExtendedDebugLogger


def verify_has_logger_type() -> logging.Logger:
    return HasLogger.logger


def verify_has_extended_debug_logger_type() -> ExtendedDebugLogger:
    return HasExtendedDebugLogger.logger
