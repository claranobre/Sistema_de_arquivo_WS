# Sistema de Arquivos com Web Service

Projeto de implementação Web Service da disciplina de Programação Distribuída 2017.1

# Objetivo
Dar continuidade ao projeto de RMI de desenvolvimento de um sistema de arquivos distribuídos só que agora usando o protocolo SOAP para trabalhar com Webservice.

# Linguagem utilizada
Foi utilizado a linguagem de programação Python, por curiosidade em utilizar a biblioteca [suds](http://ricardoduarte.net/posts/como-acessar-webservices-soap-com-python.html)

# Protocolo SOAP

O protocolo SOAP tem diversas vantagens sobre outras maneiras de chamar funções remotamente como DCOM, CORBA ou diretamente no TCP/IP:

- É simples de implementar, testar e usar.

- É um padrão da indústria, criado por um consórcio , adotado pela W3C (http://www.w3.org/TR/SOAP/) e por várias outras empresas.
- Usa os mesmos padrões da Web para quase tudo: a comunicação é feita via HTTP com pacotes virtualmente idênticos; os protocolos de autenticação e encriptação são os mesmos; a manutenção de estado é feita da mesma forma; é normalmente implementado pelo próprio servidor Web.
- Atravessa firewalls e roteadores, que pensam que é uma comunicação HTTP.
- Tanto os dados como as funções são descritas em XML, o que torna o protocolo não apenas fácil de usar como também muito robusto.
- É independente do sistema operacional e CPU.
- Pode ser usado tanto de forma anônima como com autenticação (nome/senha). 


# Instalando o FTP

sudo pip install pyftpdlib

# Instalando a biblioteca do protocolo SOAP para trabalharmos com o Webservice

[Download Suds](https://pypi.python.org/pypi/suds)

```
python setup.py build

sudo python setup.py install
```

# Desenvolvimento

- Servidor
O servidor visa a autenticação do usuário, fazendo sua verificação de acesso e setando suas permissões e tem sua configuração da comunicação dependente de um objeto chamado ```handler``` que irá manipular os comandos emitidos pelo usuário. Assim como as configurações padrões de IP, porta, tempo de conexão, início do serviço.

```
def main(arg):
    
    handler = config()
    address = ('', 2121)
    server = SOAPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()
```

- Cliente
O cliente possui todos os comandos das ações que um usuário pode ter dentro do servidor, começando com o seu acesso (autenticação), e após estar conectado ao servidor ele poderá fazer download de um arquivo, acessar diretórios, salvar/remover arquivo em diretório específico, listar diretórios.


# Execução do Projeto

- Servidor
```
python Servidor.py
```

- Cliente 
```
python Cliente.py
```