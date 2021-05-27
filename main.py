import pygame
import math

WIDTH, HEIGHT = 525, 560
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Calculator')
pygame.font.init()

class Button:
    def __init__(self, x, y, pic, symbol, width=87.5, height=105, color=(32, 33, 36)):
        self.x = x
        self.y = y
        self.pic = pic
        self.symbol = symbol
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
        WIN.blit(self.pic, (self.x+self.width/2 - self.pic.get_width()/2, self.y+self.height/2 - self.pic.get_height()/2))
    
    def clicked(self, posx, posy):
        if self.x <= posx <= self.x + self.width and self.y <= posy <= self.y + self.height:
            return True
        else:
            return False

def draw_window():
    global buttons
    # BUTTON PICTURES

    # Objects
    backspace = pygame.image.load('button_pictures/backspace.png')
    plus = pygame.image.load('button_pictures/plus.png')
    minus = pygame.image.load('button_pictures/minus.png')
    multiply = pygame.image.load('button_pictures/multiply.png')
    division = pygame.image.load('button_pictures/division.png')
    equal = pygame.image.load('button_pictures/equal.png')
    dot = pygame.image.load('button_pictures/dot.png')
    sqrt = pygame.image.load('button_pictures/sqrt.png')
    power = pygame.image.load('button_pictures/power.png')
    left_bracket = pygame.image.load('button_pictures/left_bracket.png')
    right_bracket = pygame.image.load('button_pictures/right_bracket.png')
    pi = pygame.image.load('button_pictures/pi.png')
    percent = pygame.image.load('button_pictures/percent.png')
    log = pygame.image.load('button_pictures/log.png')
    exclamation_mark = pygame.image.load('button_pictures/exclamation_mark.png')

    # Numbers
    zero = pygame.image.load('button_pictures/0.png')
    one = pygame.image.load('button_pictures/1.png')
    two = pygame.image.load('button_pictures/2.png')
    three = pygame.image.load('button_pictures/3.png')
    four = pygame.image.load('button_pictures/4.png')
    five = pygame.image.load('button_pictures/5.png')
    six = pygame.image.load('button_pictures/6.png')
    seven = pygame.image.load('button_pictures/7.png')
    eight = pygame.image.load('button_pictures/8.png')
    nine = pygame.image.load('button_pictures/9.png')

    # BUTTONS
    buttons = [
        Button(175,435, equal, '='),
        Button(0,435, zero, '0'), 
        Button(0,350, one, '1'), 
        Button(87.5,350, two, '2'), 
        Button(175,350, three, '3'), 
        Button(0,245, four, '4'), 
        Button(87.5,245, five, '5'), 
        Button(175,245, six, '6'), 
        Button(0,140, seven, '7'), 
        Button(87.5,140, eight, '8'), 
        Button(175,140, nine, '9'),
        Button(87.5,435, dot, '.'),
        Button(262.5, 476, plus, '+', height=84),
        Button(262.5, 392, minus, '-', height=84),
        Button(262.5, 308, multiply, '×', height=84),
        Button(262.5, 224, division, '÷', height=84),
        Button(262.5, 140, backspace, '', height=84),
        Button(350, 140, sqrt, '√', color=(23, 78, 166)),
        Button(350, 245, power, '^', color=(23, 78, 166)),
        Button(350, 435, left_bracket, '(', color=(23, 78, 166)),
        Button(437.5, 435, right_bracket, ')', color=(23, 78, 166)),
        Button(350, 350, pi, '3.1415926535897', color=(23, 78, 166)),
        Button(437.5, 140, percent, '%', color=(23, 78, 166)),
        Button(437.5, 245, log, 'log(', color=(23, 78, 166)),
        Button(437.5, 350, exclamation_mark, '!', color=(23, 78, 166))
    ]

    WIN.fill((45, 48, 51))
    pygame.draw.rect(WIN, (32, 33, 36), (0, 140, 350, HEIGHT-140))
    pygame.draw.rect(WIN, (23, 78, 166), (350, 140, WIDTH-350, HEIGHT-140))
    for btn in buttons:
        btn.draw()
    pygame.draw.line(WIN, (48, 48, 50), (262.5, 140), (262.5, HEIGHT))

# def factorial(num):
#     i = 1
#     result = 1
#     while i <= num:
#         result *= i
#         i += 1
#     return result

def main():
    run = True
    input_box = []
    show = ''
    font = pygame.font.SysFont('comicsans', 50)
    draw_window()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for btn in buttons:
                    if btn.clicked(x, y) and btn == buttons[0]: # =
                        print(input_box)
                        print(show)
                        # get the result and display on the screen
                        input_box.clear()
                    elif btn.clicked(x, y) and btn == buttons[16]: # Backspace
                        show = show[:-1]
                        if len(input_box) != 0:
                            input_box.pop()
                        pygame.draw.rect(WIN, (45, 48, 51), (0,0, WIDTH, HEIGHT-420))
                        text = font.render(show, 1, (255,255,255))
                        WIN.blit(text, (WIDTH-30 - text.get_width(), 140-20 - text.get_height()))
                    elif btn.clicked(x, y):
                        show += btn.symbol
                        input_box.append(btn)
                        pygame.draw.rect(WIN, (45, 48, 51), (0,0, WIDTH, HEIGHT-420))
                        text = font.render(show, 1, (255,255,255))
                        WIN.blit(text, (WIDTH-30 - text.get_width(), 140-20 - text.get_height()))
        pygame.display.update()

main()