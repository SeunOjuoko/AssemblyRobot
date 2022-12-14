#adapted by bethany livingstone  for homogeneous transformation matrix calculations of a robot arm from https://youtu.be/V6TKocmc9k8
import numpy as np # Scientific computing library
 
# For help with Denavit Hartenberg (DH) watch this video https://youtu.be/BuWMu59mfQI
#theta rotaion in Z to match x axis of links in degrees
Ta=0.0
Tb=0.0
Tc=0.0
Td=0.0

# alpha in degrees
Aa=-90.0
Ab=0.0
Ac=0.0
Ad=0.0

#r is distance between centers 
Ra=0.0
Rb=151.0
Rc=100.0
Rd=55.0

#d dispalcement
Da= 47.5
Db= 0.0
Dc= 0.0
Dd= 0.0

#creates DH matrix
DH = [[(Ta/180.0)*np.pi,(Aa/180.0)*np.pi,Ra,Da],
    [(Tb/180.0)*np.pi,(Ab/180.0)*np.pi,Rb,Db],
    [(Tc/180.0)*np.pi,(Ac/180.0)*np.pi,Rc,Dc],
    [(Td/180.0)*np.pi,(Ad/180.0)*np.pi,Rd,Dd]] 

i=0 #link number
H0_1=[[np.cos(DH[i][0]),-np.sin(DH[i][0])*np.cos(DH[i][1]),np.sin(DH[i][0])*np.sin(DH[i][1]),DH[i][2]*np.cos(DH[i][0])],
      [np.sin(DH[i][0]),np.cos(DH[i][0])*np.cos(DH[i][1]),-np.cos(DH[i][0])*np.sin(DH[i][1]),DH[1][2]*np.sin(DH[i][0])],
      [0,np.sin(DH[i][1]),np.cos(DH[i][1]),DH[i][3],],
      [0,0,0,1]]
i=1 #link number
H1_2=[[np.cos(DH[i][0]),-np.sin(DH[i][0])*np.cos(DH[i][1]),np.sin(DH[i][0])*np.sin(DH[i][1]),DH[i][2]*np.cos(DH[i][0])],
      [np.sin(DH[i][0]),np.cos(DH[i][0])*np.cos(DH[i][1]),-np.cos(DH[i][0])*np.sin(DH[i][1]),DH[1][2]*np.sin(DH[i][0])],
      [0,np.sin(DH[i][1]),np.cos(DH[i][1]),DH[i][3],],
      [0,0,0,1]]
i=2 #link number
H2_3=[[np.cos(DH[i][0]),-np.sin(DH[i][0])*np.cos(DH[i][1]),np.sin(DH[i][0])*np.sin(DH[i][1]),DH[i][2]*np.cos(DH[i][0])],
      [np.sin(DH[i][0]),np.cos(DH[i][0])*np.cos(DH[i][1]),-np.cos(DH[i][0])*np.sin(DH[i][1]),DH[1][2]*np.sin(DH[i][0])],
      [0,np.sin(DH[i][1]),np.cos(DH[i][1]),DH[i][3],],
      [0,0,0,1]]
i=3 #link number
H3_4=[[np.cos(DH[i][0]),-np.sin(DH[i][0])*np.cos(DH[i][1]),np.sin(DH[i][0])*np.sin(DH[i][1]),DH[i][2]*np.cos(DH[i][0])],
      [np.sin(DH[i][0]),np.cos(DH[i][0])*np.cos(DH[i][1]),-np.cos(DH[i][0])*np.sin(DH[i][1]),DH[1][2]*np.sin(DH[i][0])],
      [0,np.sin(DH[i][1]),np.cos(DH[i][1]),DH[i][3],],
      [0,0,0,1]]

print("homogeneous transformation matrix 0_1 =")
print(np.matrix(H0_1))
print("homogeneous transformation matrix 1_2 =")
print(np.matrix(H1_2))
print("homogeneous transformation matrix 2_3 =")
print(np.matrix(H2_3))
print("homogeneous transformation matrix 3_4 =")
print(np.matrix(H3_4))

# creating transform H0_4
H0_2=np.dot(H0_1,H1_2)
H0_3=np.dot(H0_2,H2_3)
H0_4=np.dot(H0_3,H3_4)

print("homogeneous transformation matrix 0_4 =")
print(np.matrix(H0_4))
