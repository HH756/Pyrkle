import hashlib
import os 
# Hash files, create layer 1
filenumber = 0
hasher = hashlib.md5()
layer = []
for x in os.listdir("./"):
    if x.endswith(".mtip"):
        filenumber += 1
        print(x)
        with open(str(x),'rb') as f:
            buf = f.read()
            hasher.update(buf)
            node = hasher.hexdigest()
            layer.append(node)
    else:
        exit
print("Attemping to hash "+str(len(layer))+' base files')
print(layer)
print('Successfully Hashed '+str(filenumber)+' base files')
# Create Layer 2
workingL = []
count = 1
count2 = 0
if len(workingL) == 0:
    for x in layer:
        if count < len(layer):
            workingL.append(layer[count2]+layer[count])
        else:
            print('index failure')
        count +=2 
        count2 +=2
    if ((len(layer))%2)!=0:
        workingL.append(layer[-1])
    print(workingL)
# Hash layer 2
for xp in workingL:
    if (len(xp)) == 64:
        print('true')
        buf = xp.encode()
        hasher.update(buf)
        nodae = hasher.hexdigest()
        workingL.append(nodae)
    else:
        exit
print(workingL)