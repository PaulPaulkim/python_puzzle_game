## puzzleList create
#iNum Horizontal jNum Vertical
iNum, jNum = 4,4
puzzleList = []
for i in range(iNum):
    tempList = []
    for j in range(jNum): 
        tempList.append(j*jNum+i+1)
    puzzleList.append(tempList)
puzzleList[-1][-1] = 0


##puzzleList show
def puzzleShow():
    textTemp = ""
    for j in range(jNum):
        for i in range(iNum):
            textTemp += str(puzzleList[i][j]) + "\t"
        textTemp += '\n'
    print(textTemp)

#find blank
blank = None
for i in range(iNum):
    for j in range(jNum):
        if puzzleList[i][j] == 0:
            blank = (i,j)

dirDict ={
    "left" : (-1,0), "right" : (1,0), "up" : (0,-1), "down" : (0,1) 
}
i, j = blank
ii, jj = dirDict["right"]
iNew, jNew = i+ii, j+jj

if iNew>= 0 and iNew < iNum and jNew>= 0 and jNew < jNum:
    puzzleList[i][j], puzzleList[iNew][jNew] = \
        puzzleList[iNew][jNew], puzzleList[i][j]
puzzleShow()
