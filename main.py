import pygame
import math

WIDTH, HEIGHT = 525, 560
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Calculator')
pygame.font.init()
font = pygame.font.SysFont('comicsans', 50)

operation_order = ['(', 'log(', '!', '^', '√', '%', '×', '÷', '+', '-', ')']

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
    
    def clicked(self, posx=0, posy=0):
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

def factorial(num):
    i = 1
    result = 1
    while i <= num:
        result *= i
        i += 1
    return result

def add_complete_num(input_box):
    length = 0
    for i, item in enumerate(input_box):
        if i > 0:
            if item.isnumeric() and input_box[i-1].isnumeric():
                length += 1

    for num in range(length):
        for i, item in enumerate(input_box):
            if i > 0 and item.isnumeric() and input_box[i-1].isnumeric():
                input_box[i-1] = input_box[i-1]+input_box[i]
                input_box.pop(i)
    return input_box 

def add_to_dict(dict, input_box):
    for i, item in enumerate(input_box):
        if isinstance(item, float):
            continue
        elif not item.isnumeric():
            dict[item] = i
    return len(dict)

def new_order(order):
    order2 = []
    for key in order:
        order2.append(key[0])
    return order2

def calculate(input_box):
    temp_dict = {}
    to_del = []
    dict_len = add_to_dict(temp_dict, input_box)
    keys = temp_dict.keys()
    order = []

    for i in keys:
        if i == operation_order[0]:
            order.append((i, 0))
        elif i == operation_order[1]:
            order.append((i, 1))
        elif i == operation_order[2]:
            order.append((i, 2))
        elif i == operation_order[3]:
            order.append((i, 3))
        elif i == operation_order[4]:
            order.append((i, 4))
        elif i == operation_order[5]:
            order.append((i, 5))
        elif i == operation_order[6]:
            order.append((i, 6))
        elif i == operation_order[7]:
            order.append((i, 7))
        elif i == operation_order[8]:
            order.append((i, 8))
        elif i == operation_order[9]:
            order.append((i, 9))
    
    order = sorted(order, key=lambda x : x[1])
    order = new_order(order)

    for key in order:
        add_to_dict(temp_dict, input_box)
        if key == operation_order[0]: # (
            pass

        elif key == operation_order[1]: # log(
            input_box[temp_dict[key]+1] = math.log10(float(input_box[temp_dict[key]+1]))
            input_box.pop(temp_dict[key])
            to_del.append(key)
            if len(input_box) > 1:
                if input_box[temp_dict[key]+1] == operation_order[-1]:
                    input_box.pop(temp_dict[key]+1)

        elif key == operation_order[2]: # !
            input_box[temp_dict[key]-1] = factorial(float(input_box[temp_dict[key]-1]))
            input_box.pop(temp_dict[key])
            to_del.append(key)

        elif key == operation_order[3]: # ^
            input_box[temp_dict[key]+1] = float(input_box[temp_dict[key]-1]) ** float(input_box[temp_dict[key]+1])
            input_box.pop(temp_dict[key])
            input_box.pop(temp_dict[key]-1)
            to_del.append(key)

        elif key == operation_order[4]: # √
            input_box[temp_dict[key]+1] = math.sqrt(float(input_box[temp_dict[key]+1]))
            input_box.pop(temp_dict[key])
            to_del.append(key)

        elif key == operation_order[5]: # %
            if len(input_box[temp_dict[key]:]) > 1:
                if isinstance(input_box[temp_dict[key]+1], float) or  input_box[temp_dict[key]+1].isnumeric():
                    input_box[temp_dict[key]-1] = float(input_box[temp_dict[key]-1]) / 100 * float(input_box[temp_dict[key]+1])
                    input_box.pop(temp_dict[key])
                    input_box.pop(temp_dict[key])
            else:
                input_box[temp_dict[key]-1] = float(input_box[temp_dict[key]-1]) / 100
                input_box.pop(temp_dict[key])
            to_del.append(key)
        
        elif key == operation_order[6]: # ×
            input_box[temp_dict[key]+1] = float(input_box[temp_dict[key]-1]) * float(input_box[temp_dict[key]+1])
            input_box.pop(temp_dict[key])
            input_box.pop(temp_dict[key]-1)
            to_del.append(key)

        elif key == operation_order[7]: # ÷
            input_box[temp_dict[key]+1] = float(input_box[temp_dict[key]-1]) / float(input_box[temp_dict[key]+1])
            input_box.pop(temp_dict[key])
            input_box.pop(temp_dict[key]-1)
            to_del.append(key)

        elif key == operation_order[8]: # +
            input_box[temp_dict[key]+1] = float(input_box[temp_dict[key]-1]) + float(input_box[temp_dict[key]+1])
            input_box.pop(temp_dict[key])
            input_box.pop(temp_dict[key]-1)
            to_del.append(key)

        elif key == operation_order[9]: # -
            input_box[temp_dict[key]+1] = float(input_box[temp_dict[key]-1]) - float(input_box[temp_dict[key]+1])
            input_box.pop(temp_dict[key])
            input_box.pop(temp_dict[key]-1)
            to_del.append(key)
    
    for key in to_del:
        del temp_dict[key]
    return input_box[0]

