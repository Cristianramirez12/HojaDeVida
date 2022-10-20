import pygame
import math
WIDTH=1080
HEIGHT=800
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
t=(400,400)

def Polygon(pantalla,posxy,o,color):
	pygame.draw.polygon(pantalla,color,Rot_pointlist(posxy,o))
#rotacion de una lista  
def Rot_pointlist(posxy,o):
	polygon=[]
	for x in posxy:
		polygon.append(Tras(t,Rot(o,x)))
	return polygon
#Ecuacion polar 
def polar(r,a):
    ar=math.radians(a)
    x=r*math.cos(ar)
    y=r* math.sin(ar)
    return [int(x),int(y)]
#Suma dos puntos 
def Suma_punto(p,t):
    ox=p[0]+t[0]
    oy=p[1]+t[1]
    return [ox,oy]
#rotacion de un punto
def Rot(omega,p):
	o=math.radians(omega)
	xp=(math.cos(o)*p[0])-(math.sin(o)*p[1])
	yp=(math.sin(o)*p[0])+(math.cos(o)*p[1])
	pp=[int(round(xp)),int(round(yp))]
	return pp
#escalar una lista
def Esc_lista(e,lis):
        pp=[]
        for p in lis:
                xp=e*p[0]
                yp=e*p[1]
                pp.append([int(xp),int(yp)])
        return pp
#Cambiar de carteciano a pantalla
def Tras(t,p):
	xp=t[0]+p[0]
	yp=t[1]-p[1]
	pp=[xp,yp]
	return pp


def figura(angulo,pantalla,esc):

	o=0

	grado=30+angulo
	grado2=150+angulo
	grado3=-90
#cara 1
	A=[0,0]
	B=polar(100,grado)
	C=Suma_punto(B,[0,120])
	D=Suma_punto(A,[0,40])
	E=polar(60,grado)
	E=Suma_punto(D,E)
	F=Suma_punto(E,[0,80])
	cara_1=[F,E,D,A,B,C]
	cara_1=Esc_lista(esc,cara_1)

#Cara 2
	G=polar(120,grado2)
	G=Suma_punto(G,A)
	H=Suma_punto(G,[0,40])

	cara_2=[A,G,H,D]
	cara_2=Esc_lista(esc,cara_2)
	
	Polygon(pantalla,cara_2,o,ROJO)

#Cara 3
	I=Suma_punto(G,E)
	cara_3=[I,H,D,E]
	cara_3=Esc_lista(esc,cara_3)
	Polygon(pantalla,cara_3,o,VERDE)


#Cara 4
	J=polar(40,grado2)
	J=Suma_punto(F,J)
	K=polar(40,grado)
	K=Suma_punto(J,K)
	
	cara_4=[K,J,F,C]
	cara_4=Esc_lista(esc,cara_4)

#Cara 5
	L=Suma_punto(J,[0,-40])
	
	M=polar(40,grado2)
	M=Suma_punto(L,M)
	N=Suma_punto(M,[0,20])
	Ñ=Suma_punto(I,[0,60])
	
	cara_5=[L,M,N,Ñ,I,E,F,J]
	cara_5=Esc_lista(esc,cara_5)


#Cara 6
	O=polar(40,grado)
	O=Suma_punto(Ñ,O)
	
	P=polar(40,grado)
	P=Suma_punto(P,N)
	
	cara_6=[O,P,N,Ñ]
	cara_6=Esc_lista(esc,cara_6)
	Polygon(pantalla,cara_6,o,VERDE)
#Cara 7
	Q=polar(20,grado3)
	Q=Suma_punto(Q,P)
	
	cara_7=[P,N,M,Q]
	cara_7=Esc_lista(esc,cara_7)
	Polygon(pantalla,cara_7,o,BLANCO)

#Cara 8
	R=polar(40,grado)
	R=Suma_punto(R,L)
	
	cara_8=[M,L,R,Q]
	cara_8=Esc_lista(esc,cara_8)
	
	Polygon(pantalla,cara_8,o,VERDE)
	Polygon(pantalla,cara_4,o,VERDE)
	Polygon(pantalla,cara_5,o,ROJO)
	Polygon(pantalla,cara_1,o,BLANCO)


