"""project-wide exception hierarchy"""


class LogwashError(Exception):
    """base error for all logwash failures"""


class ConfigError(LogwashError):
    """bad or missing configuration"""


class InputError(LogwashError):
    """the user gave us something we cannot use"""
