# This is a sample Python script.
def water_blue():
    pygame.draw.rect(window,BLUE, (x,y, width, hight))
    pygame.display.update()
def wight ():
    pygame.draw.rect(window, WIGHT, (x, y, width, hight))
    pygame.display.update()
def green ():
    pygame.draw.rect(window, GREEN, (x, y, width, hight))
    pygame.display.update()
import pygame
pygame.init()
window=pygame.display.set_mode((720,700))
x=0
y=0
count=0
width=100
hight=100
BLUE=(0,102,153)
WIGHT=(255,255,255)
GREEN=(0,230,0)
row,col=(7,7)
list=("")

while True:
 for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        exit()
 for i in range (0,col):
     for j in range(0,row):
         if i in range (1,6) and j in range (1,6):
             wight()
             y += 102
             continue
         if i == 6 and j == 3:
             green()
             y += 102
             continue
         water_blue()
         y+= 102

     x+=103
     y=0






