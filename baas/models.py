from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    nome: Optional[str]
    cpf: str
    saldo: Optional[int]


class Transfer(BaseModel):
    origem: Account
    destino: Account
    valor: int
