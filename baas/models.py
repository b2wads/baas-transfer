from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str
    saldo: int


class Saque(BaseModel):
    data: str
    valor: int
    account: Optional[Account]
