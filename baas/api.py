from aiohttp import web
from asyncworker import RouteTypes
from asyncworker.http.decorators import parse_path

from baas.app import app
from baas.http import parse_body
from baas.models import Transfer
from baas.services.transfer import TransferService


@app.http(["/transfers"], methods=["POST"])
@parse_body(Transfer)
async def transfer(transfer: Transfer):
    t = await TransferService.save_transfer(transfer.origem, transfer)
    return web.json_response(t.dict())


@app.http(["/transfers/{acc_id}"])
async def lista_transfers(acc_id: str):
    transfers = TransferService.list_by_origem_id(acc_id)
    return web.json_response([t.dict() for t in transfers])


@app.http(["/health"])
async def health():
    return web.json_response({"OK": True})
