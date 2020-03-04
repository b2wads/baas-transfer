from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str
    saldo: int

class Transfer(BaseModel):
    origem: str
    destino: str
    valor: int
