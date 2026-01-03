import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("runner")
clock = pygame.time.Clock()
game_active=True
font = pygame.font.Font("projects\pfont\GomePixel-DYJX1.otf",50)

sky_surf = pygame.image.load("projects\sky2.png").convert_alpha()
ground_surf = pygame.image.load("projects\ground-0002.png").convert_alpha()
score_surf = font.render("My game",False,(64,64,64))
score_rect = score_surf.get_rect(center=(400,50))

box_surf = pygame.image.load("projects\catbox7.png").convert_alpha()
box_rect = box_surf.get_rect(midbottom=(600,300))
box_scaled=pygame.transform.scale(box_surf,(90,45))

player_surf = pygame.image.load("projects\cat3.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(100,355))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            
            if event.type==pygame.MOUSEBUTTONDOWN :
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                    
                    player_gravity=-20
            
            if event.type==pygame.KEYDOWN:
                  
               if event.key==pygame.K_SPACE: 
                   player_gravity=-20
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True  
                box_rect.left=800
    
    if game_active:
            screen.blit(sky_surf,(0,0))
            screen.blit(ground_surf,(0,100))
            pygame.draw.rect(screen,"#efa905",score_rect)
            pygame.draw.rect(screen,"#efa905",score_rect,10)

            screen.blit(score_surf,score_rect)

    
            screen.blit(box_surf,box_rect)
            box_rect.x -=4
            if box_rect.right <=0:
                 
                box_rect.left =800
            screen.blit(player_surf,player_rect)
    
            #player
            player_gravity+=1
            player_rect.y+=player_gravity
            if player_rect.bottom >=355:
               player_rect.bottom=355
            screen.blit(player_surf,player_rect)
    
    
    #collision

            if box_rect.colliderect(player_rect):
              game_active=False
    else:
        screen.fill("yellow")
        
        
        

    
    

    
            
    pygame.display.update()
    clock.tick(60)
    
