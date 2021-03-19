
import random
import pygame


def main():
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    FPSCLOCK = pygame.time.Clock()
    pygame.key.set_repeat(30, 30)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 103, 163)
    large_font = pygame.font.SysFont('malgungothic', 72)
    small_font = pygame.font.SysFont('malgungothic', 36)
    score = 0
    game_over = False

    ##그림객체
    boy_image = pygame.image.load('image/boy.png')
    boy_pos = boy_image.get_rect(centerx=300, bottom=800)

    ##별 객체
    star_image = pygame.image.load('image/star.png')
    stars = []
    for i in range(3):
        star = star_image.get_rect(left=random.randint(0, 600 - star_image.get_width()), top=-100)
        dy = random.randint(3, 9)
        stars.append((star, dy))
    #게임루프
    while True:
        SCREEN.fill(WHITE)

        #이벤트 처리
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        #방향키 이벤트 처리
        elif event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                boy_pos.left -= 5
            elif event.key ==pygame.K_RIGHT:
                boy_pos.right += 5

        if not game_over:
            for star, dy in stars:
                star.top += dy
                if star.top > 800:
                    stars.remove((star, dy))
                    star = star_image.get_rect(left=random.randint(0, 600 - star.width), top=-100)
                    dy = random.randint(3, 9)
                    stars.append((star, dy))
                    score += 1


            #벽 처리
            if boy_pos.left < 0:
                boy_pos.left = 0
            elif boy_pos.right > 600:
                boy_pos.right = 600

            for star, dy in stars:
                if star.colliderect(boy_pos):
                    game_over = True

        # 화면 그리기
        for star, dy in stars:
            SCREEN.blit(star_image, star)

        SCREEN.blit(boy_image, boy_pos)
        score_image = small_font.render('점수{}'.format(score), True, BLUE)
        SCREEN.blit(score_image, (10, 10))

        if game_over:
            game_over_image = large_font.render('게임 종료', True, RED)
            score_image = small_font.render('점수{}'.format(score), True, BLACK)
            SCREEN.blit(game_over_image, game_over_image.get_rect(centerx=300, centery=400))
            SCREEN.blit(score_image, score_image.get_rect(centerx=300, top=+500))
        # 모든화면그리기 업데이트
        pygame.display.update()
        FPSCLOCK.tick(30) #초당 프레임수

    pygame.quit()


if __name__ == '__main__':
    main()

# pyinstaller -w -F 파일이름.py
# ㅍㅏ이썬 실행파일 만들기