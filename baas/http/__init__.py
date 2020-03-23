from typing import Type

from asyncworker.http.wrapper import RequestWrapper
from asyncworker.routes import call_http_handler


def parse_body(model: Type):
    def _wrap_(f):
        async def _wrap(wrapper: RequestWrapper):
            data = await wrapper.http_request.json()
            acc = model(**data)
            wrapper.types_registry.set(acc)
            return await call_http_handler(wrapper.http_request, f)

        return _wrap

    return _wrap_
