#!/usr/bin/python

#!/usr/bin/python

#!/usr/bin/python

inputData = "6#3,4,5,7,8,9#3,4,5,7,8,5"

split = inputData.split('#')
num = int(split[0])
mins = [int(mn) for mn in split[1].split(",")]
maxs = [int(mx) for mx in split[2].split(",")]

loopEnd = (num - (num/2 - 2))
nRange = num/2 -1
#print(inputData)
#print("\n")
print(mins)
#print("\n")
print(maxs)
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

tempScoreDiff1 = 0
tempScoreDiff2 = 0
scoreList1 = []
scoreList2 = []

for n in range(0, len(finalTeam1)):
    tempTeam1ScoreHigh = 0
    tempTeam1ScoreLow = 0
    tempTeam2ScoreHigh = 0
    tempTeam2ScoreLow = 0

    t1 = finalTeam1[n]
    for x in t1:
        print("# " + str(x) + " score = " + str(maxs[x-1]))
        tempTeam1ScoreHigh = tempTeam1ScoreHigh + maxs[x-1]
        tempTeam1ScoreLow = tempTeam1ScoreLow + mins[x-1]        

    print("tempTeam1ScoreHigh  " + str(tempTeam1ScoreHigh))
    t2 = finalTeam2[n]
    for y in t2:
        print("# " + str(y) + " score2 = " + str(mins[y-1]))
        tempTeam2ScoreHigh = tempTeam2ScoreHigh + maxs[y-1]
        tempTeam2ScoreLow = tempTeam2ScoreLow + mins[y-1]      
    
    print("tempTeam2ScoreLow  " + str(tempTeam2ScoreLow))
    
    tempScoreDiff1 = abs(tempTeam1ScoreHigh - tempTeam2ScoreLow)
    tempScoreDiff2 = abs(tempTeam2ScoreHigh - tempTeam1ScoreLow)
    scoreList1.append(tempScoreDiff1)
    scoreList2.append(tempScoreDiff2)
    
#bestScorePos = scoreList.index(min(scoreList))

#print("And the winning team combination is ...")
#print(finalTeam1[bestScorePos])
#print(finalTeam2[bestScorePos])
print(scoreList1)
print(scoreList2)
print(min(scoreList1))
print(min(scoreList2))
