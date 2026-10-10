"""
Mock REST Server - Dinamik soxta REST API generatsiya qiluvchi va test serveri.
"""

from .generator import SchemaDataGenerator
from .server import MockRESTEngine

__version__ = "1.0.0"
__all__ = ["SchemaDataGenerator", "MockRESTEngine"]
