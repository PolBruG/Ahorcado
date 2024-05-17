import getpass
import string
def actualitzarParaula(original,migendevinar,c):
    """
    retorna la paraula a mig endevinar actualitzada
    >>> actualitzarParaula('informatica','i-------i--','o')
    'i--o----i--'
    >>> actualitzarParaula('infoaula','infoa--a','u')
    'infoau-a'
    >>> actualitzarParaula('provando','--------','z')
    '--------'
    """
    aux=""
    for i,lletra in enumerate(original):
        if lletra==c:
            aux+=c
        else:
            aux+=migendevinar[i]
    return aux
def chequejaParaula(p):
    """
    Retorna True si p esta composada per lletres alfabetiques
    >>> chequejaParaula('HoLa')
    True
    >>> chequejaParaula('Hola123')
    False
    >>> chequejaParaula('#abc')
    False
    """
    if p=='':
        return False
    for c in p:
        if c not in string.ascii_letters:
            return False
    return True

def demanaParaula():
    """
    Retorna la primera paraula introduida bé
    """
    paraula=getpass.getpass("Player 1 enter word to guess: ")
    while not chequejaParaula(paraula):
        paraula=getpass.getpass("Player 1 bad word, enter word to guess: ")
    return paraula

def chequejaLletra(l):
    """
    retorna True si l es una lletra de l'alfabet
    >>> chequejaLletra('aa')
    False
    >>> chequejaLletra('@')
    False
    >>> chequejaLletra('2')
    False
    >>> chequejaLletra('a')
    True
    >>> chequejaLletra('')
    False
    """
    return len(l)==1 and l in string.ascii_letters

def demanaLletra():
    """
    retorna la primera lletra correcta
    """
    lletra=input("Enter letter player 2: ")
    while not chequejaLletra(lletra):
        lletra=input("Bad letter, Player 2 renter letter: ")
    return lletra

def jugarUnaPartida():
    print("Guess the word")
    paraula=demanaParaula()
    paraula=paraula.upper()
    s="-"*len(paraula)
    print(s)
    N=13
    j=1
    while j<=N and s!=paraula:
        c=demanaLletra()
        c=c.upper()
        s=actualitzarParaula(paraula,s,c)
        print(s)
        j+=1
    if s==paraula:
        print("You win")
    else:
        print("You lose, the word was",paraula)

def opcioCorrecta(o):
    """
    retorna True si es opcio correcta
    """
    return o=="0" or o=="1"

def menuOpcions():
    print("1. Play")
    print("0. Exit")
    x=input("Enter option: ")
    while not opcioCorrecta(x):
        x=input("Bad option, reenter option: ")
    return x

#def recomptePunts():
    
    

if __name__=='__main__':
   opcio=menuOpcions()
   while opcio=="1":
       jugarUnaPartida()
       opcio=menuOpcions()
   print("Game over")
        
