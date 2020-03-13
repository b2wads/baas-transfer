from collections import defaultdict
from typing import Optional, List

from baas.models import Transfer, Account


class TransferStorage:
    def __init__(self):
        self.__data = defaultdict(list)

    def save(self, origem_id: str, transfer: Transfer):
        self.__data[origem_id].append(transfer)

    def get_by_origem_id(self, acc_id: str) -> List[Transfer]:
        return self.__data[acc_id] if acc_id in self.__data else []

    def clear(self):
        self.__data = defaultdict(list)


class TransferService:

    storage = TransferStorage()

    @classmethod
    def save_transfer(cls, origem: Account, transfer: Transfer):
    async def save_transfer(
        cls, origem: Account, transfer: Transfer
    ) -> Transfer:

    @classmethod
    def list_by_origem_id(cls, origem_id: str):
        raise NotImplementedError
