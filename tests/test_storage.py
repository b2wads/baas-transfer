from asynctest import TestCase

from baas.models import Saque, Account
from baas.services.saque import SaqueStorage


class StorageTest(TestCase):
    async def setUp(self):
        self.storage = SaqueStorage()
        self.account = Account(nome="Dalton", cpf="1234", saldo=1000)
        self.other_account = Account(nome="Outro", cpf="2253", saldo=850)

    async def test_get_by_date(self):
        saque = Saque(data="2020-02-21", valor=250, account=self.account)
        self.storage.save(acc_id="42", saque=saque)

        saques = self.storage.get_by_date("42", "2020-02-21")
        self.assertEqual(1, len(saques))
        self.assertEqual(saque.dict(), saques[0].dict())

    async def test_get_by_acc_id(self):
        saque = Saque(data="2020-02-21", valor=250, account=self.account)
        self.storage.save(acc_id="1234", saque=saque)
        self.storage.save(acc_id="1234", saque=saque)
        self.storage.save(acc_id="2253", saque=saque)

        saques_acc_1234 = self.storage.get_by_acc_id("1234")
        saques_acc_2253 = self.storage.get_by_acc_id("2253")

        self.assertEqual(2, len(saques_acc_1234))
        self.assertEqual(1, len(saques_acc_2253))

    async def test_get_by_acc_id_empty_list(self):
        self.assertEqual([], self.storage.get_by_acc_id("2273"))
