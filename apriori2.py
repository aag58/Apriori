import sys
import itertools

minSupport = float(input('Enter min support in %: '))/100
minConfidence = float(input('Enter min confidence in %: '))/100
# minSupport = 0.5
# minConfidence = 0.5
frequentItemset = []
datafile = sys.argv[1]
dataMap={}
mapping={}

def support(itemSet):
    count=0
    for i in dataMap:
        flag = True
        for j in itemSet:
            if j not in dataMap[i]:
                flag=False
        if(flag):
            count+=1
    return(count/len(dataMap))

def confidence(left, S):
    return support(S)/support(left)

def findsubsets(S,m):
    return list(set(itertools.combinations(S, m)))

def PrintAssociations(S):
    leftpart=[]
    rightpart=[]
    m=len(S)-1
    while m>=1:
        se = findsubsets(S, m)
        for i in se:
                leftpart=list(i)
                rightpart=list(set(S).difference(set(i)))
                if confidence(leftpart,S)>=minConfidence:
                    lp=[]
                    rp=[]
                    for i in leftpart:
                        lp.append(items[i-1])
                    for i in rightpart:
                        rp.append(items[i-1])
                    print(lp,rp,sep='-->')
                    # print(leftpart,rightpart,sep='-->')
        m=m-1

def candidates(L):
    k=len(L[1])
    l=[]
    if len(L[1])==1:
        for i in range(0,len(L)):
            for j in range(i+1,len(L)):
                x=(list(set().union(L[j],L[i])))
                l.append(x)
    if len(L[1])>1:
        for i in range(0,len(L)):
            for j in range(i+1,len(L)):
                if L[i][0:k-1]==L[j][0:k-1]:
                    x=(list(set().union(L[j],L[i])))
                    l.append(x)
    return(l)
# --------------------------------------------------------------------------------------

cnt=1
f = open(datafile, 'r')
l=f.readline()
while(l!=''):
    a=l.split()
    if a[1] not in mapping:
        mapping[a[1]] = cnt
        cnt+=1
    l=f.readline()
# print(mapping)

f = open(datafile, 'r')
l=f.readline()
while(l!=''):
    a=l.split()
    if a[0] not in dataMap:
        dataMap[a[0]] = []
    dataMap[a[0]].append(mapping[a[1]])
    l=f.readline()

# print(dataMap)
# --------------------------------------------------------------------------------------
c=[]
L=[]
for i in dataMap:
    for j in dataMap[i]:
        if j not in c:
            c.append(j)

temp=[]
for i in c:
    temp.append(i)
    if support(temp) >= minSupport:
        L.append(temp)
    temp=[]

for i in L:
    frequentItemset.append(i)

# --------------------------------------------------------------------------------------

while len(L)>1:
    C=candidates(L)
    L=[]
    for i in C:
        if support(i)>=minSupport:
            L.append(i)
    for i in L:
        frequentItemset.append(i)

# print(frequentItemset)

# --------------------------------------------------------------------------------------
items=[]
for keys in mapping:
    items.append(keys)
# print('Items --> ',items)

print('-----------------------------------------------------------')
print('Frequent Item Set:')
print('-----------------------------------------------------------')
for i in frequentItemset:
    print('Support:',support(i),'|', end=' ')
    for j in i:
        print(items[j-1],end=' ')
    print()
print('-----------------------------------------------------------')
print('Associations with confidence greater than', minConfidence)
print('-----------------------------------------------------------')

for i in frequentItemset:
    if len(i)>1:
        PrintAssociations(i)