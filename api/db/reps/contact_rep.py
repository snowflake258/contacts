from api.injectors import ManagerInjector
from api.db.models import contact


class ContactRep:
    def __init__(self):
        self.__db_manager = ManagerInjector.db_manager()

    async def exists(self, id: int) -> bool:
        result = await self.__db_manager.query_list(contact.select().where(contact.c.id == id))

        if len(result) == 0:
            return False
        return True

    async def add(self, data: dict) -> dict:
        result = await self.__db_manager.query_scalar(contact.insert().values(**data))
        return {'id': result}

    async def update(self, id: int, data: dict) -> None:
        await self.__check_id(id)
        await self.__db_manager.query(contact.update().where(contact.c.id == id).values(**data))

    async def delete(self, id: int) -> None:
        await self.__check_id(id)
        await self.__db_manager.query(contact.delete().where(contact.c.id == id))

    async def __check_id(self, id: int):
        if not await self.exists(id):
            raise ValueError('Incorrect identifier.')
