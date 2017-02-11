# Vasya - Clerk
# Level: 6kyu

'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?
Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) 
         # => NO. Vasya will not have enough money to give change to 100 dollars
''' 

def tickets(people):
    vasya = [0,0,0] # vasya[0] = $25, vasya[1] = $50, vasya[2] = $100 bills
    
    for pay in people:
        if (pay == 25):
            vasya[0] += 1    # increment $25 bill
        elif (pay == 50):
            if (vasya[0] == 0):
                return 'NO'
            else:
                vasya[0] -= 1    # decrement $25 bill
                vasya[1] += 1    # increment $50 bill
        else:
            if (vasya[0] >= 1 and vasya[1] >= 1):    # when 25 + 50 bills are available
                vasya[2] += 1    # increment $100
                vasya[1] -= 1    # decrement $50
                vasya[0] -= 1    # devrement $25
            elif (vasya[0] >= 3):    # when 25 * 3 bills are available
                vasya[2] += 1    
                vasya[0] -= 3
            else:    # no change
                return 'NO'
    return 'YES'

'''
Other Solution
def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'
'''

test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
