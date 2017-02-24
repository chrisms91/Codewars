# Consecutive Strings
# Level: 6 Kyu

'''
You are given an array strarr of strings and an integer k. 
Your task is to return the first longest string 
consisting of k consecutive strings taken in the array.
'''

def longest_consec(strarr, k):
    n = len(strarr)
    longest = ""
    
    if((n == 0) or (k > n) or (k <= 0)):
        return ""
    else:
        for index in range(0, n - k+1):
            current = "".join(strarr[index:index+k])
            
            if(len(longest) < len(current)):
                longest = current
    return longest


'''
Took me some times to understand what the problem wants.
At first, I tried to solve it using JavaScript but since I am novice in JS,
I changed my mind to use python. Learned how to use join more clearly.
'''