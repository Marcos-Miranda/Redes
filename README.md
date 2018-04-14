# Avaliação1 da disciplina Redes de Computadores - Engenharia de Computação 2018-1

Servidor Web simples que processa apenas uma requisição. Cria um socket de conexão quando contatado por um cliente, recebe uma requisição HTTP e analisa a requisição para determinar o arquivo requisitado do sistema do sevidor. Caso o arquivo esteja presente, ele envia uma mensagem de resposta HTTP, consistindo de linhas de cabeçalho e do arquivo, caso não esteja, ele envia uma mensagem de erro "404 Not Found".
