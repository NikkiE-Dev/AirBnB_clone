#!/usr/bin/python3
""" User Class that inherits from BaseModel """

import json
from models import BaseModel


class User(BaseModel):
    """ Inherited class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
