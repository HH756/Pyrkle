import hashlib
numNodes = 4
x = 0
y = 0
hasher = hashlib.md5()
hss = []
while x < numNodes:
    with open(str(x)+'.txt','rb') as f:
        buf = f.read()
        hasher.update(buf)
        Cnode = hasher.hexdigest() 
        hss.append(Cnode)
    x += 1
print(hss)
hssLen = len(hss)
hssFirstHalf = hss[:len(hss)//2]
hssHalf = hssLen/2
hssLastHalf = []
while hssHalf > y: 
    hssfirstHalfplur = hss[int(hssHalf+y)]
    y += 1
    hssLastHalf.append(hssfirstHalfplur)
print(hssFirstHalf)
print(hssLastHalf)

# Needs to be a function that accepts an Array of interative file names