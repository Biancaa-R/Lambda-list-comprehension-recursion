#Lambda function to print square:

y=lambda x : x**2
print(y(4),"is the square of the number")

#lambda function to find the larger of 2 numbers

y = lambda a,b : a if a>b else b

print(y(9,7),"is the greater number")

#Sorting names based on length:

names=["bob","brittany","timm","gilly"]
names.sort(key=lambda x : len(x))
print(names)

# concatenation of lists
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]

#y=lambda l1,l2 : x+y for x,y in l1,l2

y=list(i for i in range(0,9))

print(y)

y=list(map( lambda x : x**2 ,range(0,9)))
print(y)

'''16 is the square of the number
9

======================== RESTART: D:/lambda/lamdafns.py ========================
16 is the square of the number
9 is the greater number
['bob', 'timm', 'gilly', 'brittany']

======================== RESTART: D:/lambda/lamdafns.py ========================
16 is the square of the number
9 is the greater number
['bob', 'brittany', 'gilly', 'timm']

======================== RESTART: D:/lambda/lamdafns.py ========================
16 is the square of the number
9 is the greater number
['bob', 'brittany', 'gilly', 'timm']

======================== RESTART: D:/lambda/lamdafns.py ========================
16 is the square of the number
9 is the greater number
['bob', 'timm', 'gilly', 'brittany']
<function <lambda> at 0x000002A8194E9120>

======================== RESTART: D:/lambda/lamdafns.py ========================
16 is the square of the number
9 is the greater number
['bob', 'timm', 'gilly', 'brittany']
[1, 2, 3, 4, 5, 3, 4, 5, 6, 7]
'''


