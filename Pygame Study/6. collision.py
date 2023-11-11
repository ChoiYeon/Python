import pygame

pygame.init() # 초기화 작업 필수

screen_width = 480
screen_height = 640

#screen 변수 생성 (화면)
screen = pygame.display.set_mode((screen_width,screen_height))

#게임 타이틀
pygame.display.set_caption("게임 제목")

#FPS
clock = pygame.time.Clock()

#배경 변수
background = pygame.image.load("C:\\study\\Python\\util\\background_sample.jpg")

#스프라이트
character = pygame.image.load("C:\\study\\Python\\util\\character.png")

#스프라이트 크기
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

#스프라이트 위치 정보
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height

#이동 좌표
to_X = 0
to_Y = 0

#이동 속도
character_speed = 0.6

running = True

while running:

    dt = clock.tick(10) # 게임화면의 초당 프레임

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_X -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_X += character_speed
            elif event.key == pygame.K_UP:
                to_Y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_Y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_X = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:    
                to_Y = 0

    character_x_pos += to_X * dt
    character_y_pos += to_Y * dt

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width
    
    if character_y_pos < 0 : 
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #RGB값으로 배경 채울 시 
    #screen.fill((255, 255, 255))

    #이미지로 배경 채울 시 
    screen.blit(background, (0,0))

    #배경과 마찬가지 캐릭터의 초기 위치를 설정해줌
    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update()


pygame.quit()