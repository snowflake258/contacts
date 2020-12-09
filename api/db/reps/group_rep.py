from typing import Union
from api.injectors import ManagerInjector
from api.db.models import group


class GroupRep:
    def __init__(self):
        self.__db_manager = ManagerInjector.db_manager()

    async def exists(self, id: int) -> bool:
        result = await self.__db_manager.query_list(group.select().where(group.c.id == id))

        if len(result) == 0:
            return False
        return True

    async def get(self, id: int) -> Union[dict, list]:
        query = self.__define_query_for_get(id)
        return await self.__get(id, query)

    @staticmethod
    def __define_query_for_get(id: int):
        if id is None:
            return group.select()
        else:
            return group.select().where(group.c.id == id)

    async def __get(self, id: int, query):
        if id is None:
            result = await self.__db_manager.query_list(query)
            return [dict(item) for item in result]
        else:
            await self.__check_id(id)
            result = await self.__db_manager.query_record(query)
            return dict(result)

    async def add(self, data: dict) -> dict:
        result = await self.__db_manager.query_scalar(group.insert().values(**data))
        return {'id': result}

    async def update(self, id: int, data: dict) -> None:
        await self.__check_id(id)
        await self.__db_manager.query(group.update().where(group.c.id == id).values(**data))

    async def delete(self, id: int) -> None:
        await self.__check_id(id)
        await self.__db_manager.query(group.delete().where(group.c.id == id))

    async def __check_id(self, id: int):
        if not await self.exists(id):
            raise ValueError('Incorrect identifier.')
