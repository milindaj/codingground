N = input()
K = input()
S = str(input())
assert 1 <= N <= 10**6
assert 1 <= K <= 10**6

#print(bool(S))
lenT = len(S)


b = S[lenT-1] #-48
newS = str(b)

b = int(b) ^ int(S[lenT-2]) #-48)
newS = str(b) + newS

for i in range(lenT-3, N-K-1, -1):
    lenS = len(newS)
    bb = newS[lenS-1]
    for j in range(lenS-2, -1, -1):
        bb = int(bb)^int(newS[j])
    b = int(S[i])^int(bb)
    newS = str(b) + newS

print(newS)

#ans5 = int(ans4) ^ (arr[lenT-5]-48)
#print(ans5)

#print(toggleBit(int(S[lenT-1]),0))
