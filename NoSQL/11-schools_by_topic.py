#!/usr/bin/env python3
"""
Module for retrieving schools by topic in a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school documents that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: The topic to search for.

    Returns:
        List[dict]: A list of dictionaries representing the school documents.
    """
    return list(mongo_collection.find({"topics": topic}))
