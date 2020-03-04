from typing import Type

from aiohttp import web
from asyncworker.routes import call_http_handler


def parse_body(model: Type):
    def _wrap_(f):
        async def _wrap(req: web.Request):
            data = await req.json()
            acc = model(**data)
            req["types_registry"].set(acc)
            return await call_http_handler(req, f)

        return _wrap

    return _wrap_


def parse_id(param_type: Type):
    def _handler_wrap(f):
        async def _wrap(req: web.Request):
            first_path_param = list(req.match_info.keys())[0]
            param_value = param_type(req.match_info[first_path_param])
            req["types_registry"].set(param_value)
            return await call_http_handler(req, f)

        return _wrap

    return _handler_wrap
