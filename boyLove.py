
import random
import pygame


def main():
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    FPSCLOCK = pygame.time.Clock()
    pygame.key.set_repeat(10, 30)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 103, 163)

    LIFE_COUNT = 3

    large_font = pygame.font.SysFont('malgungothic', 72)
    small_font = pygame.font.SysFont('malgungothic', 20)
    score = 0
    game_over = False

    ##그림객체
    boy_image = pygame.image.load('image/boy.png')
    boy_pos = boy_image.get_rect(centerx=300, bottom=800)

    ##하트 이미지
    love_image = pygame.image.load('image/love.png')
    loves = []
    for i in range(3):
        love = love_image.get_rect(left=random.randint(0, 600 - love_image.get_width()), top=-100)
        dy = random.randint(3, 9)
        loves.append((love, dy))

    #생명 이미지
    life_image = pygame.image.load('image/life_2.png');
    lifes = []
    for i in range(LIFE_COUNT):
        life = life_image.get_rect(top=0, left=600 - love_image.get_width()*(i+1))
        lifes.append(life)

    #게임루프
    while True:
        SCREEN.fill(WHITE)

        #이벤트 처리
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        #방향키 이벤트 처리
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boy_pos.left -= 10
            elif event.key == pygame.K_RIGHT:
                boy_pos.right += 10

        if not game_over:
            for love, dy in loves:
                love.top += dy
                if love.top > 800:
                    lifes.pop()
                    if len(lifes)==0 :
                        game_over = True
                    loves.remove((love, dy))
                    love = love_image.get_rect(left=random.randint(0, 600 - love.width), top=-100)
                    dy = random.randint(3, 9)
                    loves.append((love, dy))


            #벽 처리
            if boy_pos.left < 0:
                boy_pos.left = 0
            elif boy_pos.right > 600:
                boy_pos.right = 600

            for love, dy in loves:
                if love.colliderect(boy_pos):
                    score += 1
                    loves.remove((love, dy))

                    love = love_image.get_rect(left=random.randint(0, 600 - love.width), top=-100)
                    dy = random.randint(3, 9)
                    loves.append((love, dy))


        # 화면 그리기
        for love, dy in loves:
            SCREEN.blit(love_image, love)
        for life in lifes:
            SCREEN.blit(life_image, life)

        SCREEN.blit(boy_image, boy_pos)
        score_image = small_font.render('score : {}'.format(score), True, BLUE)
        SCREEN.blit(score_image, (10, 10))

        if game_over:
            game_over_image = large_font.render('GAME OVER', True, RED)
            score_image = small_font.render('score : {}'.format(score), True, BLACK)
            SCREEN.blit(game_over_image, game_over_image.get_rect(centerx=300, top=+300))
            SCREEN.blit(score_image, score_image.get_rect(centerx=300, top=+400))
        # 모든화면그리기 업데이트
        pygame.display.update()
        FPSCLOCK.tick(30) #초당 프레임수

    pygame.quit()


if __name__ == '__main__':
    main()

# pyinstaller -w -F 파일이름.py
# ㅍㅏ이썬 실행파일 만들기