#encoding: utf-8

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import sys

# importante: a biblioteca pyftpdlib não é padrão do python, precisa ser instalada
#  link: https://code.google.com/p/pyftpdlib/downloads/list

def config():
	# Objeto responsavel pela autenticação dos usuarios
	# e suas respectivas permissoes
	authorizer = DummyAuthorizer()
	path = "/home/iury/Documents/projetos/pyftp/PastaExemplo/"
	print "Local de acesso do servidor : \n  " + path + '\n'
	# usuário de exemplo                                                    
	authorizer.add_user("iury","42",path,perm="elradfmwM")
	#usuário anonimo
	authorizer.add_anonymous(path, perm="el")

	# objeto que manipula os comandos enviados pelo cliente FTP
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
	porta = 2121 # porta padrão do servidor
	if len(arg) == 1:
		ip = "127.0.0.10" # ip padrão do servidor
	 	
	else:
		ip = arg[1]
	

	 
	# servidor
	server = FTPServer((ip,porta),handler)
	#inicia o servidor
	server.serve_forever()

if __name__ == '__main__':
	main(sys.argv)
