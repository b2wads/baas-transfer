# Banco as a Service

O objetivo desse projeto é ensinar um pouco sobre testes. Esse projeto é usado na aula de testes do programa de estágio da B2W Digital.

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

## Instalando python

Depois que o pyenvf estiver funcionando é hora de instalar uma versão do python. Para esse projeto podemos
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

A partir desse momento você já pode rodar `pipenv` no terminal.

# Instalando o projeto

Entre na pasta do projeto e digite:

```
pipenv install --dev
```

# Rodando os testes

Para rodas os teses, faça:

```
pipenv run test
```

Todos os testes devem passar.



# Implementação

Temos 4 endpoints para serem implementados nesse projeto:

- `POST /saque/<acc_id>`
- `GET /saques/<acc_id>`

Todos os endpoints seguem a mesma estrutura: A função que recebe o request HTTP chama um "Service". Esse service por sua vez chama um storage interno para salvar e pegar os dados. Os testes estão na pasta `tests/`.


Os edpoints HTTP já estão implementados e chamando os Services corretos. O que precisa sser feito é preencher o método `SaqueService.save_saque()`. Esse método deve efeutar um saque usando o serviço de account para isso.
