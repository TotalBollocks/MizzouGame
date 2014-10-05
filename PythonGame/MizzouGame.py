import pygame, sys
#import ocempgui.access
from random import randint
from pygame.locals import *
import time
import math


#For gui
#from pgu import gui
#from pgu import html

pygame.init()
fpsClock = pygame.time.Clock()

font = pygame.font.SysFont("monospace", 15)

log = []

class logFile():
    def __init__(self, message):
        self.message = message
        
    def draw(self, window, x, y):
        logString = font.render(self.message, 1, (255,0,0,))
        window.blit(logString, (x, y))
        
        
class player():
    def __init__(self, image, name, idNumber, weapon, armor, health):

        self.name = name
        self.idNumber = idNumber

        #Weapon is a number right now. Implemented later.
        self.weapon = weapon

        #Armor is a number right now. Implemented later.
        self.armor = armor

        #New stats
        self.Str = randint(3,9)
        self.Skl = randint(3,9)
        self.Ini = randint(3,9)
        self.Dex = randint(3,9)
        self.Int = randint(3,9)
        self.Spr = randint(3,9)
        self.Tgh = randint(3,9)
        self.Lck = randint(3,9)

        #Defense is now the TOTAL from armor and Tgh.
        self.defense = (math.floor(self.Tgh/2) + self.armor)

        #Attack is now the Total from weapon and Str.
        self.attack = self.Str + self.weapon

        #Health is calculated from Tgh plus whatever the base(health) is
        self.health = health + self.Tgh

        self.alive = True
        
        self.x = 100
        self.y = 300

        if self.idNumber == 1:
            self.x = 600
            
        self.image = pygame.image.load(image + '.png')
        self.button1 = pygame.image.load('attack.png')
        self.button2 = pygame.image.load('defend.png')
        self.healthImage =  pygame.image.load('healthBar.png')
        self.manaImage =  pygame.image.load('manaBar.png')

        self.imageRect = Rect(self.x, self.y, self.image.get_rect().w, self.image.get_rect().h)
        self.button1Rect = Rect(self.x, self.y+120, self.button1.get_rect().w, self.button1.get_rect().h)
        self.button2Rect = Rect(self.x, self.y+190, self.button2.get_rect().w, self.button2.get_rect().h)
        self.healthRect = Rect(self.x+120, self.y+71, self.healthImage.get_rect().w, self.healthImage.get_rect().h)
        self.healthAmount = Rect(self.x+122, self.y+73, self.healthImage.get_rect().w-4, self.healthImage.get_rect().h-4)
        self.manaRect = Rect(self.x+120, self.y+25+70, self.manaImage.get_rect().w, self.manaImage.get_rect().h)
        self.manaAmount = Rect(self.x+122, self.y+25+72, self.manaImage.get_rect().w-4, self.manaImage.get_rect().h-4)
        
    def updateHealth(self, attack):
        if self.health <= 0:
            self.health = 0
            self.healthAmount.width = 0
            self.alive = False
        else:
            self.health -= attack
            self.healthAmount.width -= attack

    def updateMana(self, attack):
        self.mana -= attack
        self.manaAmount.width-=attack
            
    # mouse x and y
    def doTurn(self, x, y, enemy):

        if(self.imageRect.collidepoint(x, y)):
            print "player clicked"
        elif(self.button1Rect.collidepoint(x, y)):
            #self.updateHealth(self.attack)
            enemy.getAttacked(self.attack)
        elif(self.button2Rect.collidepoint(x, y)):
            enemy.getDefend(self.defense)
        

    def draw(self, window):
        window.blit(self.image, self.imageRect)
        window.blit(self.button1, self.button1Rect)
        window.blit(self.button2, self.button2Rect)
        window.blit(self.healthImage, self.healthRect)
        window.blit(self.manaImage, self.manaRect)
        pygame.draw.rect(window, (255,0,0), self.healthAmount)
        pygame.draw.rect(window, (0,0,255), self.manaAmount)
        #pygame.draw.rect(window, (255,0,0), self.button1Rect)


