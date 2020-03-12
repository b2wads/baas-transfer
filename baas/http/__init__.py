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


def parse_id(param_type: Type):
    def _handler_wrap(f):
        async def _wrap(wrapper: RequestWrapper):
            req = wrapper.http_request
            first_path_param = list(req.match_info.keys())[0]
            param_value = param_type(req.match_info[first_path_param])
            wrapper.types_registry.set(param_value)
            return await call_http_handler(wrapper.http_request, f)

        return _wrap

    return _handler_wrap
