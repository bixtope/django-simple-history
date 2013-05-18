from __future__ import unicode_literals

__version__ = '1.3.0.post1'


def register(model, app=None, manager_name='history'):
    """
    Create historical model for `model` and attach history manager to `model`.

    Keyword arguments:
    app -- App to install historical model into (defaults to model.__module__)
    manager_name -- class attribute name to use for historical manager

    This method should be used as an alternative to attaching an
    `HistoricalManager` instance directly to `model`.
    """
    from . import models
    if not model._meta.db_table in models.registered_models:
        records = models.HistoricalRecords()
        records.manager_name = manager_name
        records.module = app and ("%s.models" % app) or model.__module__
        records.finalize(model)
        models.registered_models[model._meta.db_table] = model
