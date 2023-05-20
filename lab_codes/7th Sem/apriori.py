from collections import Counter
from itertools import combinations

dataset = [
        ['T100',['I1','I3','I4']],
        ['T200',['I2','I3','I5']],
        ['T300',['I1','I2','I3','I5']],
        ['T400',['I2','I5']],
]

values = []
for i in dataset:
    for q in i[1]:
        if(q not in values):
            values.append(q)

values = sorted(values)
print("Unique Values")
print(values)

minimumSupport = 2
confidence = 0.8

# candidate set
c = Counter()

for i in values:
    for d in dataset:
        if(i in d[1]):
            c[i]+=1
print("C1:")

for i in c:
    print(str([i])+": "+str(c[i]))
print()

# item set
l = Counter()

for i in c:
    if(c[i] >= minimumSupport):
        l[frozenset([i])]+=c[i]

print("L1:")
for i in l:
    print(str(list(i))+": "+str(l[i]))
print()

pl = l
pos = 1

for count in range (2,300):
    nc = set()
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union(temp[j])
            if(len(t) == count):
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i] = 0
        for q in dataset:
            temp = set(q[1])
            if(i.issubset(temp)):
                c[i]+=1
    print("C"+str(count)+":")
    for i in c:
        print(str(list(i))+": "+str(c[i]))
    print()
    l = Counter()
    for i in c:
        if(c[i] >= minimumSupport):
            l[i]+=c[i]
    print("L"+str(count)+":")
    for i in l:
        print(str(list(i))+": "+str(l[i]))
    print()
    if(len(l) == 0):
        break
    pl = l
    pos = count

print("Result: ")
print("L"+str(pos)+":")
for i in pl:
    print(str(list(i))+": "+str(pl[i]))
print()

# Association Rules
for l in pl:
    c = [frozenset(q) for q in combinations(l,len(l)-1)]
    mmax = 0
    for a in c:
        b = l-a
        ab = l
        # subsets
        sab = 0
        sa = 0
        sb = 0
        for q in dataset:
            temp = set(q[1])
            if(a.issubset(temp)):
                sa+=1
            if(b.issubset(temp)):
                sb+=1
            if(ab.issubset(temp)):
                sab+=1
        temp = sab/sa*100
        if(temp > mmax):
            mmax = temp
        temp = sab/sb*100
        if(temp > mmax):
            mmax = temp
        print(str(list(a))+" -> "+str(list(b))+" = "+str(sab/sa*100)+"%")
        print(str(list(b))+" -> "+str(list(a))+" = "+str(sab/sb*100)+"%")
    curr = 1
    print("choosing:", end=' ')
    for a in c:
        b = l-a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        for q in dataset:
            temp = set(q[1])
            if(a.issubset(temp)):
                sa+=1
            if(b.issubset(temp)):
                sb+=1
            if(ab.issubset(temp)):
                sab+=1
        temp = sab/sa*100
        if(temp == mmax):
            print(curr, end = ' ')
        curr += 1
        temp = sab/sb*100
        if(temp == mmax):
            print(curr, end = ' ')
        curr += 1
    print()
    print()
