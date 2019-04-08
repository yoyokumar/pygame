import pygame,sys
pygame.init()
display=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('ANIMATION')
img=pygame.image.load('cat.png')
fps=pygame.time.Clock()
picx=20
picy=20
direction='right'
while True:
    for event in pygame.event.get():
        display.fill((255,255,255))
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if direction=='right':
            picx+=5
            if picx==850:
                direction='down'
        elif direction=='down':
            picy+=5
            if picy==850:
                direction='left'
        elif direction=='left':
            picx-=5
            if picx==20:
                direction='up'
        else:
            picy-=5
            if picy==20:
                direction='right'
        display.blit(img,(picx,picy))
        pygame.display.update()
        fps.tick(30)
