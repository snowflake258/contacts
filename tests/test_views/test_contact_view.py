import pytest
from api.db.reps import GroupRep, ContactRep
from api.injectors import RepInjector


class TestContactView:
    @staticmethod
    def __get_contact_data(group_id):
        return {
            "firstname": "Test Firstname",
            "lastname": "Test Lastname",
            "phone": "+0-000-000-00-00",
            "group_id": group_id
        }

    @pytest.fixture
    async def data(self):
        group_rep = RepInjector.group_rep()
        contact_rep = RepInjector.contact_rep()

        group_id = (await group_rep.add({'name': 'Test Group'}))['id']
        contact_id = (await contact_rep.add(self.__get_contact_data(group_id)))['id']

        yield {'contact_id': contact_id, 'group_id': group_id}

        await group_rep.delete(group_id)

    async def test_post(self, client, data):
        resp = await client.post('/contact', data=self.__get_contact_data(data['group_id']))
        assert resp.status == 200

        resp = await client.post('/contact', data={})
        assert resp.status == 422

    async def test_put(self, client, data):
        resp = await client.put(f'/contact/{data["contact_id"]}', data=self.__get_contact_data(data['group_id']))
        assert resp.status == 200

    async def test_delete(self, client, data):
        resp = await client.delete(f'/contact/{data["contact_id"]}')
        assert resp.status == 200
