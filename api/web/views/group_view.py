from aiohttp.web import View, json_response
from aiohttp_apispec import request_schema
from api.web.schemes import GroupScheme
from api.injectors import RepInjector


class GroupView(View):
    def __init__(self, request):
        super().__init__(request)
        self.__group_rep = RepInjector.group_rep()

    async def get(self):
        result = await self.__group_rep.get(self.__id)
        return json_response(result)

    @request_schema(GroupScheme())
    async def post(self):
        result = await self.__group_rep.add(self.request['data'])
        return json_response(result)

    @request_schema(GroupScheme())
    async def put(self):
        await self.__group_rep.update(self.__id, self.request['data'])
        return json_response()

    async def delete(self):
        await self.__group_rep.delete(self.__id)
        return json_response()

    @property
    def __id(self):
        return self.request.match_info.get('id', None)
