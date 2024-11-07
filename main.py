#Next Up:
#register the correct click
#drop the box if click and incorrect.


# import sys module
import pygame
import sys
import random  
import time

# pygame.init() will initialize all
# imported module
pygame.init()
  
clock = pygame.time.Clock()
  
# it will display on screen
screen = pygame.display.set_mode([600, 500])
  
# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rectangle
q_rect = pygame.Rect(200, 150, 140, 32)
input_rect = pygame.Rect(200, 200, 140, 32)
output_rect1 = pygame.Rect(325, 225, 140, 32)
output_rect2 = pygame.Rect(325, 300, 140, 32)
output_rect3 = pygame.Rect(125, 225, 140, 32)
output_rect4 = pygame.Rect(125, 300, 140, 32)
answer_rect = pygame.Rect(200, 400, 140, 32)
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive

#color of output box
color_o = pygame.Color('blue')

color_a = pygame.Color('white')
color_o_correct = pygame.Color('green')  
color_o_incorrect = pygame.Color('red')

#color of question
color_q = pygame.Color("white")

o_text = ""
active = False
game_on = True

options = range(1,11)
def setQText():
    x = random.choice(options)
    y = random.choice(options)
    q_text1 = "What is {} + {}".format(x,y)
    return q_text1,x,y

q_text = "FALSE"

answer = ""
answer1 = ""
answer2 = ""
answer3 = ""
answer4 = "" 
yesno = ""

winning = False

def assignAnswer(answer1, answer2, answer3, answer4, x,y):
    listAns = [answer1, answer2, answer3, answer4]
    a_answer = str(x + y)
    possible_answer = []
    p = 1 
    while p < len(listAns): 
        possible_answer.append(str(random.choice(options)+random.choice(options)))
        p += 1
    possible_answer.append(a_answer)
    print(possible_answer)
    for item, indy in enumerate(listAns):
        tempans = random.choice(possible_answer)
        listAns[item] = tempans
        possible_answer.remove(tempans)
    
    answer1 = listAns[0]
    answer2 = listAns[1]
    answer3 = listAns[2]
    answer4 = listAns[3]
    print(listAns)
    print(possible_answer)
    return answer1, answer2, answer3, answer4



#You want to assign the answer to a random answer
#Assign random answers to the rest of the answers
#Return answer1, answer2, answer3, answer4



#this is essentially a never ending while loop so we're constantly getting events and drawing rectangles.     
while True:
    
    if len(o_text) == 0:
        color_o == color_o
    elif str(o_text) == answer:
        color_a = color_o_correct
        yesno = "CORRECT"
        winning = True
    elif len(o_text) == 0:
        color_a = pygame.Color("white")
        yesno = ""
    else:
        yesno = "INCORRECT"
        color_a = color_o_incorrect


    for event in pygame.event.get():

    # if user types QUIT then the screen will close
        if q_text == "FALSE":
            result = setQText()
            q_text = result[0]
            x = result[1]
            y = result[2]
            answer = str(x+y)
            answer1, answer2, answer3, answer4 = assignAnswer(answer1, answer2, answer3, answer4, x, y)
            print(answer1, answer2, answer3, answer4)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if output_rect1.collidepoint(event.pos):
                o_text = answer1
            elif output_rect2.collidepoint(event.pos):
                o_text = answer2
            elif output_rect3.collidepoint(event.pos):
                o_text = answer3
            elif output_rect4.collidepoint(event.pos):
                o_text = answer4
            else:
                continue

        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                o_text = user_text                
                
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
    
        

    # it will set background color of screen
    screen.fill((255, 255, 255))
  
    if active:
        color = color_active
    else:
        color = color_passive
          
    # draw rectangle and argument passed which should
    # be on screen
    #pygame.draw.rect(screen, color, input_rect)
    pygame.draw.rect(screen, color_o, output_rect1)
    pygame.draw.rect(screen, color_o, output_rect2)
    pygame.draw.rect(screen, color_o, output_rect3)
    pygame.draw.rect(screen, color_o, output_rect4)
    pygame.draw.rect(screen, color_q, q_rect)
    pygame.draw.rect(screen, color_a, answer_rect)

    #text_surface = base_font.render(user_text, True, (255, 255, 255))
    text_surface_1 = base_font.render(answer1, True, (255, 255, 255))
    text_surface_2 = base_font.render(answer2, True, (255, 255, 255))
    text_surface_3 = base_font.render(answer3, True, (255, 255, 255))
    text_surface_4 = base_font.render(answer4, True, (255, 255, 255))
    text_surface_o = base_font.render(q_text, True, (000,000,000))
    text_surface_a = base_font.render(yesno, True, (000, 000, 000))
        
    # render at position stated in arguments
    #screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(text_surface_1, (output_rect1.x+5, output_rect1.y+5))
    screen.blit(text_surface_2, (output_rect2.x+5, output_rect2.y+5))
    screen.blit(text_surface_3, (output_rect3.x+5, output_rect3.y+5))
    screen.blit(text_surface_4, (output_rect4.x+5, output_rect4.y+5))
    screen.blit(text_surface_o,(q_rect.x+5, q_rect.y+5))
    screen.blit(text_surface_a,(answer_rect.x+5, answer_rect.y+5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    #input_rect.w = max(100, text_surface.get_width()+10)
    output_rect1.w = max(100, text_surface_1.get_width()+10)
    output_rect2.w = max(100, text_surface_2.get_width()+10)
    output_rect3.w = max(100, text_surface_3.get_width()+10)
    output_rect4.w = max(100, text_surface_4.get_width()+10)
    q_rect.w = max(100, text_surface_o.get_width()+10 )
    answer_rect.w = max(100, text_surface_a.get_width()+10 )
        
        # display.flip() will update only a portion of the
        # screen to updated, not full area
    pygame.display.flip()
        
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
    if winning == True:
        time.sleep(3)
        yesno = "" 
        o_text = ""
        result = setQText()
        q_text = result[0]
        answer = str(result[1] + result[2])
        x = result[1]
        y = result[2]
        answer1, answer2, answer3, answer4 = assignAnswer(answer1, answer2, answer3, answer4, x, y)
        winning = False
    clock.tick(60)