class encounter():
    def __init__(self, image, name, weapon, armor, health):

        self.x = 50
        self.y = 50

        self.image = pygame.image.load(image + '.png')
        self.imageRect = Rect(self.x+20, self.y+20, self.image.get_rect().w, self.image.get_rect().h)
        
        self.backgroundImage = pygame.image.load('background.png')
        self.backgroundRect = Rect(self.x, self.y, self.backgroundImage.get_rect().w, self.backgroundImage.get_rect().h)

        self.healthImage =  pygame.image.load('healthBar.png')

        self.healthRect = Rect(self.x+70, self.y+5, self.healthImage.get_rect().w, self.healthImage.get_rect().h)
        self.healthText = Rect(self.x+8, self.y+5, self.healthImage.get_rect().w, self.healthImage.get_rect().h)
        self.healthAmount = Rect(self.x+72, self.y+7, self.healthImage.get_rect().w-4, self.healthImage.get_rect().h-4)

        self.name = name
        self.idNumber = 0

        #Weapon is a number right now. Implemented later.
        self.weapon = weapon = 2

        #Armor is a number right now. Implemented later.
        self.armor = armor

        #New stats
        self.Str = randint(3,9)
        self.Skl = randint(3,9)
        self.Ini = randint(3,9)
        self.Dex = randint(3,9)
        self.Int = randint(3,9)
        self.Spr = randint(3,9)
        self.Tgh = randint(3,9)
        self.Lck = randint(3,9)

        #Defense is now the TOTAL from armor and Tgh.
        self.defense = (math.floor(self.Tgh/2) + self.armor)

        #Attack is now the Total from weapon and Str.
        self.attack = self.Str + self.weapon

        #Health is calculated from Tgh plus whatever the base(health) is
        self.health = health + self.Tgh

        self.alive = True

    def doTurn(self, player):
        player.updateHealth(self.attack)
        log.insert(0, logFile(self.name+" attacked for a damage of: " + str(self.attack)))

    def getAttacked(self, attackValue):
        self.health-=attackValue
        if self.health <= 0:
            self.alive = False;
        else:
            log.insert(0, logFile("player attacked for a damage of: " + str(attackValue)))

    def getDefend(self, defendValue):
        log.insert(0, logFile("player defended..."))

    def updateHealth(self, attack):
        self.health -= attack
        if self.health <= 0:
            self.alive = False

    def draw(self, window):
        health = "Health: " + str(self.health)
        label = font.render(health, 1, (0,255,0,))
        
        # Center the image
        backgroundImage_size_x, backgroundImage_size_y = self.backgroundImage.get_size()
        image_size_x, image_size_y = self.image.get_size()
        

        window.blit(self.backgroundImage, self.backgroundRect)
        window.blit(self.image, (self.x+backgroundImage_size_x/2-(image_size_x/2), self.y+backgroundImage_size_y/2-(image_size_y/2)))

        window.blit(self.healthImage, self.healthRect)
        pygame.draw.rect(window, (255,0,0), self.healthAmount)   
        
        #window.blit(self.image, (size_x/2-image_size_x/2, size_y/2-image_size_y/2-100))
        window.blit(label, (self.healthText))
    

class other():
    def __init__(self, name, message):
        self.name = name
        self.message = message
        print name, message



#CREATING AN ACTUAL ENCOUNTER
encounters = [encounter("elephant", "Monster", 100, 5, 10), encounter("dragon", "Dragon", 300, 20, 20), encounter("monster", "Monster", 200, 20, 20)]

players = [player("Player1", "Guy1", 0, 5, 2, 20), player("Player2","Guy2", 1, 5, 2, 20)]


def main():

    window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mizzou Game")

    whiteColor = pygame.Color(255,255,255)

    # GUI stuff..............................
    #app = gui.App()
    #def i_disable(value):
    #    item.disabled = False
        #item.blur()
        #item.chsize()
    #c = gui.Container(width=240,height=120)
    #spacer = gui.Spacer(240,220)
    #item = gui.ScrollArea(spacer,height=120)
    #item.connect(gui.CLICK,i_disable,None)
    #c.add(item,500,400)
    #app.init(c)
    #app.run(c)
    #.........................................

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
                    encounter.doTurn(players[randint(0,len(players)-1)])

        
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

        # Display the log ------------------------
            i = 0
            for s in log:
                i+=1
                if i <= 10:
                    s.draw(window, 670, 50+12*i)
        # ----------------------------------------
         
        pygame.display.update()


main()
