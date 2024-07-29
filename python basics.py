#!/usr/bin/env python
# coding: utf-8

# # BASICS DATATYPES
# 

# In[1]:


x = 5
get_ipython().run_line_magic('whos', '')


# ##this is used to find saved data and its description 
# 
# 
# 

# In[2]:


print(type(x))


# In[8]:


a,b,c,d,e = 2,2.3,-5,3.2,5.0
get_ipython().run_line_magic('whos', '')


# In[9]:


del d #used to dleate the variable
get_ipython().run_line_magic('whos', '')


# # operators
## use shift + enter to print headline
# variable name cant start with number or special cracter except _

# In[10]:


3x=4


# # bool

# In[18]:


print(2<3)


# In[19]:


print(2==4)
print(2!=3)


# In[20]:


a = 3
b = 4
c = 9
3 == 3.0


# In[21]:


(a<b) and (c>b) or (a==b)


# In[26]:


1 or 0 and 1


# In[27]:


0 or (1 and 0)


# # FUNCTIONS
# 

# 1. ROUND FUNCTION 

# In[28]:


print(round(9.4647))


# 2.DIVMOD FUNCTION :- gives  (quoestent,remainder)

# In[31]:


G = divmod(39,8)


# In[33]:


print(G)
G[1]


# In[36]:


G[0]


# In[37]:


type(G)


# 3. isinstance function :- to check the given data type 

# In[39]:


isinstance(9.9,(int,complex))


# In[40]:


isinstance(2,int)


# 4. INPUT FUNCTION 

# In[41]:


a = input("guess a no.")


# In[42]:


type(a)


# In[48]:


a =int(a) #to convert string into int


# In[47]:


type (a)


# In[49]:


print (a+3)


# In[51]:


b = float(input("enter a real no"))


#  TO KNOW HOW TO USE ANY FUNCTION 

# In[53]:


get_ipython().run_line_magic('pinfo', 'pow')


# In[54]:


get_ipython().run_line_magic('pinfo2', 'input')


# In[55]:


help(round)


# # control flow

# 1. IF CONDITION 

# In[1]:


a = int(input())
b = int(input())
if a>b:
    print(a)#here this line is inside if condition thats why it didnt started from starting
if b>a:
    print(b)
    


# 2. IF ELSE CONDITION 

# In[2]:


a = int(input())
b = int(input())
if a>b:
    print(a)
    print("if part")#here this line is inside if condition thats why it didnt started from starting
else:
    print(b)
    print("else part")
    


# 3.IF ELIF ELSE CONDITION
# 

# In[9]:


a = int(input("enter your marks : "))
if (a>100):#try to use bracket for conditions
    print ("recheck the copy")
elif (a>=85) and (a<=100):#dont put space b\w >and= 
    print("A grade")
elif (a>=75) and (a<85):# similarly all other gates can be used like not, or gates 
    print("A-")
elif (a>=65) and (a<75):
    print ("B")
elif (a>=55) and (a<65):
    print ("B-")
else:
    print("Below average")
    
   



# 4. NESTED IF :- IF CONDITION INSIDE A IF CONDITION 

# In[1]:


# single line comment
""" 
User will enter a floating point number let say 238.915. Your task
is to find out the integer portion before the point (in this case 238)
and then check if that integer portion is an even number or not?
"""
x = float(input("Enter a real number :"))
y = round(x)
if x>0:    
    if y>x:#NESTED IF
        intPortion = y-1 # 29.6
    else:#NESTED ELSE
        intPortion = y
else:
    if y<x:
        intPortion = y+1
    else:
        intPortion = y

if intPortion%2 == 0:
    print("Even")
else:
    print("Odd")


# # LOOPS

# In[2]:


n = int(input())
i = 1
while i < n:
    print(i**2)
    print("This is iteration number :", i)
    i+=1 # i = i+1
print("Loop done")


# In[3]:


n = int(input("no upto which you want even no ."))
i = 1 #starting no.
while i<n:
    if i%2==0:
        print(i)
    else:
        pass
    i += 1


# BREAK AND CONTINUE
# 

# In[10]:


i = 3
while True:
    if i%9 == 0:
        print("Inside if")
        break
    else:
        print("inside Else")
        i = i+1 # i+=1
print("done")


# In[12]:


i = 7
while True:
    if i%9 != 0:
        print("inside if")
        i +=1
        continue
    print("something")
    print("somethingelse")
    break
    
print("done")


# FOR LOOP

# In[2]:


L = []
for i in range (0,12,2):# last no in bracket show common differense b\w no to be taken
    print(i)
    L.append(i**2)
