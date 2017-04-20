# Sistema de Arquivos com Web Service

Projeto de implementação Web Service da disciplina de Programação Distribuída 2017.1

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

[suds] [http://ricardoduarte.net/posts/como-acessar-webservices-soap-com-python.html]


# Como executar 

** Servidor
python Servidor.py

** Cliente 
python Cliente.py