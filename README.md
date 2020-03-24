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

Onde `<HOME>` é o seu usuário local. Para descobrir sua home abra um terminal e digite:

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