def press_key(show):
    pygame.draw.rect(WIN, (45, 48, 51), (0,0, WIDTH, HEIGHT-420))
    text = font.render(show, 1, (255,255,255))
    WIN.blit(text, (WIDTH-30 - text.get_width(), 140-20 - text.get_height()))

def main():
    run = True
    input_box = []
    show = ''
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
                        pygame.draw.rect(WIN, (45, 48, 51), (0,0, WIDTH, HEIGHT-420))
                        answer = calculate(add_complete_num(input_box))
                        text = font.render(str(answer), 1, (255,255,255))
                        WIN.blit(text, (WIDTH-30 - text.get_width(), 140-20 - text.get_height()))
                        show = str(answer)
                        input_box.clear()
                        input_box.append(answer)

                    elif btn.clicked(x, y) and btn == buttons[16]: # Backspace
                        show = show[:-1]
                        if len(input_box) != 0:
                            input_box.pop()
                        pygame.draw.rect(WIN, (45, 48, 51), (0,0, WIDTH, HEIGHT-420))
                        text = font.render(show, 1, (255,255,255))
                        WIN.blit(text, (WIDTH-30 - text.get_width(), 140-20 - text.get_height()))

                    elif btn.clicked(x, y):
                        show += btn.symbol
                        input_box.append(btn.symbol)
                        pygame.draw.rect(WIN, (45, 48, 51), (0,0, WIDTH, HEIGHT-420))
                        text = font.render(show, 1, (255,255,255))
                        WIN.blit(text, (WIDTH-30 - text.get_width(), 140-20 - text.get_height()))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    show += buttons[1].symbol
                    input_box.append(buttons[1].symbol)
                    press_key(show)
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    show += buttons[2].symbol
                    input_box.append(buttons[2].symbol)
                    press_key(show)
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    show += buttons[3].symbol
                    input_box.append(buttons[3].symbol)
                    press_key(show)
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    show += buttons[4].symbol
                    input_box.append(buttons[4].symbol)
                    press_key(show)
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    show += buttons[5].symbol
                    input_box.append(buttons[5].symbol)
                    press_key(show)
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    show += buttons[6].symbol
                    input_box.append(buttons[6].symbol)
                    press_key(show)
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    show += buttons[7].symbol
                    input_box.append(buttons[7].symbol)
                    press_key(show)
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    show += buttons[8].symbol
                    input_box.append(buttons[8].symbol)
                    press_key(show)
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    show += buttons[9].symbol
                    input_box.append(buttons[9].symbol)
                    press_key(show)
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    show += buttons[10].symbol
                    input_box.append(buttons[10].symbol)
                    press_key(show)
                elif event.key == pygame.K_BACKSPACE:
                    show = show[:-1]
                    if len(input_box) != 0:
                        input_box.pop()
                    press_key(show)
                elif event.key == pygame.K_DELETE:
                    show = ''
                    input_box.clear()
                    press_key(show)
                elif event.key == pygame.K_KP_PLUS:
                    show += buttons[12].symbol
                    input_box.append(buttons[12].symbol)
                    press_key(show)
                elif event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                    show += buttons[13].symbol
                    input_box.append(buttons[13].symbol)
                    press_key(show)
                elif event.key == pygame.K_KP_MULTIPLY:
                    show += buttons[14].symbol
                    input_box.append(buttons[14].symbol)
                    press_key(show)
                elif event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_SLASH:
                    show += buttons[15].symbol
                    input_box.append(buttons[15].symbol)
                    press_key(show)
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    pygame.draw.rect(WIN, (45, 48, 51), (0,0, WIDTH, HEIGHT-420))
                    answer = calculate(add_complete_num(input_box))
                    text = font.render(str(answer), 1, (255,255,255))
                    WIN.blit(text, (WIDTH-30 - text.get_width(), 140-20 - text.get_height()))
                    show = str(answer)
                    input_box.clear()
                    input_box.append(answer)

        pygame.display.update()

main()