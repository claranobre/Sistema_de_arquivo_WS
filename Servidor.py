#!/usr/bin/env python

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
#from pyftpdlib.servers import SOAPServer

import sys

def config():
    # Objeto responsável pela autenticação dos usuarios e permissões
    authorizer = DummyAuthorizer()

    # Local de acesso padrão
    path = "/home/clara/Documents/UFRN/Programação\ Distribuida/Sistema_de_arquivo_WS/"
    print "Local de acesso ao servidor FTP: \n"
    
    # Usuario padrão com permissão total de escrita/leitura
    authorizer.add_user('clara', '42', path, perm='elradfmwM')

    # Usuario anônimo
    authorizer.add_anonymous(path, perm="el")

    # Instantiate FTP handler class
    # Objeto que manipula os comandos enviados pelo cliente FTP
    handler = FTPHandler
    handler.authorizer = authorizer


    '''    permissoes que um usuario pode ter 
     |      Read permissions:
     |       - "e" = change directory (CWD command)
     |       - "l" = list files (LIST, NLST, STAT, MLSD, MLST, SIZE, MDTM commands)
     |       - "r" = retrieve file from the server (RETR command)
     |      
     |      Write permissions:
     |       - "a" = append data to an existing file (APPE command)
     |       - "d" = delete file or directory (DELE, RMD commands)
     |       - "f" = rename file or directory (RNFR, RNTO commands)
     |       - "m" = create directory (MKD command)
     |       - "w" = store a file to the server (STOR, STOU commands)
     |       - "M" = change file mode (SITE CHMOD command)
      '''

    return handler
    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    # handler.masquerade_address = '151.25.42.11'
    # handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121 =

def main(arg):
    
    handler = config()
    address = ('', 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


if __name__ == '__main__':
    main(sys.argv)