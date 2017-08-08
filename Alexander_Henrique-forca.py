import random # Está importando a biblioteca random, o random gera números aleatórios

palavras = [] # "palavras" é uma lista vazia


while True:
    p = input('Digite as palavras que deseja usar no jogo:') # p é uma variável que pergunta as palavras desajadas para uso no jogo.

    if p == "": # se p for igual a nada:
        break # o comando vai parar de perguntar as palavras
    
    palavras.append(p) # vai adicionar as palavras digitadas na lista "p"
# o bloco abaixo fala que as variaveis sao iguais a nada
letrasErradas = ''
letrasCertas = ''
# no bloco abaixo estão os desenhos que irão aparecer de acordo com as letras que o jogador errar. 
FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',]

def principal(): # esta chamando a função "principal"
    """
    Função Princial do programa 
    """
    # A cima é só um comentario que irá aparecer na tela para complementar o jogo.
    print('F O R C A') # Vai printar (colar) na tela o item 'F O R C A'
    
    palavraSecreta = sortearPalavra() # Vai a palavra secreta vai ser definida pela função 'sortearPalavra'
    palpite = '' # onde o Jogador coloca seu palpite de letra 
    desenhaJogo(palavraSecreta,palpite)# de acordo com o palpite vai desenhar um dos desenhos mostrados a cima

    while True: # Vai repetir o bloco de instrução abaixo enquanto a condição definidad em seu cabeçalho for verdadeira 
        palpite = receberPalpite() # vai receber o palpite dado a cima 
        desenhaJogo(palavraSecreta,palpite) # Vai desenvolver a parte gráfica do programa, onde vai desenhar o boneco da forca de acordo com a palavra secreta e o palpite.
        if perdeuJogo(): # Está declarando uma condição
            print('Voce Perdeu!!!') # Vai printar(colar) 'Você Perdeu!!!' na tela 
            break # Quebra o loop quando chegar nele
        if ganhouJogo(palavraSecreta): 
            print('Voce Ganhou!!!') # Vai printar(colar) 'Você Ganhou!!!' na tela
            break              
        
def perdeuJogo():# está definindo uma função
    global FORCAIMG # Essa é uma variável que está sendo definida fora da função 
    if len(letrasErradas) == len(FORCAIMG): # Está lendo a quantidade de caracteres dentro de (letrasErradas) que é igual a quantidade de caracteres dentro de (FORCAIMG)
        return True # Designa o valor a ser retornado enquanto for verdade 
    else: # defini o bloco de instrução a ser executado todas as vezes que a expressão definida for igual a falso.
        return False # Designa o valor a ser retornado nquanto for falso
    
def ganhouJogo(palavraSecreta):# está definindo uma função
    global letrasCertas # Está definindo 'letrasCertas' fora da função.
    ganhou = True # o jogador ganhou.
    for letra in palavraSecreta: # Para cada letra em 'palavraSecreta'.
        if letra not in letrasCertas: # Se a letra não estiver em 'letrasCertas'.
            ganhou = False # o jogador nao ganhou
    return ganhou # Designa o valor a ser retornado       
        


def receberPalpite():# está definindo uma função
    
    palpite = input("Adivinhe uma letra: ") # palpite está recebendo os dados ou valores que o usuário fornece através do teclado.
    palpite = palpite.upper() # Está dizendo que todas as letras que estiverem dentro de palpite ficarão em maiúsculo.
    if len(palpite) != 1: # A quantidade de caracteres está dentro de (palpite) é diferente de 1.
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas: # Está atribuindo uma condição para else em letrasCertas ou em palpite e em letrasErradas.
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": # se o palpite digitado não estiver entre as letras "A" e "Z".
        print('Por favor escolha apenas letras')
    else:
        return palpite # Vai retornar o palpite novamente
    
    
def desenhaJogo(palavraSecreta,palpite):# está definindo uma função 
    global letrasCertas # Essa é uma variável que está sendo definida fora da função
    global letrasErradas 
    global FORCAIMG
    # No bloco a cima está disendo que a variavel "global" está sendo definida comandos fora da função
    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-' # a variavel "vazio" recebe a quantidade de caracteres dentro de "palavraSecreta"
    
    if palpite in palavraSecreta: # se palpite estiver em palavraSecreta :
        letrasCertas += palpite #letrasCertas é igual, e soma com palpite 
    else:
        letrasErradas += palpite # letrasErradas é igual e soma com palpite.

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]: # se letra for igual a palavraSecreta:
                vazio = vazio[:x] + letra + vazio[x+1:]# a letra vai substituir os caracteres que estão dentro da variavel "vazio" de acordo como ele acertar as letras  
                
    print('Acertos: ',letrasCertas )# vai printar(colar) na tela as letras certas que irão está dentro da variavel"letrasCertas"
    print('Erros: ',letrasErradas)# vai printar(colar) na tela as letras erradas que irão está dentro da variavel "letrasErradas".
    print(vazio)
     

def sortearPalavra():# definindo uma função 
    global palavras
    return random.choice(palavras).upper()# está retornando a biblioteca random.choice

    
principal()# "principal" não possui nada dentro 
