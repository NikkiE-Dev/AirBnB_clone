#!/usr/bin/python3
"""
This module creates a unique FileStorage instance
for your application
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
