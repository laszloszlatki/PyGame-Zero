from random import randint
apple = Actor("apple")
orange = Actor("orange")
count = 0

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    
def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def place_orange():
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        global count
        print("Good shot!")
        count = count + 1
        place_apple()
        place_orange()
    else:
        print("I'm afraid you missed it this time!")
        print ("You hit the target " + str(count) + " times in a row")
        count = 0
        #quit()

place_apple()
place_orange()
         
