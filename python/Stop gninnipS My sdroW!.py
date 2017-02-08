# Stop gninnipS My sdroW!
# Level: 6kyu

'''
Problem Description: Write a function that takes in a string of one or more words, and returns the 
same string, but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more 
than one word is present.
Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
'''

def spin_words(sentence):
    # Your code goes here
    
    words = sentence.split()
    answer = []
    
    for i in words:
        if(len(i) >= 5):
            answer.append(i[::-1])
        else:
            answer.append(i)
    return ' '.join(answer)

print(spin_words("Welcome to the worldd!"))