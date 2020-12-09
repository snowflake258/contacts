import pytest
from api.injectors import RepInjector


class TestGroupView:
    @pytest.fixture
    async def group_id(self):
        rep = RepInjector.group_rep()
        result = await rep.add({'name': 'Test Group'})

        yield result['id']

        if await rep.exists(result['id']):
            await rep.delete(result['id'])

    async def test_get(self, client, group_id):
        resp = await client.get('/group')
        assert resp.status == 200

        resp = await client.get(f'/group/{group_id}')
        assert resp.status == 200

        resp = await client.get('/group/0')
        assert resp.status == 400

    async def test_post(self, client):
        resp = await client.post('/group', data={'name': 'Test Group'})
        assert resp.status == 200

        resp = await client.post('/group', data={})
        assert resp.status == 422

    async def test_put(self, client, group_id):
        resp = await client.put(f'/group/{group_id}', data={'name': 'Test Group'})
        assert resp.status == 200

        resp = await client.put(
            f'/group/{group_id}',
            data={'name': 'Test Group Test Group Test Group Test Group Test Group Test Group Test Group Test Group'}
        )
        assert resp.status == 422

    async def test_delete(self, client, group_id):
        resp = await client.delete(f'/group/{group_id}')
        assert resp.status == 200
