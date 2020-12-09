from dependency_injector import containers, providers
from api.db.managers import DbManager


class ManagerInjector(containers.DeclarativeContainer):
    db_manager = providers.Singleton(DbManager)
