import pygame, sys
import ocempgui.access
from random import randint
from pygame.locals import *
import time

#import gui stuff
from ocempgui.widgets import *
from ocempgui.widgets.components import TextListItem
from ocempgui.widgets.Constants import *



pygame.init()
fpsClock = pygame.time.Clock()

font = pygame.font.SysFont("monospace", 15)

log = []

class logFile():
    def __init__(self, message):
        self.message = message
        self.time = 100
        self.x = 600;
        self.y = 500
        
    def _create_vframe (text):
        frame = VFrame (Label (text))
        frame.spacing = 5
        frame.align = ALIGN_LEFT
        return frame
    
    def update(self):
        self.time-=.2
        self.y-=.1
    def draw(self, window):
        logString = font.render(self.message, 1, (0,255,0,))
        window.blit(logString, (self.x, self.y))

        
class player():
    def __init__(self, image, name, idNumber, health, attack, defense):
        self.image = pygame.image.load(image + '.png')
        self.button1 = pygame.image.load('attack.png')
        self.button2 = pygame.image.load('defend.png')
        
        self.name = name
        self.idNumber = idNumber
        self.health = health
        self.attack = attack
        self.defense = defense

        self.x = 100
        self.y = 300

        self.imageRect = Rect(self.x+50, self.y, self.image.get_rect().w, self.image.get_rect().h)
        self.button1Rect = Rect(self.x, self.y+120, self.button1.get_rect().w, self.button1.get_rect().h)
        self.button2Rect = Rect(self.x, self.y+200, self.button2.get_rect().w, self.button2.get_rect().h)
        
        self.alive = True
        
        print name, health, attack, defense
        
    def updateHealth(attack):
        this.health -= attack
        if this.health <= 0:
            self.alive = False
            
    # mouse x and y
    def doTurn(self, x, y, enemy):

        if(self.imageRect.collidepoint(x, y)):
            print "player clicked"
        elif(self.button1Rect.collidepoint(x, y)):
            enemy.getAttacked(self.attack)
            print "attack"
        elif(self.button2Rect.collidepoint(x, y)):
            print "defend"
            enemy.getDefend(self.defense)
        

    def draw(self, window):
        window.blit(self.image, self.imageRect)
        window.blit(self.button1, self.button1Rect)
        window.blit(self.button2, self.button2Rect)
        #pygame.draw.rect(window, (255,0,0), self.button1Rect)


class encounter():
    def __init__(self, image, name, health, attack, defense):
        self.image = pygame.image.load(image + '.png')
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

        self.alive = True

    def doTurn(self):
        print "doing turn..."

    def getAttacked(self, attackValue):
        self.health-=attackValue
        if self.health <= 0:
            self.alive = False;
        else:
            log.append(logFile("player attacked for a damage of: " + str(attackValue)))

    def getDefend(self, defendValue):
        log.append(logFile("player defended..."))

    def updateHealth(self, attack):
        self.health -= attack
        if self.health <= 0:
            self.alive = False

    def draw(self, window):
        health = "Health: " + str(self.health)
        label = font.render(health, 1, (0,255,0,))
        
        # Center the image
        size_x, size_y = window.get_size()
        image_size_x, image_size_y = encounter.image.get_size()
        
        window.blit(encounter.image, (size_x/2-image_size_x/2, size_y/2-image_size_y/2-100))
        window.blit(label, (size_x/2-image_size_x/2, size_y/2-image_size_y/2-100))
    

class other():
    def __init__(self, name, message):
        self.name = name
        self.message = message
        print name, message


encounters = [encounter("elephant", "Monster", 100, 5, 10), encounter("dragon", "Dragon", 300, 20, 20), encounter("monster", "Monster", 200, 20, 20)]

players = [player("Player1", "Guy1", 0, 100, 20, 10), player("Player2","Guy2", 1, 100, 5, 10)]

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Mizzou Game")

# create GUI object
gui = Renderer()
gui.screen = window

# create page label
lbl = Label('Pygame GUI Test Page - Ocemp')
lbl.position = 29, 13
gui.add_widget(lbl)


whiteColor = pygame.Color(255,255,255)


encounter = None
yourTurn = True

mouseX = 800
mouseY = 800

while True:
    # Close the window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if yourTurn:
                players[0].doTurn(mouseX, mouseY, encounter)
            else:
                encounter.doTurn()
    
    window.fill(whiteColor)

    
    # Get next random encounter once encounter becomes None
    if(encounter == None):
        encounter = encounters[randint(0,len(encounters)-1)]

    elif encounter.alive == False:
        encounter = None

    # Display current encounter
    else:
        
        encounter.draw(window)
        
        for player in players:
            player.draw(window)

        for s in log:
            s.update()
            s.draw(window)
            if s.time <= 0:
                log.remove(s)
            

    gui.update()
    gui.draw(window)

            
        

    pygame.display.update()

    


