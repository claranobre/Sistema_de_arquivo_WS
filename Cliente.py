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

# Função para conectar ao servidor
def connect(login = '', password = '', ip='127.0.0.1', porta=2121):
	try:
        handler = FTP()
        handler.connect(ip, port)
        handler.login(login, password)
        
    except Exception:
        logging.critical('Não foi possivel conectar ao servidor FTP')

    return handler
def listDirectories(ftp):
    log = []
    ftp.retrlines('LIST', callback=log.append)
    files = (line.rsplit(None, 1)[1] for line in log)
    print 'Arquivos: \n'
    for f in list(files):
        print f

# a função sobe um arquivo no servidor com o nome especificado por 'name'
# localizada no diretório espeficidado por 'path'
def upload(handler, name, path):

    try:
        handler.storbinary('STOR ' + name, open(path, 'rb'))

    except Exception,e:
        print e
        print 'Erro ao subir o arquivo ao servidor'
        return None
    print 'operação efetuada com sucesso :)'
    

# A função move o cliente para o diretório determinado por Dir
def moveToDir(handler, Dir):

    try:
        handler.cwd(Dir)
    except Exception:
        print 'Não foi possivel acessar o diretorio ou o diretorio não existe'


# A função cria um novo diretório com o nome especificado por 'name'
def makeDir(handler, name):

    try:
        handler.mkd(name)
    except Exception:
        print 'Não foi possivel criar o diretorio =( '

# A função deleta um arquivo com o nome especificado por 'name'
def delFile(handler, name):

    try:
        handler.delete(name)
    except Exception:
        print ' não foi possivel deletar o arquivo ou ele é inexistente'
    print 'O arquivo foi deletado'