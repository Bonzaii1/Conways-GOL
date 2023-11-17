import pygame
import random
pygame.init()

#Define Constants
BLACK = (0,0,0)
GREY = (128, 128, 128)
YELLOW = (255,255,0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH//TILE_SIZE
GRID_HEIGHT = HEIGHT//TILE_SIZE
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def setRandomGrid(num):
    return set([(random.randrange(0, GRID_HEIGHT) * 20, random.randrange(0, GRID_WIDTH) * 20) for _ in range(num)])



def adjustGrid(positions: set):
    new_set = set()
    dead_cells = set()

    
    for position in positions:
        col, row = position
        all_neighbors = getNeighbors(col, row)


        
        count = 0
        for neighbor in all_neighbors:
            if neighbor in positions:
                count+=1
            else:
                dead_cells.add(neighbor)
        if count == 2 or count == 3:
            new_set.add(position)

        
        
        for cell in dead_cells:
            col_dead, row_dead = cell
            all_neighbors_dead = getNeighbors(col_dead, row_dead)
            count_dead = sum(1 for neighbor in all_neighbors_dead if neighbor in positions)
            
            
            if count_dead == 3:
                new_set.add(cell)
            
    return new_set


            



def getNeighbors(col, row):
    neighbors = set()
    for i in range(-1, 2):  # Iterate over neighboring rows
        for j in range(-1, 2):  # Iterate over neighboring columns
            new_col = col + j * TILE_SIZE
            new_row = row + i * TILE_SIZE

            # Check if the new indices are within bounds
            if 0 <= new_col < WIDTH and 0 <= new_row < HEIGHT:
                neighbors.add((new_col, new_row))

    # Remove the cell itself from the neighbors
    neighbors.remove((col, row))
    
    return neighbors

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
                if((posX, posY) in positions):
                    positions.remove((posX, posY))
                else:
                    positions.add((posX, posY))  
                #print(positions)    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulate = not simulate
                if event.key == pygame.K_r:
                    positions = setRandomGrid(random.randrange(7, 10) * 20)
                if event.key == pygame.K_w:
                    positions = set()


               
        if(simulate):
            positions = adjustGrid(positions)
        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
