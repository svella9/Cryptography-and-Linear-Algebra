import numpy as np


a = []
filename = input("Enter the filename  ")
f = open(filename)


for ch in iter(lambda: f.read(1),''):
        a.append(ord(ch))
        
while(len(a)%3 != 0):
        a.append(32)
  
data = np.array(a)
data  = data.reshape(3,len(a)//3)
cipher = np.array([[-3,-3,-4],[0,1,1],[4,3,4]])

encrypt = np.dot(cipher,data)
np.savetxt('Encry.txt',encrypt,fmt = '%.0f')
#Encryption matrix








