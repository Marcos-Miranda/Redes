# importação do módulo socket
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepara o socket do servidor
serverSocket.bind(('', 80))
serverSocket.listen(1)
while True:
    print('O servidor está pronto para receber requisições...')
    # Estabelece a conexão com o cliente
    connectionSocket, addr = serverSocket.accept()
    try:
        mensagem = connectionSocket.recv(1024)
        nome_arquivo = mensagem.split()[1]
        arquivo = open(nome_arquivo[1:])
        saida = arquivo.read()
        arquivo.close()
        # Envia linhas de cabeçalho
        connectionSocket.send(('HTTP/1.1 200 OK\r\n\r\n').encode())
        # Envia o conteúdo do arquivo requisitado ao cliente
        for i in range(0, len(saida)):
            connectionSocket.send(saida[i].encode())
        connectionSocket.close()
    except IOError:
        # Envia resposta de arquivo não encontrado
        connectionSocket.send(('HTTP/1.1 200 OK\r\n\r\n').encode())
        connectionSocket.send(('<h1>404 Not Found</h1>').encode())
        # Encerra a conexão com o cliente
        connectionSocket.close()
serverSocket.close()
