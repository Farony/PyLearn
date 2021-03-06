import pygame
import sys

FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

while 1:
    for i in pygame.event.get():
        # print(i)
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            print(i.type)
            print(i.key)
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
            elif i.key == 1073741905:
                y += 3
            elif i.key == 1073741906:
                y -= 3
        elif i.type == pygame.MOUSEBUTTONDOWN:
            print(i)
            print(i.type)
            if i.button == 1:
                print("Нажата клавиша 1")
            else:
                print("Нажата не 1 клавиша")

    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()
    clock.tick(FPS)