# Square Every Digit
# Level - 7Kyu

'''
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    listOfNum = [int(i) for i in str(num)]
    for i in range(len(listOfNum)):
        listOfNum[i] = listOfNum[i] * listOfNum[i]
        
    num = listToNum(listOfNum)
    
    return num
    
        
def listToNum(numList):     # numlist = [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s


 test.assert_equals(square_digits(9119), 811181)