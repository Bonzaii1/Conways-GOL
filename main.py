import pygame

pygame.init()

#Define Constants
BLACK = (0,0,0)
GREY = (128, 128, 128)
YELLOW = (255,255,0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH//TILE_SIZE
GRID_HEIGHT = HEIGHT//TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()



def check_neighbors(positions):
    pass 


def draw_grid(positions):

    for position in positions:
        col, row = position

        pygame.draw.rect(screen, YELLOW, ((col // TILE_SIZE)  * TILE_SIZE, (row // TILE_SIZE) * TILE_SIZE, TILE_SIZE,  TILE_SIZE))
        

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

    

def main():
    running = True
    simulate = False

    positions = set()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                positions.add((pos[0], pos[1]))  
                print(positions)    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulate = not simulate


               
        if(simulate):
            print("simulating")
        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()