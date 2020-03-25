# Banco as a Service

O objetivo desse projeto é ensinar um pouco sobre testes. Esse projeto é usado na aula de testes do programa de estágio da B2W Digital.


# Modelos usados no projeto

O Projeto possui dois modelos: `Transfer` e `Account`:

```python
class Account(BaseModel):
    nome: Optional[str]
    cpf: str
    saldo: Optional[int]


class Transfer(BaseModel):
    origem: Account
    destino: Account
    valor: int
```

O modelo principal é o `Transfer` que é usado nos endpoints do projeto.

## Endpoints HTTP

O projeto possui os seguintes endpoints:

- `POST /transfers`: Registra uma nova transferência. Recebe um pbjeto `Transfer` no copro do request;
- `GET /transfers/{acc_id}`: Lista todas as transferências que possuem `acc_id` com conta de origem.

## Funcionalidades

- Registrar uma nova transferência entre duas contas
- Lista todas as transferências saintes de uma mesma conta



# Rodando o projeto localmente

Para rodar o projeto localmente você precisará do `pyenv` e `pipenv`

## Instalando o pyenv

Basta seguir a documentação do projeto: https://github.com/pyenv/pyenv#basic-github-checkout

Resumindo, esses são os passos:

- git clone https://github.com/pyenv/pyenv.git ~/.pyenv
- echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
- echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
- echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

Se você estiver usando outro shell que não seja o bash precisará substituir o `~/.bashrc` pelo arquivo
de configuração do seu shell.

Depois dessa instalação, abra um novo terminal para que essas modificações tenham efeito.

## Instalando python

Depois que o pyenv estiver funcionando é hora de instalar uma versão do python. Para esse projeto podemos
usar python 3.7.5. Para instalar rode:

```
pyenv install 3.7.5
```

**Atenção**: Para Distros baseadas em Debian (Ubuntu, Elementary, etc) instalem os seguintes pacotes:

```
sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```


# Instalando pipenv

Para instalar o pipenv rode:

```
pip install --user pipenv
```

Quando instalamos com `--user` os binários vão para `${HOME}/.local/bin` então é importante adicionar essa pasta em seu `$PATH`.
Isso pode ser feito assim:

```
echo 'export PATH="$PATH:<HOME>/.local/bin"' >> ~/.bashrc
```

Onde `<HOME>` é a pasta onde ficam seus arquivos e configurações. Para descobrir sua home abra um terminal e digite:

```
cd
pwd
```

Isso deve imprimir o endereço da sua home.

A partir dos próximos terminais abertos você já poderá rodar `pipenv` no terminal.

# Instalando o projeto

Depois de fazer o clone desse projeto, entre na pasta onde está o código e digite:

```
pipenv install --dev
```

# Rodando os testes

Para rodas os teses, faça:

```
pipenv run test
```

Todos os testes devem passar.

Você deve ver uma pensagem desse tipo, no final do output: `14 passed, 4 warnings in 0.40s`.

Esse é um exemplo de output:

```
$ pipenv run test
===================================================================================== test session starts =====================================================================================
platform linux -- Python 3.7.5, pytest-5.2.1, py-1.8.1, pluggy-0.13.1 -- /home/daltonmatos/.local/share/virtualenvs/baas-transfer-RPlrfRcH/bin/python3
cachedir: .pytest_cache
rootdir: /home/daltonmatos/src/baas-transfer
plugins: cov-2.8.1
collected 14 items

tests/test_clients.py::AccountClientTest::test_credito PASSED
tests/test_clients.py::AccountClientTest::test_debito PASSED
tests/test_clients.py::AccountClientTest::test_get_by_id PASSED
tests/test_clients.py::AccountClientTest::test_update_account PASSED
tests/test_decorators.py::HTTPDecoratorsTest::test_parse_body PASSED
tests/test_decorators.py::HTTPRouteDecoratorTest::test_can_return_list_of_pydnatic_models PASSED
tests/test_decorators.py::HTTPRouteDecoratorTest::test_can_return_optional_model PASSED
tests/test_decorators.py::HTTPRouteDecoratorTest::test_can_return_pydantic_model PASSED
tests/test_decorators.py::HTTPRouteDecoratorTest::test_can_use_other_http_methods PASSED
tests/test_decorators.py::HTTPRouteDecoratorTest::test_registers_http_route PASSED
tests/test_http_api.py::TransferAPITest::test_health PASSED
tests/test_storage.py::StorageTest::test_get_by_multiple_origem_id PASSED
tests/test_storage.py::StorageTest::test_get_by_origem_id PASSED
tests/test_storage.py::StorageTest::test_get_by_origem_id_empty_list PASSED

----------- coverage: platform linux, python 3.7.5-final-0 -----------
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
baas/__init__.py                0      0   100%
baas/api.py                    15      2    87%   14, 19
baas/app.py                    24      0   100%
baas/clients/__init__.py        0      0   100%
baas/clients/account.py        26      6    77%   29-34, 38-43
baas/conf.py                    7      0   100%
baas/http/__init__.py          12      0   100%
baas/models.py                 10      0   100%
baas/services/__init__.py       0      0   100%
baas/services/transfer.py      18      1    94%   18
---------------------------------------------------------
TOTAL                         112      9    92%
Coverage XML written to file coverage.xml

=============================================================================== 14 passed, 4 warnings in 0.36s ================================================================================

```
