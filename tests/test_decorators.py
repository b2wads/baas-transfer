from http import HTTPStatus
from typing import List, Optional

from aiohttp import web
from asynctest import TestCase
from asyncworker.http.wrapper import RequestWrapper
from asyncworker.testing import HttpClientContext
from pydantic import BaseModel

from baas.app import MyApp
from baas.http import parse_body


class Model(BaseModel):
    name: str
    numero: int


class HTTPDecoratorsTest(TestCase):
    async def setUp(self):
        self.app = MyApp()

        @self.app.http(["/body"], methods=["POST"])
        @parse_body(Model)
        async def parse_body_handler(m: Model):
            return web.json_response(m.dict())

        @self.app.http(["/get_by_id/{id}"], methods=["POST"])
        async def parse_path_handler(id_: int):
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


class HTTPRouteDecoratorTest(TestCase):
    async def setUp(self):
        self.app = MyApp()

    async def test_registers_http_route(self):
        @self.app.http(["/hello"])
        async def _hello_handler():
            return web.json_response({"Hello": True})

        async with HttpClientContext(self.app) as client:
            resp = await client.get("/hello")

            self.assertEqual(HTTPStatus.OK, resp.status)
            data = await resp.json()

            self.assertEqual({"Hello": True}, data)

    async def test_can_use_other_http_methods(self):
        expected_response_data = {"POST": True}

        @self.app.http(["/post"], methods=["POST"])
        async def _get_post(wrapper: RequestWrapper):
            body = await wrapper.http_request.json()
            return web.json_response(body)

        async with HttpClientContext(self.app) as client:
            resp = await client.post("/post", json=expected_response_data)
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual(expected_response_data, data)

    async def test_can_return_pydantic_model(self):
        class User(BaseModel):
            id: str

        @self.app.http(["/users/{user_id}"])
        async def _get_user_by_id(user_id: str) -> User:
            return User(id=user_id)

        async with HttpClientContext(self.app) as client:
            resp = await client.get("/users/42")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual(User(id="42").dict(), data)

    async def test_can_return_list_of_pydnatic_models(self):
        class User(BaseModel):
            id: str

        @self.app.http(["/users/{user_id}/{other_id}"])
        async def _get_user_by_id(user_id: str, other_id: str) -> List[User]:
            return [User(id=user_id), User(id=other_id)]

        async with HttpClientContext(self.app) as client:
            resp = await client.get("/users/42/44")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual([User(id="42").dict(), User(id="44").dict()], data)

    async def test_can_return_optional_model(self):
        class User(BaseModel):
            id: str

        @self.app.http(["/users/{user_id}/{other_id}"])
        async def _get_user_by_id(
            user_id: str, other_id: str
        ) -> Optional[User]:
            return None

        async with HttpClientContext(self.app) as client:
            resp = await client.get("/users/42/44")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({}, data)
