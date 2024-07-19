# database_router.py

class MongoRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'mongo_app':  # Remplacez par l'app contenant les modèles MongoDB
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'mongo_app':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'mongo_app' or obj2._meta.app_label == 'mongo_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'mongo_app':
            return db == 'mongodb'
        return db == 'default'
