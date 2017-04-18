# coding: utf-8

from ftplib import FTP
import log
import logging
#log.criarLog()
log.atualizarLog()
# A função abaixa um arquivo definido por 'filename' na pasta definida por local com o nome
# especificado por 'name'
def download(handler, name, filename="musica1.mp3"):
    Dfile = open('PastaExemplo/Downloads/' + name, 'wb')

    try:
        handler.retrbinary('RETR ' + filename, Dfile.write)
    except Exception, e:
      
        print 'Erro ao abaixar o arquivo '
        raise e
    log.atualizarLog('Download feito com sucesso! :)')    
    print 'Download feito com sucesso! :)'
    
    
    Dfile.close()
    

# a função conecta um cliente no servidor
# é chamado assim que a linha de comando é iniciada
def connectClient(login=' ', password=' ', ip='127.0.0.10', port=2121):

    try:
        handler = FTP()
        handler.connect(ip, port)
        handler.login(login, password)
        
    except Exception:
        logging.critical('Não foi possivel conectar ao servidor FTP')

    return handler

# A função lista diretorios da pasta atual

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