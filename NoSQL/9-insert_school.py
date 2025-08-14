#!/usr/bin/env python3
"""Module for inserting a new document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: fields for the new document.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
