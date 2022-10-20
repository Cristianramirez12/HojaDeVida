import math
import pygame
def colocar_puntos(vent,ls):
        pygame.draw.circle(vent,[255,255,0],ls,2,)
        pygame.display.flip()
        
def escala(p):
    xp=p[0]*10
    yp=p[1]*10
    print(xp)
    return[int(xp),int(yp)]

def llenar_ecuacion (n, Nx,Ny,Nr):
    while n > 0:
        a = int(input("ingrese el numero que multiplica x"))
        b = int(input("ingrese el numero que multiplica y"))
        c = int(input("ingrese el numero igualado"))
        Nx.append(a)
        Ny.append(b)
        Nr.append(c)
        n-=1
    
    return Nx,Ny,Nr
def recta(ventana, datos, a, b):
    while(b<len(datos)):
        pygame.draw.line(ventana,[250,250,250],datos[a],datos[b],1)
        a+=2
        b+=2
        pygame.display.flip()
    
        
def punto_rec(origen,tras):
    origenx=origen[0]
    origeny=origen[1]
    trasx=tras[0]
    trasy=tras[1]
    A=[trasx+origenx,(-trasy+origeny)]
    return A

def multiplicar(Nx,Ny,Nr,punt,n,a):
        cont=0
        while(n>a):
                suma=Nx[a]*(punt[0]/10)+(Ny[a]/10)*punt[1]
                if(suma==Nr[a]):
                        cont+=1
                elif(suma<Nr[a]):
                        cont+=2
                elif(suma>Nr[a]):
                        cont+=3
                a+=1
        return cont

    
def punto(n,Nx,Ny,Nr):
    a=0
    Puntos=[]
    while(a<n):
        Puntos.append([0,int(Nr[a]/Ny[a])])
        Puntos.append([int(Nr[a]/Nx[a]),0])
        a+=1
    return Puntos

def Plano(v,p):
    y= p[1]
    x= p[0]
    pygame.draw.line(v,[250,0,0],[0,y],[700,y],2)
    pygame.draw.line(v,[250,0,0],[x,0],[x,500],2)
    
def carteciano(origen,punto):
    B=[(punto[0]-origen[0]),(origen[1]-punto[1])]
    return B

def menu(n) :
    a=0
    print("Metodo grafico")
    x = int(input("ingrese el numero que multiplica x en la ecuacion optima"))
    y = int(input("ingrese el numero que multiplica y en la ecuacion optima"))

    n= int (input("ingrese el numero de ecuaciones"))
    Nx=[]
    Ny=[]
    Nr=[]
    Nx,Ny,Nr=llenar_ecuacion(n,Nx,Ny,Nr)
    Puntos=punto(n,Nx,Ny,Nr)
    Ancho=700
    Alto=500
    ventana = pygame.display.set_mode([Ancho,Alto])
    
    origen=[350,250]
    Plano(ventana,origen)
    pun_car=[]
    for a in Puntos:
        pun_car.append(escala(a))
    Puntos=[]
    for a in  pun_car:
        Puntos.append(punto_rec(origen,a))
        
    recta(ventana,Puntos,0,1)
    s=0
    cont=0
    pun=[]
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if(event.button==1):
                    pun=carteciano(origen , event.pos)
                    s=multiplicar(Nx,Ny,Nr,pun,n,0)
                    pun_car=punto_rec(origen,pun)
                    colocar_puntos(ventana, pun_car)
                    s=multiplicar(Nx,Ny,Nr,pun,n,0)
                    if( s > n*2 ):
                        print()
                        print("No es solucion ")
                    elif( s > n and s <= n*2):
                        print()
                        print("Es solucion factible es con x= ",pun[0]/10,"y en Y=",pun[1]/10,)
                        print("Con una maximizacion de ",(((pun[0]/10)*x)+(y*(pun[1]/10))))
                       
                    
                    elif(s==n):
                        print("La solucion optima es con x= ",pun[0]/10,"y en Y=",pun[1]/10,)
                        print("Con una maximizacion de ",(((pun[0]/10)*x)+(y*(pun[1]/10))))
                        fin=True
                        
                    
                        

        pygame.display.flip()
     

    


menu(0)
