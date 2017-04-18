# coding: utf-8

from ftplib import FTP 

# Função para fazer download de um arquivo

def download(handler, name, filename=""):
	Dfile = open('/tmp/' + name, 'wb')

	try:
		handler.retrbinary('Arquivo ' + filename, Dfile.write)
	except Exception, e:
	
		print 'Erro ao baixar o arquivo'
		raise e
	print 'Download feito com sucesso'	

	Dfile.close()