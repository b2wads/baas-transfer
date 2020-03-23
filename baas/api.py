from typing import List

from aiohttp import web

from baas.app import app
from baas.http import parse_body
from baas.models import Transfer
from baas.services.transfer import TransferService


@app.http(["/transfers"], methods=["POST"])
@parse_body(Transfer)
async def transfer(transfer: Transfer) -> Transfer:
    return await TransferService.save_transfer(transfer.origem, transfer)


@app.http(["/transfers/{acc_id}"])
async def lista_transfers(acc_id: str) -> List[Transfer]:
    return TransferService.list_by_origem_id(acc_id)


@app.http(["/health"])
async def health():
    return web.json_response({"OK": True})
