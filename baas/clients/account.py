from aiohttp.client import ClientSession

from baas.conf import settings
from baas.models import Account, Saque


class AccountClient:
    @classmethod
    async def get_by_id(cls, acc_id) -> Account:
        async with ClientSession() as session:
            async with session.get(
                f"{settings.ACCOUNT_SERVICE_ADDRESS}/accounts/{acc_id}"
            ) as resp:
                data = await resp.json()
                return Account(**data)

    @classmethod
    async def update_account(cls, account: Account) -> Account:
        async with ClientSession() as session:
            async with session.post(
                f"{settings.ACCOUNT_SERVICE_ADDRESS}/accounts",
                json=account.dict(),
            ) as resp:
                data = await resp.json()
                return Account(**data)

    @classmethod
    async def saque(cls, account: Account, saque: Saque) -> Saque:
        async with ClientSession() as session:
            async with session.post(
                f"{settings.ACCOUNT_SERVICE_ADDRESS}/accounts/{account.cpf}/debito",
                json=saque.dict(),
            ) as resp:
                data = await resp.json()
                return Saque(**data)
