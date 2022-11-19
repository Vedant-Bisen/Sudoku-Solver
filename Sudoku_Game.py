import pygame

WIDTH,HEIGHT = 980,980

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")
BORDER1 = pygame.Rect(0,0,10,HEIGHT)
BORDER2 = pygame.Rect(0,0,WIDTH,10)
BORDER3 = pygame.Rect(WIDTH-10,0,10,HEIGHT)
BORDER4 = pygame.Rect(0,HEIGHT-10,WIDTH,10)

MIDDLELINE1 = pygame.Rect(0,45*6,WIDTH,10)
MIDDLELINE2 = pygame.Rect(0,95*6,WIDTH,10)


WHITE = (255,255,255)
BLACK = (0,0,0)




def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,BORDER1)
    pygame.draw.rect(WIN,BLACK,BORDER2)
    pygame.draw.rect(WIN,BLACK,BORDER3)
    pygame.draw.rect(WIN,BLACK,BORDER4)
    pygame.draw.rect(WIN,BLACK,MIDDLELINE1)
    pygame.draw.rect(WIN,BLACK,MIDDLELINE2)
    pygame.display.update()
    


def main():
    run = True
    while(run):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

        draw_window()

    
    pygame.display.quit()




if __name__ == '__main__':
    main()