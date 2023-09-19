import pygame

pygame.init() # 초기화 작업 필수

screen_width = 480
screen_height = 640

pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("게임 제목")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            


pygame.quit()