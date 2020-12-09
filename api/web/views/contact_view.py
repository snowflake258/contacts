from aiohttp.web import View, json_response
from aiohttp_apispec import request_schema
from api.web.schemes import ContactSchema
from api.injectors import RepInjector


class ContactView(View):
    def __init__(self, request):
        super().__init__(request)
        self.__contact_rep = RepInjector.contact_rep()

    @request_schema(ContactSchema)
    async def post(self):
        result = await self.__contact_rep.add(self.request['data'])
        return json_response(result)

    @request_schema(ContactSchema)
    async def put(self):
        await self.__contact_rep.update(self.__id, self.request['data'])
        return json_response()

    async def delete(self):
        await self.__contact_rep.delete(self.__id)
        return json_response()

    @property
    def __id(self):
        return self.request.match_info.get('id', None)
