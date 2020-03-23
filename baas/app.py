from typing import List

from aiohttp import web
from asyncworker import App, RouteTypes
from asyncworker.http.decorators import parse_path
from asyncworker.http.wrapper import RequestWrapper
from asyncworker.routes import call_http_handler


class MyApp(App):
    def http(self, routes: List[str], methods: List[str] = ["GET"]):
        def _wrap(handler):
            return self.route(routes, type=RouteTypes.HTTP, methods=methods)(
                self._unwrap_pydantic_model(parse_path(handler))
            )

        return _wrap

    def _unwrap_pydantic_model(self, handler):
        async def _handler_wrapper(wrapper: RequestWrapper):
            response = await call_http_handler(wrapper.http_request, handler)
            try:
                if isinstance(response, list):
                    return web.json_response([o.dict() for o in response])
                elif response is None:
                    return web.json_response({})

                return web.json_response(response.dict())
            except AttributeError:
                return response

        return _handler_wrapper


app = MyApp()
