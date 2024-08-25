#!/usr/bin/env python3
"""
Lists all documents in a collection.
"""

from typing import List, Dict
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.

    Returns:
        List[Dict]: A list of dictionaries representing all documents \
        in the collection.
    """
    return list(mongo_collection.find())
