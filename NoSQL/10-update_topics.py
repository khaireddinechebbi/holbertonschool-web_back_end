#!/usr/bin/env python3
"""
Module for updating topics in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document in a MongoDB collection based on the school name.

    Args:
        mongo_collection: The pymongo collection object.
        name: The name of the school to update.
        topics: The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