print (L)


# In[11]:


s = {"apple",2.3,"cherry"}
i=1
for x in s:
    print(x)
    i+=1
    if i==3:
        break
    else:
        pass
else:
    print("loop terminate with sucess")
print("outside the loop")


# In[12]:


D = {"A":10,"B":-19,"C":"abc"}
for x in D:
    print(x,D[x])


# GOOD QUESTION SEE LATER

# In[17]:


""" Given a list of numbers i.e. [1,2,4,-5,7,9,3,2], make another list
that contains all the items in sorted order from min to max. i.e. your 
result will be another list like [-5,1,2,2,3,7,9]"""
L = [1,2,4,-5,7,9,3,2]
for j in range(len(L)):
   m = L[j]
   idx = j
   c = j
   for i in range(j,len(L)):
       if L[i]<m:
           m = L[i]
           idx = c
       c+=1    
   tmp = L[j]
   L[j] = m
   L[idx] = tmp
print(L)


# # FUNCTION

# In[18]:


def printMsg(msg):
    """ The function prints the message supplied by the user
    or prints that msg is not in the form of string"""
    
    if isinstance(msg,str):
        print(msg)
    else:
        print("Your input argument is not a string")
        print("Here is the type of what you have supplied :",type(msg))


# In[20]:


printMsg(34)


# In[23]:


def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print((a+b+c)**2)
    else:
        print("Error: the input arguements are not of the expected types")


# In[24]:


checkArgs(2,3,5)


# In[25]:


def f(a,b,c):
    print("A is :",a)
    print("B is :",b)
    print("C is :",c)


# In[26]:


#f(2,3,"game")
f(3,"game",2)


# In[1]:


def myadd(a,b):
    sumValue = a+b
    return sumValue
"""we use return so that we can replace sumvalue to d then 
we can whatever we want with d and it is also used to exit from frunctions"""


# In[2]:


d = myadd(2,3)
print(d)


# In[5]:


def h():
    print("A")
    a = 3
    b = 5
    c = a+b
    print("something")
    return c
    print("B")
    print("C")


# In[4]:


print(h())


# In[6]:


def myAddUniversal(*args): #here args just reprent notion or representation
    s = 0
    for i in range(len(args)):
        s += args[i] # s = s+args[i]
    return s


# In[7]:


print(myAddUniversal(2,4,5,4.6,78))


# In[8]:


def printAllVariableNamesAndValues(**args):
    for x in args:
        print("Variable Name is :",x," And Value is :",args[x])


# In[9]:


printAllVariableNamesAndValues(a = 3,b="B",c="CCC",y=6.7)


# In[10]:


def gg(s=4):
    print(s)


# In[11]:


gg()


# In[12]:


gg(56)


# In[29]:


import sys
sys.path.append('D:/ABC/')


# In[37]:


import my_universal_function as myfs
#from my_universal_function import addAllNumerics


# In[31]:


d = addAllNumerics(2,3,4,5,6,7)
print(d)


# In[38]:


""" Given a list of numbers i.e. [1,2,4,-5,7,9,3,2], make another list
that contains all the items in sorted order from min to max. i.e. your 
result will be another list like [-5,1,2,2,3,7,9]
"""


# In[3]:


def findMin(L,startIndx):
    m = L[startIndx]
    idx = startIndx    
    for i in range(startIndx,len(L)):
        x = L[i]
        if x<m:
            m = x
            idx = i
        else:
            pass                
    return m,idx


# In[4]:


