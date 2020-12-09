from dependency_injector import containers, providers
from api.db.reps import GroupRep, ContactRep


class RepInjector(containers.DeclarativeContainer):
    group_rep = providers.Singleton(GroupRep)
    contact_rep = providers.Singleton(ContactRep)
