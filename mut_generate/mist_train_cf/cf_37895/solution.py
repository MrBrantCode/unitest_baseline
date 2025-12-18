"""
QUESTION:
Create a class with a method named `allow_migrate` that takes `self`, `db`, `app_label`, and `**hints` as parameters. The `allow_migrate` method should return `True` if the migration for the given `app_label` is allowed on the specified `db` and `False` otherwise. The method should follow these rules: allow migration if the database alias (`db`) matches the app label (`app_label`), and deny migration if they do not match. Assume that only specific database and app label combinations are allowed, as defined in the dictionary `allowed_databases`.
"""

def allow_migrate(self, db, app_label, **hints):
    allowed_databases = {
        'cheapcdn': ['cheapcdn'],
        'lifecycle': ['lifecycle']
    }
    return db in allowed_databases and app_label in allowed_databases[db]