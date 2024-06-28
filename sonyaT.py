import pygame
import os

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((450, 700))

geroi = pygame.Rect(55,55,40,40)
flower_yellow = pygame.Rect(350,600,45,45)
flower_green = pygame.Rect(350,50,45,45)
flower_blue = pygame.Rect(250,250,45,45)
finish = pygame.Rect(150,250,45,45)
flower_bad = pygame.Rect(150,50,45,45)
flower_bad2 = pygame.Rect(250,450,45,45)
pp_wall = pygame.Rect(100,150,50,50)

go_right = False
go_left = False
go_down = False
go_up = False

dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")

wall = pygame.image.load(img_path + "/wall.png")
wall_2 = pygame.image.load(img_path + "/wall_2.png")
eyes_wall = pygame.image.load(img_path + "/eyes_wall.png")
eyes_floor = pygame.image.load(img_path + "/eyes_floor.png")
floor = pygame.image.load(img_path + "/floor.png")
floor_2 = pygame.image.load(img_path + "/floor_2.png")
hero = pygame.image.load(img_path + "/hero.png")
yellow_flower = pygame.image.load(img_path + "/yellow.png")
blue_flower = pygame.image.load(img_path + "/blue.png")
green_flower = pygame.image.load(img_path + "/green.png")
exit = pygame.image.load(img_path + "/exit.png")
bad_flower = pygame.image.load(img_path + "/bad_flower.png")
bad_flower2 = pygame.image.load(img_path + "/bad_flower2.png")
wall_pp = pygame.image.load(img_path + "/wall_pp.png")

textures = [
    [1,2,6,1,1,2,1,1,2],
    [6,4,1,3,4,4,5,4,6],
    [1,3,1,2,1,3,1,6,1],
    [6,4,3,5,1,3,4,4,2],
    [2,5,2,4,1,2,1,5,1],
    [1,4,1,3,6,3,6,4,6], 
    [2,3,2,1,1,4,1,3,2], 
    [1,4,3,3,4,5,1,4,1],
    [6,4,1,2,1,1,2,5,2],
    [1,5,1,5,6,3,1,4,1],
    [2,3,2,4,5,4,3,3,6],
    [1,3,1,4,1,1,2,1,2],
    [1,5,4,3,4,5,4,3,1],
    [2,1,6,2,1,6,1,2,1],   
]

rects = []
rects_textures = []

bad_rects = [] 

x = 0
y = 0

for texture in textures:    
    for i in texture:       
        kvadrat = pygame.Rect(x, y, 50, 50)
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 1:
            bad_rects.append(kvadrat)
        if i == 2:
            bad_rects.append(kvadrat)  
        if i == 6:
            bad_rects.append(kvadrat) 

        x += 50 
    y += 50   
    x = 0  

dlina_spiska = len(rects)

game = True
can_move = True

while game:

    display.fill((34, 35, 74))

    pygame.draw.rect(display, (0,255,0), geroi)
    font = pygame.font.SysFont("Arial", 70)
    text = font.render("YOU WIN!", True, (135, 15, 15))

    for i in range(dlina_spiska):
        if rects_textures[i] == 1:
            display.blit(wall, rects[i])
        if rects_textures[i] == 2:
            display.blit(eyes_wall, rects[i])
        if rects_textures[i] == 3:
            display.blit(floor, rects[i])
        if rects_textures[i] == 4:
            display.blit(floor_2, rects[i]) 
        if rects_textures[i] == 5:
            display.blit(eyes_floor, rects[i])  
        if rects_textures[i] == 6:
            display.blit(wall_2, rects[i])   

    display.blit(wall_pp, pp_wall)
    display.blit(bad_flower2, flower_bad2)
    display.blit(bad_flower, flower_bad)
    display.blit(exit, finish)
    display.blit(green_flower, flower_green)      
    display.blit(blue_flower, flower_blue)
    display.blit(yellow_flower, flower_yellow)
    display.blit(hero, geroi) 
    
    for bad in bad_rects:
        if geroi.colliderect(bad):
            geroi.x = 55
            geroi.y = 55 

    if geroi.colliderect(flower_yellow):
            geroi.x = 55
            geroi.y = 55  

    if geroi.colliderect(flower_blue):
            geroi.x = 155
            geroi.y = 555  

    if geroi.colliderect(flower_green):
            geroi.x = 155
            geroi.y = 155  
            pp_wall.x = 1000
            pp_wall.y = 1000

    if geroi.colliderect(flower_bad):
            geroi.x = 55
            geroi.y = 55  

    if geroi.colliderect(flower_bad2):
            geroi.x = 55
            geroi.y = 55      

    if geroi.colliderect(pp_wall):
            geroi.x = 55
            geroi.y = 55 

    if geroi.colliderect(finish):
            display.fill((0, 0, 0))
            display.blit(text, (100,100))   
            can_move = False        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
        if can_move == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    go_right = True
                if event.key == pygame.K_a:
                    go_left = True
                if event.key == pygame.K_s:
                    go_down = True
                if event.key == pygame.K_w:
                    go_up = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    go_right = False
                if event.key == pygame.K_a:
                    go_left = False
                if event.key == pygame.K_s:
                    go_down = False
                if event.key == pygame.K_w:
                    go_up = False   
            

    if go_right == True and can_move == True:
        geroi.x += 5
    if go_left == True and can_move == True:
        geroi.x -= 5
    if go_down == True and can_move == True:
        geroi.y += 5
    if go_up == True and can_move == True:
        geroi.y -= 5

    pygame.display.flip()
    clock.tick(60)