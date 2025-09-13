import pygame, random
#1. Spiel initializieren.
pygame.init()
#image importieren
puzzleImage = pygame.image.load("puzzle.png")
puzzleSize = puzzleImage.get_size()
#puzzle teilen.

iNum, jNum = 4,4
puzzleList = []
puzzleListInit = []
for i in range(iNum):
    tempList = []
    tempListInit = []
    for j in range(jNum): 
        w, h = puzzleSize[0]//iNum, puzzleSize[1]//jNum
        x, y = i*w, j*h
        partImage = puzzleImage.subsurface((x,y,w,h))
        tempDict = {
            "num" : j*jNum+i+1,
            "image" : partImage,
            "pos" : (x,y)
        }

        tempList.append(tempDict)
        tempListInit.append(j*jNum+i+1)
    puzzleList.append(tempList)
    puzzleListInit.append(tempListInit)
puzzleList[-1][-1]["num"] = 0
puzzleListInit[-1][-1] = 0
bs = pygame.Surface((w,h))
bs.fill((0,0,0))
puzzleList[-1][-1]["image"] = bs


#2. Fenster Option 
size = (puzzleSize)
screen = pygame.display.set_mode(size)
title = "puzzle"
pygame.display.set_caption(title)

#3. Spiel Option
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
dirDict ={
    "left" : (-1,0), "right" : (1,0), "up" : (0,-1), "down" : (0,1) 
}
keyPress = False
mix = False
gameOver = False
spaceNum = 0
exit = False

#4. main Event
while not exit:
    #4.1 FPS setting
    clock.tick(60)
    #4.2. Eingabe 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            keyName = pygame.key.name(event.key)
            if keyName == "space": 
                mix = not mix
                spaceNum +=1
            for key in dirDict.keys():
                if key == keyName:
                    keyPress = True

    #4.3 Eingabeänderung, Zeitänderung
    #Black suchen
    blank = None
    for i in range(iNum):
     for j in range(jNum):
        if puzzleList[i][j]["num"] == 0:
            blank = (i,j)
    #Blank Ändern  
    if keyPress == True or mix == True:
        if mix == True:
            ranIndex = random.randrange(0,4)
            keyName = list(dirDict.keys())[ranIndex]
        i, j = blank
        ii, jj = dirDict[keyName]
        iNew, jNew = i+ii, j+jj
        if iNew>= 0 and iNew < iNum and jNew>= 0 and jNew < jNum:
            puzzleList[i][j]["num"], puzzleList[iNew][jNew]["num"] = \
                puzzleList[iNew][jNew]["num"], puzzleList[i][j]["num"]
            puzzleList[i][j]["image"], puzzleList[iNew][jNew]["image"] = \
                puzzleList[iNew][jNew]["image"], puzzleList[i][j]["image"]
        keyPress = False
    same = True
    #spiel ende option
    if spaceNum >= 2:
        for i in range(iNum):
         for j in range(jNum):
            if puzzleList[i][j]["num"] != puzzleListInit[i][j]:
                same = False
        if same == True:
            gameOver = True
    #4.4 zeichnen
    screen.fill(white)
    #puzzle zeichnen
    for i in range(iNum):
        for j in range(jNum):
            img = puzzleList[i][j]["image"]
            pos = puzzleList[i][j]["pos"]
            screen.blit(img,pos)
            x,y = pos
            # Grenzlinie
            A = (x, y)
            B = (x+w,y)
            C = (x, y+h)
            D = (x+w, y+h)

            pygame.draw.line(screen, white,A,B,3)
            pygame.draw.line(screen, white,A,C,3)
            pygame.draw.line(screen, white,D,B,3)
            pygame.draw.line(screen, white,D,C,3)
    
    if gameOver == True:
        screen.blit(puzzleImage,(0,0))
    #4.5. Update
    pygame.display.flip()
#5. Spiel ende
pygame.quit()