import pygame
import numpy as np
from pygame import *

pygame.init()

screen = pygame.display.set_mode((800, 450))
game = np.zeros((45, 80))
print(game)
lines = (170, 170, 170)
BG = (100, 100, 100)
alive = (255, 255, 255)
nextAlive = (200, 200, 200)
screen.fill(BG)

def drawHor():
    startP = 10
    for x in range(45):
        pygame.draw.line(screen, lines, (0, startP), (800, startP))
        pygame.display.flip()
        startP += 10        
def drawVer():
    startP = 10
    for x in range(80):
        pygame.draw.line(screen, lines, (startP, 0), (startP, 450))
        pygame.display.flip()
        startP += 10
def update():
    nextAlive = []
    nextDie = []
    for y in range(0,45):
        for x in range(0, 80):
            cell = game[y][x]
            if y == 44:
                rowA = game[y-1][x-1:x+2]
                rowB = game[y][x-1:x+2]
                totalC = sum(rowA)+sum(rowB) - game[y][x]                     
            elif y == 0:
                rowB = game[y][x-1:x+2]
                rowC = game[y+1][x-1:x+2]                    
                totalC = sum(rowB)+sum(rowC) - game[y][x]
            else:
                rowA = game[y-1][x-1:x+2]
                rowB = game[y][x-1:x+2]
                rowC = game[y+1][x-1:x+2]
                totalC = sum(rowA)+sum(rowB)+sum(rowC) - game[y][x]             
            if cell == 1.0 and (totalC < 2.0):
                nextDie.append((y, x))
            elif cell == 1.0 and (totalC >= 2.0 and totalC <= 3.0):
                nextAlive.append(tuple([y, x]))
            elif cell == 0.0 and totalC == 3.0:
                nextAlive.append(tuple([y, x]))
            elif cell == 1.0 and totalC > 3.0:
                nextDie.append(tuple([y, x]))
    for x in range(len(nextAlive)):
        newCell = nextAlive[x]
        newY = newCell[0]
        newX = newCell[1]
        game[newY, newX] = 1
        pygame.draw.rect(screen, alive, pygame.Rect(newX*10, newY*10, 9.5, 9.5))        
    for y in range(len(nextDie)):
        newCell = nextDie[y]

        newY = newCell[0]
        newX = newCell[1]

        game[newY, newX] = 0
        pygame.draw.rect(screen, BG, pygame.Rect(newX*10, newY*10, 9.5, 9.5))
    drawVer()
    drawHor()

def main():
    
    running = True
    
    drawHor()
    drawVer()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False
            elif pygame.mouse.get_pressed() == (1, 0, 0):
                mouseX = pygame.mouse.get_pos()[0] // 10
                mouseY = pygame.mouse.get_pos()[1] // 10
                game[mouseY, mouseX] = 1
                pygame.draw.rect(screen, alive, pygame.Rect(mouseX*10, mouseY*10, 9.5, 9.5))
                pygame.display.flip()

    
            elif  pygame.mouse.get_pressed() == (0, 0, 1):
                mouseX = pygame.mouse.get_pos()[0] // 10
                mouseY = pygame.mouse.get_pos()[1] // 10
                game[mouseY, mouseX] = 0
                pygame.draw.rect(screen, BG, pygame.Rect(mouseX*10, mouseY*10, 9.5, 9.5))
                pygame.display.flip()

            elif  pygame.mouse.get_pressed() == (0, 1, 0):
                print()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                                    
                    update()
            drawHor()
            drawVer()
                    
main()