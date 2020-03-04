from asynctest import TestCase, mock

from baas.models import Saque
from baas.services.saque import SaqueService, SaqueStorage


class ServiceTest(TestCase):
    async def test_list_saques_by_acc_id(self):
        storage = SaqueStorage()
        with mock.patch.object(SaqueService, "storage", storage):
            saque = Saque(data="2020-02-26", valor=200)
            storage.save("123", saque)
            self.assertEqual([saque], SaqueService.list_by_acc_id("123"))

    async def test_list_saques_by_acc_id_empty_result(self):
        self.assertEqual([], SaqueService.list_by_acc_id("42"))

    async def test_list_saques_by_date(self):
        storage = SaqueStorage()
        with mock.patch.object(SaqueService, "storage", storage):
            saque_1 = Saque(data="2020-02-26", valor=200)
            saque_2 = Saque(data="2020-02-26", valor=300)
            storage.save("123", saque_1)
            storage.save("123", saque_2)
            self.assertEqual(
                [saque_1, saque_2],
                SaqueService.list_by_date("123", "2020-02-26"),
            )

    async def test_list_saques_by_date_empty_result(self):
        self.assertEqual([], SaqueService.list_by_date("42", "2020-02-26"))
