import itertools
import copy
import random
from time import time

def checarBoard(m,value):
    for x in range(0,3):
        if m[x][0]== value and m[x][1]== value and m[x][2] == value:
            return 1
    for y in range(0,3):
        if m[0][y]== value and m[1][y]== value and m[2][y] == value:
            return 1
    if m[0][0]== value and m[1][1]== value and m[2][2] == value:
        return 1
    if m[0][2]== value and m[1][1]== value and m[2][0] == value:
        return 1
    return 0

def eva(m):
    if checarBoard(m,'X'):
        return 1
    if checarBoard(m,'O'):
        return -1
    return 0

def printBoard(m):
    p=" |0|1|2|"
    l="--------"
    print(m)
    print(p)
    for i in range(0,3):
        print(l)
        pri= str(i)+"|"
        for c in range(0,3):
            if '0' != m[i][c]:
                pri+= str(m[i][c])+"|"
            else:
                pri+= " "+"|"
        print(pri)

def changeBoard(m,x,y,value):
    if m[x][y]=='0':
        m[x][y]=value
        return 1
    return 0

def validarResp():
    x=-1
    while x < 0 or x>=3:
        print("Donde Deseas tirar en y?")
        x=int(input())
    y=-1
    while y < 0 or y>=3:
        print("Donde Deseas tirar en x?")
        y=int(input())
    return x,y

def turnoHumano(m):
    printBoard(m)
    
    x,y=validarResp()
    valido=changeBoard(m,x,y,'O')
    #print(valido)
    while valido == 0:
        print("Movimiento NO valido Casilla ocupada")
        #print(x)
        #print(y)
        x,y=validarResp()
        valido=changeBoard(m,x,y,'O')
    if checarBoard(m,'O'):    
        print("Conseguiste lo imposible le ganaste al jugador perfecto de TicTacToe!!!!")
        
        
def celdasValidas(m):
    celdas=[]
    for x in range(0,3):
        for y in range(0,3):
            if m[x][y] == '0':
                celdas.append([x, y])
    return celdas

def minimax(m, deep, flag):
    if flag == 1:
        final = [-10,-1,-1]
    else:
        final =[10,-1,-1]
    if deep==0 or abs(eva(m)):
        return [eva(m),-1,-1]
    for move in celdasValidas(m):
        x,y = move

        if flag == 1:
            changeBoard(m,x,y,'X')
        else:
            changeBoard(m,x,y,'O')
        punt=minimax(m,deep-1,-flag)
        m[x][y] = '0'
        punt[1]=x
        punt[2]=y
        if flag==1:
            if punt[0] > int(final[0]):
                final= punt
        else:
            if punt[0]< int(final[0]):
                final= punt            
    return final

def IAturno(m):
    deep=celdasValidas(m)
    if len(deep) == 0:
        return 0
    print(len(deep))
    if len(deep) == 9:
        x = random.choice([0,1,2])
        y = random.choice([0,1,2])
    else:
        holiwis = minimax(m,len(deep),1)
        s,x,y=holiwis
    changeBoard(m,x,y,'X')

        
def funcion(m,prof,path,selec):
    costo=0
    path=[]
    lis ={}
    dos=2
    while len(celdasValidas(m))>0 and (not checarBoard(m,'X') and not checarBoard(m,'X')):

        if selec == '2':
            tiempo_inicial = time()
            IAturno(m)
            selec=0
            tiempo_final = time() 
            tiempo_ejecucion = tiempo_final - tiempo_inicial
            print ("El tiempo de ejecucion fue:",tiempo_ejecucion) #En segundos
        turnoHumano(m)
        c=celdasValidas(m)
        tiempo_inicial = time()
        IAturno(m)
        tiempo_final = time() 
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print ("El tiempo de ejecucion fue:",tiempo_ejecucion) #En segundos
    printBoard(m)
    if checarBoard(m,'X') == 1:
        print("PERDISTE CONTRA EL MEJOR JUGADOR NO HAY DE QUE AVERGONZARSE")
    else:
        if checarBoard(m,'X') == 1:
            print("NO SE POR QUE LO ANOTO SI NUNCA NADIE LO VERA")
        else:
            print("HICISTE LO MEJOR POSIBLE")
    m=[['0','0','0'],['0','0','0'],['0','0','0']]
                
m=[['0','0','0'],['0','0','0'],['0','0','0']]
printBoard(m)
prof=0
Estado=0
path=[]
while 1:
    m=[['0','0','0'],['0','0','0'],['0','0','0']]
    selec = input('Escoje turno?[1/2]: ')
    funcion(m,prof,path,selec)
