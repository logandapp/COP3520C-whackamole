import pygame
import random

TILE_SIZE = 32
MAP_SIZE = (20, 16)

def convert_to_tile(x_pos: int, y_pos: int):
    """
    :param x_pos: mouse x-coordinate.
    :param y_pos: mouse y-coordinate.
    :return: the "world coordinate" a.k.a. the tile location.
    """
    return x_pos // TILE_SIZE, y_pos // TILE_SIZE

def generate_mole(screen, mole_obj, x_loc: int, y_loc: int):  # Would much rather do this in a class.
    screen.blit(mole_obj, mole_obj.get_rect(topleft=(x_loc * TILE_SIZE, y_loc * TILE_SIZE)))

def generate_random_mole():  # screen, mole_obj):
    x_loc = random.randrange(0, MAP_SIZE[0])
    y_loc = random.randrange(0, MAP_SIZE[1])
    # generate_mole(screen, mole_obj, x_loc, y_loc)
    return x_loc, y_loc

def main():
    try:
        pygame.init()

        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_loc = generate_random_mole()

        while running:

            screen.fill("light green")
            for x_ in range(0, MAP_SIZE[0] * TILE_SIZE, TILE_SIZE):
                pygame.draw.line(screen, 'dark green', (x_, 0), (x_, MAP_SIZE[1] * TILE_SIZE))
            for y_ in range(0, MAP_SIZE[1] * TILE_SIZE, TILE_SIZE):
                pygame.draw.line(screen, 'dark green', (0, y_), (MAP_SIZE[0] * TILE_SIZE, y_))
            generate_mole(screen, mole_image, mole_loc[0], mole_loc[1])
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                tile_clicked = None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tile_clicked = convert_to_tile(event.pos[0], event.pos[1])

                if tile_clicked is not None:
                    if tile_clicked == mole_loc:
                        mole_loc = generate_random_mole()

            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
