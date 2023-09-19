import pygame

pygame.init() # 초기화 작업 필수

screen_width = 480
screen_height = 640

#screen 변수 생성 (화면)
screen = pygame.display.set_mode((screen_width,screen_height))

#게임 타이틀
pygame.display.set_caption("게임 제목")

#배경
background = pygame.image.load("C:\\study\\Python\\util\\background_sample.jpg")



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #screen.fill((255, 255, 255))
    screen.blit(background, (0,0))

    pygame.display.update()


pygame.quit()