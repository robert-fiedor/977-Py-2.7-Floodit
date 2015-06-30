import pygame
import pygame.gfxdraw
import pygame.rect

def main():

    pygame.init()
    screen = pygame.display.set_mode((500,500))
    screen.fill((255, 255, 255))

    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)

    pygame.gfxdraw.aacircle(s, 250, 250, 200, (0, 0, 0))

    pygame.gfxdraw.rectangle(s, (200,150,100,50), (0,0,255))

    screen.blit(s, (0, 0))
    pygame.display.update()










    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
            pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()