inputData = "6#3,4,5,7,8,9#3,4,5,7,8,9"

split = inputData.split('#')
num = int(split[0])
mins = [int(mn) for mn in split[1].split(",")]
maxs = [int(mx) for mx in split[2].split(",")]

loopEnd = (num - (num/2 - 2))
nRange = num/2 -1
#print(inputData)
#print("\n")
#print(mins)
#print("\n")
#print(maxs)
print(num)
print(loopEnd)
print(nRange)

fullList = range(1, num+1)
finalTeam1 = []
finalTeam2 = []

tempList = []
for i in range(2, loopEnd + 1):
    roleList = []
    roleList.append(1)
    roleList.append(i)
    #print("in i *** i = " + str(i))
    for j in range(i+1, num+1): # 3 - 6
        #print("in j *** j = " + str(j))
        for n in range(1,nRange): # 1 - 1
            #print("in n *** n = " + str(n))
            #for j in range(i+1,num + 1):
            tempTeam1 = []
            tempTeam1 = roleList[:]
            tempTeam1.append(j)
        
        finalTeam1.append(tempTeam1)
        fullList = range(1, num+1)
        tempTeam2 = [x for x in fullList if x not in tempTeam1]

        #print("tempTeam2")
        #print(tempTeam2)
        finalTeam2.append(tempTeam2)
        tempTeam1 = []
        tempTeam2 = []
        #print("printed")

print("FINAL team 1")
print(finalTeam1)

print("FINAL team 2")
print(finalTeam2)

tempScoreDiff = 0
scoreList = []

for n in range(1, len(finalList1)+1):
    tempTeam1Score = 0
    tempTeam2Score = 0

    for x in finalList1:
        tempTeam1Score = tempTeam1Score + maxs[x]

    for x in finalList2:
        tempTeam2Score = tempTeam2Score + maxs[x]        
    
    tempScoreDiff = abs(tempTeam1Score - tempTeam2Score)
    scoreList.append(tempScoreDiff)
    
bestScorePos = scoreList.index(min(scoreList))

print("And the winning team combination is ...")
print(finalTeam1[bestScorePos])
print(finalTeam2[bestScorePos])


