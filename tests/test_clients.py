from aioresponses import aioresponses
from asynctest import TestCase
from tests import mock_account_client

from baas.clients.account import AccountClient
from baas.models import Account


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
        with mock_account_client(acc, acc):
            await AccountClient.debito(acc, 100)
            account = await AccountClient.get_by_id(acc.cpf)
            self.assertEqual(300, account.saldo)

    async def test_credito(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        with mock_account_client(acc, acc):
            await AccountClient.credito(acc, 100)
            account = await AccountClient.get_by_id(acc.cpf)
            self.assertEqual(500, account.saldo)
