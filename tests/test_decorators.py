from aiohttp import web
from asynctest import TestCase
from asyncworker import App, RouteTypes
from asyncworker.testing import HttpClientContext
from pydantic import BaseModel

from baas.http import parse_body, parse_id


class Model(BaseModel):
    name: str
    numero: int


class HTTPDecoratorsTest(TestCase):
    async def setUp(self):
        self.app = App()

        @self.app.route(["/body"], type=RouteTypes.HTTP, methods=["POST"])
        @parse_body(Model)
        async def parse_body_handler(m: Model):
            return web.json_response(m.dict())

        @self.app.route(
            ["/get_by_id/{id}"], type=RouteTypes.HTTP, methods=["POST"]
        )
        @parse_id(int)
        async def parse_body_handler(id_: int):
            m = Model(name="Dalton", numero=id_)
            return web.json_response(m.dict())

    async def test_parse_body(self):
        async with HttpClientContext(self.app) as client:
            resp = await client.post(
                "/body", json=Model(name="Dalton", numero=42).dict()
            )
            data = await resp.json()
            self.assertEqual({"name": "Dalton", "numero": 42}, data)

    async def test_parse_path_param(self):
        async with HttpClientContext(self.app) as client:
            resp = await client.post("/get_by_id/42")
            data = await resp.json()
            self.assertEqual({"name": "Dalton", "numero": 42}, data)
