"""
Functions related to JSON
"""

import json
import exce
from datetime import date, timedelta


def dict_to_json(json_dict):
    """
    convert from a dictionary to json
    """
    return json.dumps(json_dict)


def json_to_dict(json_str):
    """
    convert from json to dictionary
    """
    return json.loads(json_str)


def get_value(json_dict, field):
    """
    Gets the value of a field
    returns the value
    if no such field raises NoField exception
    """
    if not json_dict.has_key(field):
        raise exce.NoField("No such field: %s" %(field))
    return json_dict[field]


def update_dict(json_dict, field, val):
    """
    updates the value of a field
    returns the dict
    if no such field raises NoField exception
    """
    if not json_dict.has_key(field):
        json_dict[field] = []
    json_dict[field].append(val)
    return json_dict
