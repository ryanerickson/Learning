__author__ = 'joecoastie'
#AND

a,b = 1,0

if a == 1 and b == 1:
    print('1')

elif ((a == 1 and b == 0) or (a == 0 and b == 1)):
    print('0')

elif (a == 0 and b == 0):
    print('0')

else:
    print('Invalid Input')


#OR

a,b = 1,0

if a == 1 or b == 1:
    print('1')
elif ((a == 1 or b == 0) or (a == 0 or b == 1)):
    print('1')
elif (a == 0 or b == 0):
    print('0')
else:
    print('Invalid input')

#NOT
a = 0

if a == 1:
    print('0')
elif a == 0:
    print('1')
else:
    print('Invalid Input')