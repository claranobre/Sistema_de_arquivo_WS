#!/usr/bin/env python
# -*- coding: utf-8

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
#from pyftpdlib.servers import FTPServer
#from SOAPpy import SOAPServer
from suds.servers import Servidor
import sys

def config():
    #Objeto responsável pela autenticação dos usuarios e permissões
    authorizer = DummyAuthorizer()

    #Local de acesso padrão
    path = "/home/clara/Documents/"
    print "Local de acesso ao servidor FTP: \n"
    
    #Usuario padrão com permissão total de escrita/leitura
    authorizer.add_user('clara', '42', path, perm='elradfmwM')

    #Usuario anônimo
    authorizer.add_anonymous(path, perm="el")

    #Instantiate FTP handler class
    #Objeto que manipula os comandos enviados pelo cliente FTP
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

def main(arg):
    
    handler = config()
    address = ('', 2121)
    server = SOAPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


if __name__ == '__main__':
    main(sys.argv)