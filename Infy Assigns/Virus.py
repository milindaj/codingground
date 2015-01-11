# Hello World program in Python
    
print "Hello World!\n"
#input = "90 120 Infected,90 150 NotInfected,100 140 Infected,80 130 NotInfected#95 125,95 145,75 160"
input = "80 120 Infected,70 145 Infected,90 100 Infected,80 150 NotInfected,80 80 NotInfected,100 120 NotInfected#120 148,75 148,60 90"

split = input.split('#')

catVals = split[0].split(",")
#catVals = [int(cat) for cat in catVals]

trvVals = split[1].split(",")
#trvVals = [int(trv) for trv in trvVals]

#inpArray = dict()

inTempList = [] #infected temp
inPrsList = [] # infected pressure

unTempList = [] # uninfected temp
unPrsList = [] # uninfected pressure

for cat in catVals:
    catTmp = cat.split(" ")
    if catTmp[2] == "Infected":
        inTempList.append(int(catTmp[0]))
        inPrsList.append(int(catTmp[1]))
    else:    
        unTempList.append(int(catTmp[0]))
        unPrsList.append(int(catTmp[1]))
    

inTempList.sort()
inPrsList.sort() 
unTempList.sort()
unPrsList.sort()
tmpRangeType = ""
prsRangeType = ""
rangeType = ""

if inTempList[0] < unTempList[0]:
    tmpRangeType = "Infected"
elif inTempList[0] > unTempList[0]:
    tmpRangeType = "NotInfected"
    
if inPrsList[len(inPrsList)-1] > unPrsList[len(unPrsList)-1]:
    prsRangeType = "Infected"
elif inPrsList[len(inPrsList)-1] < unPrsList[len(unPrsList)-1]:
    prsRangeType = "NotInfected"    
    
if tmpRangeType == prsRangeType:
    rangeType = prsRangeType
else:
    rangeType = "Unknown"
    
print( "range type is :" + rangeType)    
ansList = []
for trv in trvVals:
    trvTmp = trv.split(" ")
    tmp = int(trvTmp[0])
    prs = int(trvTmp[1])
    
    if (tmp >= inTempList[0] and tmp <= inTempList[len(inTempList)-1]) and (prs >= inPrsList[0] and prs <= inPrsList[len(inPrsList)-1]):
        ansList.append("Infected")
    elif (tmp >= unTempList[0] and tmp <= unTempList[len(unTempList)-1]) and (prs >= unPrsList[0] and prs <= unPrsList[len(unPrsList)-1]):
        ansList.append("Notinfected")          
    else:
        if rangeType != "Unknown":
            if rangeType == "Infected":
                if tmp < inTempList[0] and prs > inPrsList[len(inTempList)-1]:
                    ansList.append("Infected")
                else:     
                    ansList.append("Unknown")
            else:
                if tmp < unTempList[0] and prs > unPrsList[len(unTempList)-1]:
                    ansList.append("Notinfected")
                else:
                    ansList.append("Unknown")
        else:
            ansList.append("Unknown")       

print(catVals)
print(trvVals)
print("\n")

print("infected List :")
print(inTempList)
print(inPrsList)
print("\n")

print("Not infected List :")
print(unTempList)
print(unPrsList)
print("\n")

print(ansList)
