# -*- coding: utf-8 -*-
import pygame
import random
import math

class Balle:
    def __init__(self,):
        self.posX = 350
        self.posY = 350
        self.vitesse = 2
        self.taille = 20
        self.angle = random.randint(0,360)
        
        self.a_posX = self.posX
        self.a_posY = self.posY
    
    def afficher(self)-> None:
        pygame.draw.circle(screen,(color),(self.posX,self.posY),self.taille)
        
    def addAngle(self, add)-> None:
        self.angle = (self.angle + add) % 360
        
    def supAngle(self, sup)-> None:
        sup %= 360
        if self.angle - sup < 0:
            self.angle = self.angle - sup + 360
        else:
            self.angle -= sup
    
    def getPosX(self)-> int:
        return self.posX
    
    def getPosY(self)-> int:
        return self.posY
    
    def setPosX(self,x)-> None:
        self.posX = x
    
    def setPosY(self,y)-> None:
        self.posY = y
    
                
    def setVitesse(self, v)-> None:
        if v >= 0:
            self.vitesse = v
    
    def resetBalle(self)-> None:
        self.setPosX(350)
        self.setPosY(350)
        
        self.a_posX = self.posX
        self.a_posY = self.posY
        
        self.angle = random.randint(0,360)
        
        self.vitesse = 2
        
    def lancerBalle(self)-> None:
        
        self.a_posX += math.sin(self.angle * math.pi/180)*self.vitesse
        self.a_posY -= math.cos(self.angle * math.pi/180)*self.vitesse
        
        self.posX = round(self.a_posX)
        self.posY = round(self.a_posY)
        
    def rebond(self)-> None:
        if balle.posX + balle.taille >= 689: # touche la droite
            if self.angle <= 180 and self.angle >= 90:
                self.addAngle((180 - self.angle)*2)
                
            if self.angle >= 0 and self.angle <= 90:
                self.supAngle((self.angle -360)*2)
               
            
        if balle.posX - balle.taille <= 12: # touche la gauche
            if self.angle <= 270 and self.angle >= 180:
                self.supAngle((self.angle - 180)*2)
                
            if self.angle <= 360 and self.angle >= 270:
                self.addAngle((360 - self.angle)*2)
                
            
        if balle.posY + balle.taille >= 689: # touche le bas
            if self.angle <= 180 and self.angle >= 90:
                self.supAngle((self.angle - 90)*2)
                
            if self.angle <= 270 and self.angle >= 180:
                self.addAngle((270 - self.angle)*2)
                
            
        if balle.posY - balle.taille <= 12: # touche le haut
            if self.angle <= 90 and self.angle >= 0:
                self.addAngle((90 - self.angle)*2)
                
            if self.angle <= 360 and self.angle >= 270:
                self.supAngle((self.angle - 270)*2)
                

        
def contoure() -> None:
    pygame.draw.line(screen, (32, 192, 0), (10, 10),(10, 690), 2)
    pygame.draw.line(screen, (32, 192, 0), (10,10),(690, 10), 2)
    pygame.draw.line(screen, (32, 192, 0), (690,690),(690, 10), 2)
    pygame.draw.line(screen, (32, 192, 0), (690,690),(10, 690), 2)
    
def add_txt(surface, txt: str, size: int, color: tuple, coord: tuple) -> None:
    texte = pygame.font.SysFont("Afterglow.ttf", size).render(txt, 1, color)
    surface.blit(texte, coord)

balle = Balle()

pygame.init()
play = True
clock = pygame.time.Clock()
format_screen = (700, 700)
screen = pygame.display.set_mode(format_screen)
kl_press, kr_press, kd_press, ku_press, go = False, False, False, False, False
rebond = False
FPS = 240
nb_rebond = 0
color = (0,0,0)

while play:
   
    pygame.display.update()
    clock.tick(FPS)
    screen.fill((0,0,0))
    contoure()
    balle.afficher()
    
    if color[0] == 0:
        action = True
    elif color[0] == 254:
        action = False
    if action:
        color = ((color[0] + 2) % 255, 0, (color[2] - 2) % 255)
    else:
        color = ((color[0] - 2) % 255, 0, (color[2] + 2) % 255)
    
    add_txt(screen, ("Nombre rebond : {}").format(nb_rebond),20,(255, 255, 255),(557,670))
    
    if go == False:
        add_txt(screen, "Appuie sur ENTREE pour lancer la balle",40,(255, 0, 0),(80,250))
    
    if go == True:
        if balle.posX + balle.taille < 689 and balle.posX - balle.taille > 12 and balle.posY - balle.taille > 12 and balle.posY + balle.taille < 689 or rebond == True:
            balle.lancerBalle()
            rebond = False
        else:
            balle.rebond()
            rebond = True
            nb_rebond += 1
            if FPS > 0:
                FPS -= 10           
            
    if FPS == 0:
        balle.setVitesse(0)
        add_txt(screen, "La balle n'a plus de vitesse",40,(255, 0, 0),(170,320))
        add_txt(screen, "appuie sur la barre espace",40,(255, 0, 0),(170,350))
        
    if FPS > 0:
        balle.setVitesse(2)
  
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            
            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_r:
                    balle.resetBalle()
                    go = False
                    nb_rebond = 0
                    FPS = 240
                    balle.setVitesse(2)
                    
                if event.key == pygame.K_RETURN:
                    balle.lancerBalle()
                    go = True
                    
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    run = False
                    
                if event.key == pygame.K_SPACE:
                    FPS += 100
                   