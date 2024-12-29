import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("adding image")
image = pygame.transform.scale(pygame.image.load("download.jpeg").convert(), (250,250))
m1 = pygame.transform.scale(pygame.image.load("Sick-Cities-A-Scenario-for-Dhaka-City (1).jpg").convert(), (300,300))
done = False
while not done :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :

            pygame.quit()
    screen.blit(image,(0,0)) 
    screen.blit(m1,(250,0))      
    pygame.display.flip()        