from typing import List

from aiohttp import web
from asyncworker import RouteTypes

from baas.app import app
from baas.http import parse_body, parse_id
from baas.models import Transfer
from baas.services.transfer import TransferService


@app.route(["/transfer/"], type=RouteTypes.HTTP, methods=["POST"])
@parse_body(Transfer)
async def transfer(transfer: Transfer) -> Transfer:
    t = await TransferService.save_transfer(transfer.origem, transfer)
    return web.json_response(t.dict())


@app.route(["/transfers/{acc_id}"], type=RouteTypes.HTTP, methods=["GET"])
@parse_id(str)
async def lista_transfers(acc_id: str) -> List[Transfer]:
    transfers = TransferService.list_by_origem_id(acc_id)
    return web.json_response([t.dict() for t in transfers])


@app.route(["/health"], type=RouteTypes.HTTP, methods=["GET"])
async def health():
    return web.json_response({"OK": True})