def swapValues(L,idx1,idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L


# In[2]:


L = [2,3,6,7]
L2 = swapValues(L,1,3)
print(L2)


# In[7]:


def checkIfNotNumeric2(L):    
    for x in L:
        if not(isinstance(x,(int,float))):
            return False
    return True


# In[10]:


def sortList(L):
    if not(checkIfNotNumeric2(L)):
        print("Error: List does not contain numeric values")
        return
    else:
        c = 0
        for x in L:
            m,idx = findMin(L,c)
            L = swapValues(L,c,idx)
            c+=1
    return L


# In[11]:


L2 = sortList([2,1,5,3,-8,17])
print(L2)


# # string

# In[15]:


s = "How are you and who are you"
print(s[5])#indexing 
print(s[0:10])
s[-1]
s[-12:-3]


# In[16]:


s[0:12:2]#jump of two


# In[17]:


#s[start:end:step]
s[:12]


# In[18]:


s[::-1]#to reverese the the whole


# In[19]:


a = "    abc def     hgq asdfaf     "
b = a.strip()#remove space from start and end
print(b)


# In[20]:


a = "ABC deFg ;; sadfa QF"
b = a.lower()
print(b)


# In[21]:


c = a.upper()
print(c)


# In[22]:


d = a.replace(";","*")
print(d)


# In[23]:


d = a.replace(";","**&&^^%%")
print(d)


# In[24]:


d = a.replace(";;","two semi colons")
print(d)


# In[25]:


a = "abc;def;hgydfa;yy23"
L = a.split(";")
print(L)


# In[26]:


L[1]


# In[27]:


print(a.capitalize())


# In[28]:


"abcdefghi"<"def"#comparision of alphabatic oder


# In[29]:


"$%"<"*&"


# In[30]:


print("we are learning \"string\" here")


# In[31]:


print('we are learing "string" here')


# In[32]:


print("we are \t now on another line")


# In[33]:


print("c:\name\drive")


# In[34]:


print(r"c:\name\drive")#here r is used to write that there is no scape function


# # DATA STRUCTURE
# 

# In[36]:


L = [1,3,4.9,"name",3]
T = (1,3,4.9,"name",3)
S = {1,3,4.9,"name",3}
D = {23:"twothree",'B':43,'C':'CCD'}


# In[37]:


print("The type of L is ", type(L))
print("The type of T is ", type(T))
print("The type of S is ", type(S))
print("The type of D is ", type(D))


# In[38]:


print(L[1])
print(T[1])
print(3 in S)
print(D[23])


# In[39]:


L[1:3]


# In[40]:


L[::-1]


# In[41]:


T[:3]


# In[45]:


L = L + ["how","are",6,"you"]


# In[49]:


L.append(6.8)


# In[51]:


T2 = ('a','b',45)
T3 = T+T2


# In[52]:


T3


# In[53]:


S.add(56)


# In[54]:


S


# In[55]:


S.update({23,"game",1})


# In[56]:


S


# In[57]:


del L[3]#to deleate a particular element


# In[58]:


S.remove('game')


# In[69]:


D.update(D2)#D=D+D2


# In[62]:


L2 = L.copy()#by this changing L2 does not change L


# In[63]:


get_ipython().run_line_magic('pinfo', 'L.clear')


# In[64]:


get_ipython().run_line_magic('pinfo', 'L.pop')


# In[65]:


L.reverse()


# In[66]:


D.items()


# In[68]:


D2 = {'A':L,'B':T,'C':S,'D':D}


# In[71]:


T


# In[72]:


S


# In[74]:


D2['A'][3]


# In[76]:


K = D2['D']


# In[78]:


"""Let say you are a teacher and you have different student
records containing id of a student and the marks list in each subject
where different students have taken different number of subjects. All
these records are in hard copy. You want to enter all the data in computer
and want to compute the average marks of each student and display"""

def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter student ID: ")
        marksList = input("Enter the marks by comma separted values: ")
        moreStudents = input('Enter "no" to quit insertion: ')
        if studentId in D:
            print(studentId, "is already insterted")
        else:
            D[studentId] = marksList.split(",")
        if moreStudents.lower() == "no":
            return D


# In[79]:


studentData = getDataFromUser()


# In[80]:


studentData


# In[81]:


def getAvgMarks(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s += int(marks)
        avgMarks[x] = s/len(L)
    return avgMarks


# In[82]:


avgM = getAvgMarks(studentData)


# In[85]:


avgM


# # NUMPY 

# In[89]:


import numpy as np


# In[86]:


a = np.array([1,2,3,5,7],dtype='i')#dtype=i means  it is of integer.


# In[87]:


a.dtype#int32 means 32 bits is used 


# In[90]:


B = np.array([[1,2,3,-1],[2,4,5,9]])


# In[91]:


B.ndim#to find dimension of array ,dimension= no of element used to find a element


# In[93]:


B[1,2]# no of element in every should be equal 


# In[94]:


C = np.array([[[1,2,3],[4,5,6],[0,0,-1]],[[-1,-2,-3],[-4,-5,-6],[0,0,1]]])


# In[96]:


C.shape[2]#shape[2] = no of two dimentional arrey 


# In[97]:


C[1,0,2]


# In[98]:


A = np.array([2])


# In[99]:


A.ndim


# In[100]:


B = np.array(3)


# In[101]:


B.ndim


# In[103]:


C.size#no of element in a arrey 


# In[104]:


C.nbytes#no of bites used


# In[105]:


A = np.arange(20,100,3) # for i in range(20,100,3)
print(A)


# In[108]:


print(range(10))


# In[117]:


print(list(range(10)))


# In[118]:


A = np.random.permutation(np.arange(10))#to make the arrey random

print(A)


# In[119]:


import matplotlib.pyplot as plt


# In[120]:


A = np.random.rand(1000)#to create a arey with 100 element b\w 1 and 0 


# In[121]:


plt.hist(A,bins=100)


# In[122]:


B = np.random.randn(100000)
plt.hist(B,bins=200)


# In[124]:


C = np.random.rand(2,3)#create 2*3 matrix


# In[126]:


C


# In[128]:


v = np.random.randint(20,300)#to chose any no b\w 20 to 300


# In[130]:


v


# In[133]:


C = np.random.rand(2,3,4,2)
""""there are two 3d arrey  
each 3d arrey have 3 2d areey 
each 2d arrey have 4 1d arrey 
each 1d arrey have 2 element"""


# In[132]:


C


# In[134]:


D = np.arange(100).reshape(4,25)#reshape to build a 4*25 matrix 


# In[135]:


D


# In[136]:


get_ipython().run_line_magic('pinfo', 'np.zeros')


# In[137]:


get_ipython().run_line_magic('pinfo', 'np.ones')


# In[139]:


A = np.arange(100)


# In[140]:


b = A[3:10]#indexing from 3 till10 but no 10 
print(b)


# In[141]:


b[0] = -1200


# In[142]:


b


# In[143]:


A


# In[145]:


b = A[3:10].copy()#we are coping a to b so that by chaning in b there should be no change in A


# In[146]:


A[::5]


# In[147]:


A[::-5]


# In[178]:


idx = np.argwhere(A==3)[0][0]


# In[179]:


idx


# In[169]:


A[idx]=3


# In[152]:


A


# In[182]:


A = np.round(10*np.random.rand(5,4))#5*4 matrix round as random.rand create no b\w 0and 1 so to round them


# In[183]:


A


# In[184]:


A[1,2]


# In[185]:


A[1,:]


# In[186]:


A[:,1]


# In[187]:


A[1:3,2:4]


# In[189]:


A.T#make tanspose 


# In[190]:


import numpy.linalg as la# linear algebra library 


# In[191]:


la.inv(np.random.rand(3,3))


# In[192]:


A


# In[193]:


A.sort(axis=0)


# In[194]:


A


# In[195]:


A = np.arange(100)


# In[196]:


B =A[[3,5,6]]#element at indx3,5,6


# In[198]:


B#here by changing element in b does not change element in A


# In[199]:


B = A[(A<40) & (A>30)]#here we can use boolen condition for shorting


# In[200]:


B


# In[201]:


# &, and 
# |, or
# ~, not
# these are symboles for numpy


# In[202]:


A = np.round(10*np.random.rand(2,3))


# In[203]:


A


# In[204]:


A=A+4


# In[205]:


A


# In[206]:


A+(np.arange(2).reshape(2,1))


# In[207]:


B = np.round(10*np.random.rand(2,2))


# In[208]:


B


# In[209]:


C = np.hstack((A,B))


# In[210]:


C


# In[211]:


A = np.random.permutation(np.arange(10))


# In[212]:


A


# In[213]:


A.sort()


# In[214]:


A


# # pandas

# In[215]:


import pandas as pd


# In[216]:


A = pd.Series([2,3,4,5],index=['a','b','c','d'])


# In[217]:


A['a':'c']


# In[218]:


grads_dict = {'A':4,'B':3.5,'C':3,'D':2.5}
grads = pd.Series(grads_dict)


# In[219]:


grads.values


# In[220]:


marks_dict = {'A':85,'B':75,'C':65,'D':55}
marks = pd.Series(marks_dict)


# In[221]:


marks


# In[222]:


D = pd.DataFrame({'Marks':marks,'Grades':grads})


# In[223]:


D


# In[224]:


D.T


# In[225]:


D.values


# In[226]:


D.values[2,0]


# In[227]:


D.columns


# In[228]:


D['ScaledMarks'] = 100*(D['Marks']/90)


# In[229]:


D


# In[230]:


del D['ScaledMarks']


# In[231]:


D


# In[232]:


G = D[D['Marks']>70]


# In[233]:


G


# In[234]:


A = pd.DataFrame([{'a':1,'b':4},{'b':-3,'c':9}])


# In[235]:


A


# In[236]:


A.fillna(0)


# In[237]:


A = pd.Series(['a','b','c'],index=[1,3,5])


# In[238]:


A[1]


# In[240]:


A[1:3]


# In[241]:


A.loc[1:3]


# In[ ]:




