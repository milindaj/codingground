def placeBox(boxCount, boxPositions, availableBoxes):
    if boxCount == totalBoxes: # placed all the boxes, return
            positionList.append(boxPositions)
            return None
    
    #we have 3 options for placing the boxes, place on floor, place on top of another box
    for i in range(1, 3):
        if i == 1: # position on floor
            boxPositions[boxCount] = "F"
            availableBoxes.append({boxCount, boxes[boxCount]*boxes[boxCount], boxes[boxCount]*boxes[boxCount]})
            boxCount = boxCount + 1
            placeBox(boxCount, boxPositions, availableBoxes)
        else:
            for i in range(0, len(availableBoxes)): # check if the current box can be placed on top of any of the available boxes
                avBox = availableBoxes[i]
                if (avBox[2] >= boxes[boxCount]*boxes[boxCount]): # this box fits, place it
                    avBox[2] = avBox[2] - boxes[boxCount]*boxes[boxCount] # reduce the available area on the box on which you are stacking
                    availableBoxes[i] = avBox
                    # add a new box
                    availableBoxes.append({boxCount,boxes[boxCount]*boxes[boxCount], boxes[boxCount]*boxes[boxCount]})
                    boxPositions[boxCount] = avBox[0] # add the position of box which is being placed
                    # call for next box placement
                    boxCount = boxCount + 1
                    placeBox(boxCount, boxPositions, availableBoxes)
                enif                    

inputData = "4 2 1 4 2"

boxes = [int(bx) for bx in inputData.split(" ")]
totalBoxes = len(boxes)

boxPositions = dict() # will contain things such as "F" for floor and box number for box

availableBoxes = [] #boxes whos top area is available for stacking box#, total area, occupied area

# put first box on flooor
boxPositions[1] = "F"
availableBoxes.append({0, boxes[0]*boxes[0], boxes[0]*boxes[0]})
positionList = []
placeBox(1, boxPositions, availableBoxes)
print(positionList)