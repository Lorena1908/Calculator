import pygame

WIDTH, HEIGHT = 525, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Calculator')

class Button:
    def __init__(self, x, y, pic, width=87.5, height=105, color=(32, 33, 36)):
        self.x = x
        self.y = y
        self.pic = pic
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
    # BUTTON PICTURES

    # Objects
    backspace = pygame.image.load('button_pictures/backspace.png')
    plus = pygame.image.load('button_pictures/plus.png')
    minus = pygame.image.load('button_pictures/minus.png')
    multiply = pygame.image.load('button_pictures/multiply.png')
    division = pygame.image.load('button_pictures/division.png')
    equal = pygame.image.load('button_pictures/dot.png')
    dot = pygame.image.load('button_pictures/equal.png')
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
        Button(0,495, zero), 
        Button(0,390, one), 
        Button(87.5,390, two), 
        Button(175,390, three), 
        Button(0,285, four), 
        Button(87.5,285, five), 
        Button(175,285, six), 
        Button(0,180, seven), 
        Button(87.5,180, eight), 
        Button(175,180, nine),
        Button(87.5,495, equal),
        Button(175,495, dot),
        Button(262.5, 516, plus, height=84),
        Button(262.5, 432, minus, height=84),
        Button(262.5, 348, multiply, height=84),
        Button(262.5, 264, division, height=84),
        Button(262.5, 180, backspace, height=84),
        Button(350, 180, sqrt, color=(23, 78, 166)),
        Button(350, 285, power, color=(23, 78, 166)),
        Button(350, 495, left_bracket, color=(23, 78, 166)),
        Button(437.5, 495, right_bracket, color=(23, 78, 166)),
        Button(350, 390, pi, color=(23, 78, 166)),
        Button(437.5, 180, percent, color=(23, 78, 166)),
        Button(437.5, 285, log, color=(23, 78, 166)),
        Button(437.5, 390, exclamation_mark, color=(23, 78, 166))
    ]

    WIN.fill((45, 48, 51))
    pygame.draw.rect(WIN, (32, 33, 36), (0, 180, 350, HEIGHT-180))
    pygame.draw.rect(WIN, (23, 78, 166), (350, 180, WIDTH-350, HEIGHT-180))
    for btn in buttons:
        btn.draw()
    pygame.draw.line(WIN, (48, 48, 50), (262.5, 180), (262.5, HEIGHT))
    pygame.display.update()

def main():
    draw_window()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

main()