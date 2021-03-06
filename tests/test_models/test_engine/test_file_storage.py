#!/usr/bin/python3
"""A module for unittests for the base model class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


fs = FileStorage()
class TestFileStorage(unittest.TestCase):
    """A class to test BaseModel & File storage"""
    def test_filestorage_save(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        self.assertNotEqual(os.path.getsize(fs._FileStorage__file_path), 0)
    def test_filestorage_new(self):
        bm1 = BaseModel()
        self.assertNotEqual(len(fs._FileStorage__objects), 0)
    def test_file_storage_all(self):
        bm1 = BaseModel()
        self.assertIsInstance(fs.all(), dict)
    def test_file_storage(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        fs.reload()
        new = fs._FileStorage__objects.copy()
        bm1.my_number = 69
        self.assertEqual(bm1.my_number, 69)
        fs.reload()
        self.assertNotEqual(new, fs._FileStorage__objects)

    def test_file_storage_objects(self):
        bm1 = FileStorage()
        self.assertIsInstance(fs._FileStorage__objects, dict)

if __name__ == '__main__':
    unittest.main()
