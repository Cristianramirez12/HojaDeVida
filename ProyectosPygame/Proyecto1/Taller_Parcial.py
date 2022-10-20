import pygame
from libreria import *

if __name__ == "__main__":
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))

	o=0
	vo=0
	a=0
	Ta_es=1
	a=3
	
	fin=False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin=True		
			
			if a>=3:
				if event.type == pygame.KEYDOWN:
                                        #Flecha hacia la izquierda gira 30° en sentido horario
					if event.key == pygame.K_LEFT:
						vo=30
						o+=vo
					#Flecha hacia la izquierda gira 30° en sentido horario
					if event.key == pygame.K_RIGHT:
						vo=-30
						o+=vo
					#Flecha hacia abajo para escalar la figura
					if event.key == pygame.K_DOWN:

						Ta_es=Ta_es*0.5
					#Flecha hacia arriba para agrandar la figura 
					if event.key == pygame.K_UP:
						Ta_es=Ta_es*1.5
						
				
                
		#Imprime la figura con una rotacion guardada en  o  
		if a==3:
			figura(o,pantalla,Ta_es)

		pygame.display.flip()
		pantalla.fill(NEGRO)


