#Função que verifica se uma das opções existentes foi escolhida
def aprova(c,t):
    if c in t:
        return False
    else:
        return True
    
#Função que verifica se algum número foi escrito
def condicao(x):
    for a in range(len(x)):
        if x[a].isnumeric() == True:
            print("---------------------------\nNÃO PODE TER NÚMEROS!")
            return True
        
#Função que verifica se o que foi escrito está em alguma lista
def especial(k,t):
    for a in range (len(k)):
        if k[a] in t:
            return False
        else:
            print("NÃO PODE TER CARACTERES ESPECIAIS OU ESPAÇO!\n---------------------------")
            return True

#Função que transforma texto em número baseando-se em uma lista
def textoNumero(x,t,a):
    for i in range (len(x)):
        if x[i] in t:
            a.append(t.index(x[i]))
        else:
            a.append(x[i])

#Função que faz a soma dois valores e pega o resto de 26
def soma(l,m,k,c):
    iChave = 0
    for i in range (len(l)):
        if l[i] in range (0, 26):
            l[i] = (l[i] + k[iChave]) % 26
            iChave = iChave + 1 
        else:
            l[i] = (m[i])     
        if iChave == len(c):
            iChave = 0

#Função que transforma número em texto baseando-se em uma lista
def numeroTexto(m,t):
    for i in range(len(m)):
        if m[i] in range (0 , 26):
            m[i] = t[m[i]]
        else:
            m[i] = m[i]

#Função que faz a subtração de dois valores, soma 26 e pega o resto de 26
def subtracao(m,c):
    iChave = 0
    for i in range (len(m)):
        if m[i] in range(0, 26):
            m[i] = (m[i] - c[iChave] + 26) % 26
            iChave = iChave + 1 
        else:
            m[i] = mensagem[i]
        if iChave == len(c):
            iChave = 0
  
#Definindo uma constante
TABELA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#Definindo listas usadas para criptografar e descriptografar
auxChave = []
auxMensagem = []
aprovar = ["c","d"]

#Definindo variáveis que precisam ser iniciadas antes do processo de criptografar e descriptografar
cript = " "
mensagem = "0"
chave = "0"

#Perguntando se deseja criptografar ou descriptografar
while aprova(cript,aprovar):
    print("+-------------------------------+\n|[c]Criptografar uma mensagem   |")
    print("|[d]Descriptografar uma mensagem|\n+-------------------------------+\n\n")
    cript = input("O que deseja fazer? ")
    cript = cript.lower()

if cript == "c":

    #Pedindo a mensagem a ser criptografada

    while condicao(mensagem):
        mensagem = input("Escreva uma mensagem para ser criptografada: ")
        mensagem = mensagem.lower()
    #Pedindo a chave para criptografar a mensagem
    while condicao(chave) and especial(chave, TABELA):
        chave = input("Escreva uma chave para criptografar a mensagem: ")
        chave = chave.lower()
    
    #Alterando a chave seguindo a TABELA, trocamos as letras por números
    #Exemplo: se a chave é "teste" após a transformação fica: "19 4 18 19 4"

    textoNumero(chave, TABELA, auxChave)
    
    #Alterando a mensagem seguindo a tablea, trocamdos as letras por números 
    #Exemplo: se mensagem fpr "bom dia" após a transformação fica "1 14 12 ' ' 3 8 0"

    textoNumero(mensagem, TABELA, auxMensagem)

    #A conta consiste em somar o valor da chave com o respectivo valor da mensagem e pegar o resto de 26
    #Exemplo: (19 + 1) % 26 = 20 // (14 + 4) %26 = 18  // (18 + 12) %26 = 4 // " " = " " /
    #/ (19 + 3) %26 = 22 // (4 + 8) %26 = 12 // (19 + 0) %26 = 19

    soma(auxMensagem, mensagem, auxChave, chave)

    #Alterando os números por letras. Vamos até a TABELA e pegamos uma letra por seu índice
    #Exemplo se for "20 18 4 ' ' 22 12 19", após a mudança fica: "USE WMT"

    numeroTexto(auxMensagem, TABELA)

    #Transformando uma lista em texto

    mensagem = "".join(auxMensagem)

    #Exibindo o resultado final

    print("A mensagem criptografada: ", mensagem)

elif cript == "d":
    #Pedindo a mensagem a ser descriptografada

    while condicao(mensagem):
        mensagem = input("Escreva uma mensagem para ser descriptografada: ")
        mensagem = mensagem.lower()
    #Pedindo a chave para descriptografar
    while condicao(chave):
        chave = input("Escreva uma chave para descriptografar a mensagem: ")
        chave = chave.lower()
 
    #Alterando a chave seguindo a TABELA, trocamos as letras por números 
    #Exemplo: se a chave é "teste" após a transformação fica "19 4 18 19 4"

    textoNumero(chave, TABELA, auxChave)

    #Alterando a mensagem criptografada, trocamdos as letras por números 
    #Exemplo: se a mensagem for "bom dia" após a transformação fica  "20 18 4 ' ' 22 12 19"

    textoNumero(mensagem, TABELA, auxMensagem)

    #A conta consiste em subtrair o valor da chave do respectivo valor da mensagem criptografada,
    #somar 26 e pegar o resto de 26
    #Exemplo: (20 - 19 + 26) % 16 = 1 // (18 - 4 + 26) %26 = 14  // (4 - 18 + 26) %26 = 12 // " " = " " /
    #/ (22 - 19 + 26) %26 = 3 // (12 - 4 + 26) %26 = 8 // (19 - 19 + 26) %26 = 0
    
    subtracao(auxMensagem, auxChave)

    #Alterando os números por letras. Vamos até a TABELA e pegamos a letra por seu índice
    #Exemplo se for "1 14 12 " " 3 8 0", após a mudança fica: "BOM DIA"

    numeroTexto(auxMensagem, TABELA)

    #Transformando uma lista em texto

    mensagem = "".join(auxMensagem)

    #Exibindo o resultado final

    print("A mensagem descriptografada: ", mensagem)