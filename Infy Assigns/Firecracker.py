def placeBox(boxCount, boxPositions, availableBoxes):
    if boxCount == totalBoxes: # placed all the boxes, return
        positionList.append(boxPositions)
        print(" RETURNING .... ")
        print(boxPositions)
        print(availableBoxes)
        return None
    else:
        #we have 3 options for placing the boxes, place on floor, place on top of another box
        for n in range(1, 3):
            if n == 1: # position on floor
                boxPositions[boxCount] = "F"
                temp = []
                temp.append(boxCount)
                temp.append(boxes[boxCount]*boxes[boxCount])
                temp.append(boxes[boxCount]*boxes[boxCount])
                availableBoxes.append(temp)
                
                boxCount = boxCount + 1
                print("calling place Box, Box Count = " + str(boxCount))
                placeBox(boxCount, boxPositions, availableBoxes)
                print(" boxCount after call to placebox = " + str(boxCount))
                if boxCount == totalBoxes:
                    return None
            else:
                for i in range(0, len(availableBoxes)): # check if the current box can be placed on top of any of the available boxes
                    avBox = availableBoxes[i]
                    print("current count = " + str(boxCount) + " " + str(avBox[2]))
                    if (avBox[2] >= boxes[boxCount]*boxes[boxCount]): # this box fits, place it
                        avBox[2] = avBox[2] - boxes[boxCount]*boxes[boxCount] # reduce the available area on the box on which you are stacking
                        availableBoxes[i] = avBox
                        # add a new box
                        temp = []
                        temp.append(boxCount)
                        temp.append(boxes[boxCount]*boxes[boxCount])
                        temp.append(boxes[boxCount]*boxes[boxCount])
                        availableBoxes.append(temp)                    
                        boxPositions[boxCount] = avBox[0] # add the position of box which is being placed
                        # call for next box placement
                        boxCount = boxCount + 1
                        placeBox(boxCount, boxPositions, availableBoxes)
                        if boxCount == totalBoxes:
                            return None                        

inputData = "4 2 1 4 2"

boxes = [int(bx) for bx in inputData.split(" ")]
totalBoxes = len(boxes)
print("total boxes = " + str(totalBoxes))
boxPositions = dict() # will contain things such as "F" for floor and box number for box

availableBoxes = [] #boxes whos top area is available for stacking box#, total area, occupied area

# put first box on flooor
boxPositions[0] = "F"
temp = []
temp.append(0)
temp.append(boxes[0]*boxes[0])
temp.append(boxes[0]*boxes[0])
availableBoxes.append(temp)
positionList = []
placeBox(1, boxPositions, availableBoxes)
print("FINAL LISTING ....")
print(positionList)
