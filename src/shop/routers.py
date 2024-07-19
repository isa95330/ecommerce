from django.db import connections
from django.db.utils import ConnectionHandler
from django.utils.deprecation import MiddlewareMixin

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """
        Routes read operations for MongoDB.
        """
        if model._meta.app_label == 'shop':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Routes write operations for MongoDB.
        """
        if model._meta.app_label == 'shop':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the same app label.
        """
        if obj1._meta.app_label == 'shop' or obj2._meta.app_label == 'shop':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Prevent migration on the MongoDB database.
        """
        if app_label == 'shop':
            return db == 'mongodb'
        return db == 'default'
