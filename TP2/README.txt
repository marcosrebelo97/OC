Trabalho Prático 2 de Organização de Computadores
Aluno: Marcos Guerreiro Rebelo

1) O que foi criado: 

Um pseudo-compilador utilizando Python para ler arquivo de texto com código assembly,
com a finalidade de traduzir cada instrução do arquivo lido em: binário e hexadecimal.
Com isso, são gerados os dois arquivos:
    - binario.txt
    - hexadecimal.txt

2) Decisões tomadas: 

As instruções a seguir são separadas por espaço, com isso não pode mais adicionar outro espaço pois corre o risco de gerar erros no resultado. 
Sendo assim, a cada nova instrução utilizada deve estar em linha diferente. Devem seguir esse padrão.

- (instrução)        RA RB
- (instrução)        Addr
- (instrução)        RB

3) Funções escritas no pseudo-compilador: 

- dir_1()
- read_Arquivo()
- dir_2()  
- dir_3()
- gerar_Txt()
- convert_hexa()
- gerar_Txt_hexa()

Observação: comentadas no código

4) Exemplos de testes utilizados para verificar:

Foram utilizados os arquivos testes compartilhados no material (slide) disponibilizado. 
No zip enviado contém uma pasta (assembly) com os arquivos teste usados.

5) Passo a passo de como executar:

Observação: não funciona na versão 2.7 do python 

- 1º passo: abra o arquivo .py e altere o diretório (comentado no código) 
- 2º passo: para executar digite: py teste.py


