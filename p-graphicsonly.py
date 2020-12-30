import ast
import time
import pygame

Width = 1000
Height = 1000

f = open('positions.txt', 'r')
posits = ast.literal_eval(f.read())
f.close()

def main():
    '''main method'''
    pygame.init()
    screen=pygame.display.set_mode([Width,Height])
    clock=pygame.time.Clock()

    cntr=0
    t0 = time.time()

    for i in range(len(posits)):
        screen.fill((0,0,0))
        for j in range(len(posits[i])):
            if posits[i][j][2] == 0.0:
                continue
#            if j < len(posits[i])/2:
#                color = (0,0,255)
#            else:
#                color = (255,0,0)
            color = (255,255,255)
            pygame.draw.circle(screen,color,[round(posits[i][j][0]),round(posits[i][j][1])],round((posits[i][j][2]/3.14)**0.5))
        pygame.image.save(screen,'images/s_'+str("{:04d}".format(cntr))+'.jpeg')
        cntr+=1
    
    print("Done in "+str(time.time()-t0)+" seconds.")
    pygame.quit()
main()
