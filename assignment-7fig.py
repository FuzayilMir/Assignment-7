import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,100)

r = np.sqrt(6.25)
R = np.sqrt(16)

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
A = np.array([-2.5,0]) 
B = np.array([0,-4]) 
O = np.array([0,0]) 
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)



fig, ax = plt.subplots(1)

ax.plot(x1,x2)
ax.set_aspect(1)

plt.xlim(-2.5,2.5)
plt.ylim(-2.5,2.5)


y1 = R*np.cos(theta)
y2 = R*np.sin(theta)

ax.plot(y1,y2)
ax.set_aspect(1)

plt.xlim(-4,4)
plt.ylim(-4,4)

plt.grid(linestyle='--')

plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')

plt.axis('equal')
plt.show()
















