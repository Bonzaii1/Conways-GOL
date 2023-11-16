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


def rule_one(col, row, new_set, positions):
    #LEFT - RIGHT = COL
     # UP - DOWN = ROW
    count = 0

    # Rule 1: Check for only 1 or less neighbors
    # Get valid neighbors of cells
    for i in range(-1, 2):  # Iterate over neighboring rows
        for j in range(-1, 2):  # Iterate over neighboring columns
            new_col = col + j * TILE_SIZE
            new_row = row + i * TILE_SIZE

            # Check if the new indices are within bounds
            if 0 <= new_col < WIDTH and 0 <= new_row < HEIGHT:
                if (new_col, new_row) in positions:
                    count+=1
    print(count)
    if(count <= 1):
        new_set.remove((col, row))
    return new_set
        


def check_neighbors(positions: set):
    new_set = positions.copy()
    for position in positions:
        col, row = position 

        new_set = rule_one(col, row, new_set, positions)
        

    return new_set
    
            

        

        
        



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
                posX = (pos[0]//TILE_SIZE) * TILE_SIZE
                posY = (pos[1]//TILE_SIZE) * TILE_SIZE
            
                positions.add((posX, posY))  
                print(positions)    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulate = not simulate


               
        if(simulate):
            print("simulating")
            positions = check_neighbors(positions)
        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
