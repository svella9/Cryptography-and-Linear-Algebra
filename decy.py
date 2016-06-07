import numpy as np
from numpy.linalg import inv

a = []
cipher = np.array([[-3,-3,-4],[0,1,1],[4,3,4]])
filename = input("Enter the filename  ")
f = open(filename)
       
s = ''

for line in f:
        line = line.strip()
        words = line.split()
        for word in words:
                a.append(int(word))

inv_cipher = inv(cipher)
data = np.array(a)
data  = data.reshape(3,len(a)//3)

decry = np.dot(inv_cipher,data)
decry = np.array(decry).flatten().tolist()

for i in decry:
        s = s + chr(int(i))

f = open("Decryp.txt","w")
f.write(s)

