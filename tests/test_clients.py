from aioresponses import aioresponses
from asynctest import TestCase

from baas.clients.account import AccountClient
from baas.models import Account, Saque


class AccountClientTest(TestCase):
    async def test_get_by_id(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        with aioresponses() as rsps:
            rsps.get(
                "http://accounts.api/accounts/42",
                payload=acc.dict(),
                status=200,
            )

            account = await AccountClient.get_by_id("42")
            self.assertEqual(acc.dict(), account.dict())

    async def test_update_account(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        with aioresponses() as rsps:
            rsps.post(
                "http://accounts.api/accounts", payload=acc.dict(), status=200
            )

            account = await AccountClient.update_account(acc)
            self.assertEqual(acc.dict(), account.dict())

    async def test_saque_account(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        saque = Saque(data="2020-02-26", valor=200)
        with aioresponses() as rsps:
            rsps.post(
                "http://accounts.api/accounts/42/debito",
                payload=saque.dict(),
                status=200,
            )

            saque_resp = await AccountClient.saque(acc, saque)
            self.assertEqual(saque_resp.dict(), saque.dict())
