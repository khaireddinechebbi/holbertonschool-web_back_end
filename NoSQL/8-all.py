#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    Args:
        mongo_collection (Collection): collection object.
    """
    documents = mongo_collection.find()
    return documents
