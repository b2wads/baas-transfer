from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from baas.api import app
from baas.models import Saque
from baas.services.saque import SaqueService


class SaqueAPITest(TestCase):
    async def test_health(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/health")
            data = await resp.json()
            self.assertEqual({"OK": True}, data)
