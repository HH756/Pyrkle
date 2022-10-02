import hashlib
numNodes = 4
x = 0
y = 0
hasher = hashlib.sha256()
layer1Hashes = []
# Hash all given files
while x < numNodes:
    with open(str(x)+'.txt','rb') as f:
        buf = f.read()
        hasher.update(buf)
        Cnode = hasher.hexdigest() 
        layer1Hashes.append(Cnode)
    x += 1
# Getting First Half of Hashed Files
layer1HashesLength = len(layer1Hashes)
layer1HalfLength = layer1HashesLength/2
layer1FirstHalf = layer1Hashes[:len(layer1Hashes)//2]
# Getting Last Half of Hashed Files
layer1LastHalf = []
while layer1HalfLength > y: 
    layer1LastHalfHash = layer1Hashes[int(layer1HalfLength+y)]
    y += 1
    layer1LastHalf.append(layer1LastHalfHash)
# Getting layer2 of the first half of layer 1
layer1FirstHalfConcat = ''.join(layer1FirstHalf)
layer2FirstHalf1 = hashlib.sha256(layer1FirstHalfConcat.encode('utf-8')).hexdigest()
# Getting layer2 of the last half of layer 1
layer1LastHalfConcat = ''.join(layer1LastHalf)
layer2LastHalf1 = hashlib.sha256(layer1LastHalfConcat.encode('utf-8')).hexdigest()
# master node hashing
layer2Hash = ''.join([layer2FirstHalf1,layer2LastHalf1])
masternode = hashlib.sha256((''.join([layer2FirstHalf1,layer2LastHalf1])).encode('utf-8')).hexdigest()
print(masternode)

