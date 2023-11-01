"""Estrutura de dados:
Uma lista pois pode ser ordenada, assim o acesso ao contacto é mais rapido. O mesmo acontese na procura de um nome, ao procurar num dicionaria a complexidade iria ser mais elevada.


funcoes/complixidade:

adicionar/ O(1) pois adiciono ao final da lista;
remover/ O(log n) se a lista telefonaca estiver ordenada (pesquisa binaria) mas se não estiver O(n);
pesquisar/ o mesmo de remover;
editar/O(1) pois nao depende do tamanho da lista;
lista de contactos/ O(N)
"""