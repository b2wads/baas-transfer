from asynctest import TestCase

from baas.models import Transfer, Account
from baas.services.transfer import TransferStorage


class StorageTest(TestCase):
    async def setUp(self):
        self.storage = TransferStorage()

    async def test_get_by_origem_id(self):
        transfer = Transfer(origem="1234", destino="4312", valor=123)
        self.storage.save(transfer.origem, transfer=transfer)
        transfers = self.storage.get_by_origem_id("1234")
        self.assertEqual(1, len(transfers))
        self.assertEqual(transfer.dict(), transfers[0].dict())

    async def test_get_by_multiple_origem_id(self):
        transfer = Transfer(origem="1234", destino="4321", valor=123)
        self.storage.save(origem_id="1234", transfer=transfer)
        self.storage.save(origem_id="1234", transfer=transfer)
        self.storage.save(origem_id="2253", transfer=transfer)

        transfers_acc_1234 = self.storage.get_by_origem_id("1234")
        transfers_acc_2253 = self.storage.get_by_origem_id("2253")

        self.assertEqual(2, len(transfers_acc_1234))
        self.assertEqual(1, len(transfers_acc_2253))

    async def test_get_by_origem_id_empty_list(self):
        self.assertEqual([], self.storage.get_by_origem_id("2273"))
