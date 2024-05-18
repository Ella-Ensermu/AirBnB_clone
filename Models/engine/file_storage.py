#!/usr/bin/python3
"""Defines FileStorage class."""


import uuid
import os
import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place


class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Review": Review,
    "State": State
    "Place": Place,
    "Amenity": Amenity,
}


class FileStorage:
    """ construct FileStorage """

    __file_path = "file.json"
    __objects = {}


def all(self):
       """Returns the dictionary of objects"""
        return FileStorage.__objects


def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)


def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj


def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except Exception:
                pass


def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

