

def toggleBit(int_type, offset):
  mask = 1 << offset
  return(int_type ^ mask)

N = input()
K = input()
S = str(input())
assert 1 <= N <= 10**6
assert 1 <= K <= 10**6



#print(bool(S))
lenT = len(S)

#arr=bytearray(S)

b = S[lenT-1] #-48
newS = str(b)

b = int(b) ^ int(S[lenT-2]) #-48)
newS = str(b) + newS
x = 0
for i in range(lenT-3, N-K-1, -1):
    lenS = len(newS)
    if lenS<(K-1):
        bb = int(newS[lenS-1])
        for j in range(lenS-2, -1, -1):
            bb = bb^int(newS[j])
        b = int(S[i])^int(bb)
        newS = str(b) + newS
    elif lenS < N:

        bb = int(newS[lenS-1-x])
        for j in range(lenS-2-x, (lenS-1-x-K), -1):
            bb = bb^int(newS[j])
        b = int(S[i])^int(bb)
        newS = str(b) + newS
        x = x + 1

print(newS)

#ans5 = int(ans4) ^ (arr[lenT-5]-48)
#print(ans5)

#print(toggleBit(int(S[lenT-1]),0))
