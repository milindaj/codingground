def placeBox(boxCount, boxPositions, availableBoxes):
    print("boxCount = " + str(boxCount))
    print("boxPositions = " + str(boxPositions))
    print("availableBoxes = " + str(availableBoxes))
    if boxCount == totalBoxes: # placed all the boxes, return
        positionList.append(boxPositions)
        #print(" RETURNING .... ")
        #print(boxPositions)
        #print(availableBoxes)
        print("DONE!!!")
        return None
    else:
        nextCount = boxCount + 1
        #boxPositionsNew = dict()
        boxPositionsNew = []
        availableBoxesNew = []        
        
        #we have 2 options for placing the boxes, place on floor, place on top of another box
        for n in range(1, 3):
            if n == 1: # position on floor
                boxPositionsNew = list(boxPositions)
                availableBoxesNew = list(availableBoxes)
                boxPositionsNew.append("F")
                temp = []
                temp.append(boxCount)
                temp.append(boxes[boxCount]*boxes[boxCount])
                temp.append(boxes[boxCount]*boxes[boxCount])
                availableBoxesNew.append(temp)
                placeBox(nextCount, boxPositionsNew, availableBoxesNew)
            else:
                #print("inside if, avl box = " + str(availableBoxes))
                for i in range(0, len(availableBoxes)): # check if the current box can be placed on top of any of the available boxes
                    print("inside if, avl box = " + str(availableBoxes))
                    avBox = availableBoxes[i]
                    avBox2 = avBox[:]
                    if (avBox2[2] >= boxes[boxCount]*boxes[boxCount]): # this box fits, place it
                        avBox2[2] = avBox2[2] - boxes[boxCount]*boxes[boxCount] # reduce the available area on the box on which you are stacking
                        boxPositionsNew = list(boxPositions)
                        availableBoxesNew = list(availableBoxes)                      
                        availableBoxesNew[i] = avBox2
                        # add a new box
                        temp = []
                        temp.append(boxCount)
                        temp.append(boxes[boxCount]*boxes[boxCount])
                        temp.append(boxes[boxCount]*boxes[boxCount])
                        availableBoxesNew.append(temp)                    
                        boxPositionsNew.append(avBox2[0]) # add the position of box which is being placed
                        # call for next box placement
                        nextCount = boxCount + 1
                        placeBox(nextCount, boxPositionsNew, availableBoxesNew)

#inputData = "4 2 1 4 2"
#inputData = "4 2 1 4 2"
inputData = "4 2 1"

boxes = [int(bx) for bx in inputData.split(" ")]
totalBoxes = len(boxes)
print("total boxes = " + str(totalBoxes))
boxPositions2 = [] # will contain things such as "F" for floor and box number for box

availableBoxes2 = [] #boxes whos top area is available for stacking box#, total area, occupied area

# put first box on flooor
boxPositions2.append("F")
temp = []
temp.append(0)
temp.append(boxes[0]*boxes[0])
temp.append(boxes[0]*boxes[0])
availableBoxes2.append(temp)
positionList = []
placeBox(1, boxPositions2, availableBoxes2)
print("FINAL LISTING ....")
print(positionList)

bestCaseList = []
floorAreaList = []
for z in range(0, len(positionList)):
    subList = []
    subList = positionList[z]
    #print(subList)
    floorList = []
    floorList = [i for i,x in enumerate(subList) if x == 'F']
    #floorArea = [f*f for f in boxes if f in floorList]
    print(floorList)
    floorArea = 0
    for n in range(0, len(floorList)):
        floorArea = floorArea + boxes[floorList[n]]*boxes[floorList[n]]
    floorAreaList.append(floorArea)
#    print(floorList)
    #print("\n")
print(floorAreaList)
    
