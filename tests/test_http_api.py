from aioresponses import aioresponses
from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from baas.api import app


class TransferAPITest(TestCase):
    async def test_health(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/health")
            data = await resp.json()
            self.assertEqual({"OK": True}, data)
