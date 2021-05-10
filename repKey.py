import binascii
freq = {'e':12.07,'t':9.1, 'a':8.12, 'o':7.68, 'i':7.31, 'n':6.95, 's':6.28,'r':6.02,'h':5.92,'d':4.32,'l':3.98,
        'u':2.88,'c':2.71,'m':2.61,'f':2.3,'y':2.11,'w':2.09,'g':2.03,'p':1.82,'b':1.49,'v':1.11,'k':0.69,'x':0.17,
        'q':0.11,'j':0.1,'z':.07,' ':5}


def hammingDist(x,y):
    cnt=0
    for b in range(len(x)):
        for i in range(8):
            if getBit(x[b],i) !=getBit(y[b],i):
                cnt+=1
    return cnt


def getBit(x,n):
    return(x & (0x01 <<n))

s1=bytearray("this is a test","ascii")
s2=bytearray("wokka wokka!!!","ascii")
def findLen(barr):
    probKeySize=[]
    lastSize=hammingDist(barr[0:2],barr[2:4])
    probKeySize.append(2)
    for keySize in range(3,40):
       if( ((hammingDist(barr[0:keySize],barr[2*keySize:3*keySize]))/keySize+ (hammingDist(barr[2*keySize:3*keySize],barr[3*keySize:4*keySize]))/keySize)/2 <= lastSize):
            lastSize= ((hammingDist(barr[0:keySize],barr[3*keySize:4*keySize]))/keySize+ (hammingDist(barr[2*keySize:3*keySize],barr[3*keySize:4*keySize]))/keySize)/2
            probKeySize.append(keySize)
    return probKeySize
def blocks(keySize,data):
    blocks=bytearray()
    key=[]
    #print(keySize)
    blockSize=(len(data)//keySize)
    print(len(data)/keySize)
    for j in range(keySize):
        for i in range(blockSize):
            #a=range(len(data[i*(len(data)//keySize):(i+1)*(len(data)//keySize)]))
            blocks.append(data[i*keySize +j])

        key.append(XOR(blocks))
        blocks.clear()

    return key

def XOR(data):
    r=bytearray(len(data))
    print(len(data))
    largest=0

    key=0
    for i in range(128):
        sum=0
        for j in range(len(data)):

            r[j]=data[j]^i
        for j in range(len(data)):
            if(r[j: j+1].isalpha()):
                sum+=freq[r[j: j+1].decode('utf-8').lower()]
        #sum= rate(r)
        if(sum> largest):
            largest= sum
            key=i
    return key

if __name__ == "__main__":
    with open("decoded.txt", "r") as bFile:
        data=bFile.read()
        data=binascii.a2b_base64(data)
        prbKeys=findLen(data)
        print(hammingDist(s1,s2))

        str=bytearray()
        for key in prbKeys:

            possibleKey=blocks(key,data)
            for i in range(len(data)):
                str.append(data[i] ^possibleKey[i%(key)])
            print(str.decode("utf-8"))
            str.clear()






#print(hammingDist(s1,s2))