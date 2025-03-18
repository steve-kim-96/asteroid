from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
