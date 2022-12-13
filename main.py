import pygame
import threading


def control_thread():
    continuer = 1
    while continuer:
        u_input = input('[:=]>')
        if u_input=='q':
            run =0
            continuer=0
        if u_input=="apply":
            force_x = -5
            
pygame.init()

HEIGHT,WIDTH = 500,500
frame_rate = 60

font = pygame.font.SysFont("Arial",20)

window = pygame.display.set_mode((HEIGHT,WIDTH))

run = 1
time = 0
clock = pygame.time.Clock()

x = 0
y = 0
pixel_size = 10

def display(x,y):
    txt = font.render("+",True,(0,0,0))
    #center the text
    text_rect = txt.get_rect(center=(x+WIDTH//2,y+HEIGHT//2))
    window.blit(txt,text_rect)

def apply_force(f_x,f_y):
    return (x+f_x,y+f_y)


force_x = 0
force_y = 0
wallsRect = pygame.Rect(0,0,HEIGHT,WIDTH)
#equation de cercle  2(x-a)+2(y-b)=r² -> eq parametrique x = 

circlex = WIDTH//2
circley= HEIGHT//2
def isCollide(x,y):
    pos = (2*(x-0)+2*(y-0))
    #print("pos : "+str(abs(pos)))
    #print(2*circlex)
    return  abs(pos-10)== (2*circlex) 

controlThread = threading.Thread(target=control_thread)
controlThread.start()

def set_force(value):
    
    return value
    
while run:
    window.fill((255,255,255))
    clock.tick(frame_rate)


    pygame.draw.ellipse(window,(0,0,0),wallsRect,4)
    processed_pos = apply_force(x,y)
    x+=set_force(value)
    display(x,y+force_y)
    

    #print(isCollide(x,y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = 0

    
    pygame.display.update()
    

pygame.quit()
exit()
