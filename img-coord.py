# # Exterior orientation
o,f,k=float(input('Omega(ilk açı giriniz): ')),float(input('Omega(ilk açı giriniz): ')),float(input('Omega(ilk açı giriniz): '))
Ext_or=[]
Ext_or.append(o)
Ext_or.append(f)
Ext_or.append(k)
#print(Ext_or) This is optional if you want to see your angle outputs.
#At once we creating input for omega, fi and kapa angles.


# Grad_Radyan Dönüşümü
# g*math.pi/200

import math

m_0_0=round((math.cos(f*math.pi/200)*math.cos(k*math.pi/200)),3)
m_0_1=round((-math.cos(f*math.pi/200)*math.sin(k*math.pi/200)),3)
m_0_2=round((math.sin(f*math.pi/200)),3)

m_1_0=round((math.cos(o*math.pi/200)*math.sin(k*math.pi/200)+math.sin(o*math.pi/200)*math.sin(f*math.pi/200)*math.cos(k*math.pi/200)),3)
m_1_1=round((math.cos(o*math.pi/200)*math.cos(k*math.pi/200)-math.sin(o*math.pi/200)*math.sin(f*math.pi/200)*math.sin(k*math.pi/200)),3)
m_1_2=round((-math.sin(o*math.pi/200)*math.cos(f*math.pi/200)),3)

m_2_0=round((math.sin(o*math.pi/200)*math.sin(k*math.pi/200)-math.cos(o*math.pi/200)*math.sin(f*math.pi/200)*math.cos(k*math.pi/200)),3)
m_2_1=round((math.sin(o*math.pi/200)*math.cos(k*math.pi/200)+math.cos(o*math.pi/200)*math.sin(f*math.pi/200)*math.sin(k*math.pi/200)),3)
m_2_2=round((math.cos(o*math.pi/200)*math.cos(f*math.pi/200)),3)

#Now we are creating the translation matrices, it is optional that using basic radyan-pi transformation rather than calculate each steps. I will be waiting for your requests.
matrix = [[m_0_0, m_0_1, m_0_2],
    [m_1_0, m_1_1, m_1_2],
    [m_2_0, m_2_1, m_2_2]]

#print(matrix)
#This print is optional if you want to check your matrices. I advise this because ıt make easier notice your error.

# Projection_center
x,y,z=float(input('Project(Enter your X coordinate of projection center): ')),float(input('Project(Enter your Y coordinate of projection center):  ')),float(input('Project(Enter your Z coordinate of projection center):  '))
Pr_k=[]
Pr_k.append(x)
Pr_k.append(y)
Pr_k.append(z)

#print(Pr_k) Optional
#These coordinates are your object space coordinates of projection center.
#Now code require the object space coordinates of projection center.


# Inter_Or
x0,y0,f0=float(input('Int_Or(X0): ')),float(input('Int_Or(Y0): ')),float(input('Int_Or(fiducial_mark): '))
Int_or=[]
Int_or.append(x0)
Int_or.append(y0)
Int_or.append(f0)
#print(Int_or)
#Then we create input parameters for interior orientation .These are as you know fiducial marks and x0 and y0.

# Field_cord
c_X,c_Y,c_Z=float(input('Field_X: ')),float(input('Field_Y: ')),float(input('Field_Z: '))
Field_cr=[]
Field_cr.append(c_X)
Field_cr.append(c_Y)
Field_cr.append(c_Z)

#print(Field_cr)
#Last we creating inputs for field coordinates of field point to be transformed.

Field_X=(x0-(f0*((m_0_0*(x-c_X)+m_1_0*(y-c_Y)+m_2_0*(z-c_Z))/(m_0_2*(x-c_X)+m_1_2*(y-c_Y)+m_2_2*(z-c_Z)))))
Field_Y=(y0-(f0*((m_0_1*(x-c_X)+m_1_1*(y-c_Y)+m_2_1*(z-c_Z))/(m_0_2*(x-c_X)+m_1_2*(y-c_Y)+m_2_2*(z-c_Z)))))

#And finally we reach our image plane coordinates of field point. 
# It is your choise to assign them in variables but I prefer to print out.
 

print(Field_X,Field_Y)

