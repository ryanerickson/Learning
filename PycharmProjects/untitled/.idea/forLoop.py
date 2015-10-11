__author__ = 'joecoastie'
#for data in [1,2,3,4,5]:
#    print(data)

#checking to see if the letters are in an even location
#key checks for for number spot (s is 0) and data is the letter
for key,data in enumerate('string'):
    if key % 2 == 0: #0 check for even, 1 checks for odd
        print('The letter {} is in an even location'.format(data))