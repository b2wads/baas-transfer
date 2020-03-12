from aioresponses import aioresponses
from asynctest import TestCase

from baas.clients.account import AccountClient
from baas.models import Account, Transfer


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

    async def test_debito(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        with aioresponses() as rsps:
            rsps.post(
                "http://accounts.api/accounts/42/debito",
                payload={**acc.dict(), "saldo": 300},
                status=200,
            )

            account = await AccountClient.debito(acc, 100)
            self.assertEqual(300, account.saldo)

    async def test_credito(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        with aioresponses() as rsps:
            rsps.post(
                "http://accounts.api/accounts/42/credito",
                payload={**acc.dict(), "saldo": 500},
                status=200,
            )

            account = await AccountClient.credito(acc, 100)
            self.assertEqual(500, account.saldo)
