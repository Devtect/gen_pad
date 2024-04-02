'''
3 letter female name
starts with either M N or O
followed with A B or C
ends with I

Mia
Noa
Mai
'''
'''
import random

six = ['m', 'n', 'o']
two = ['a', 'b', 'c']
last_letter = ['i', 'l']

letter = random.choice(six)

if letter in 'mno':
    next_letter = random.choice([x for x in mid_letter if x != 'b' and x!='c'])
else:
    next_letter = random.choice([v for v in mid_letter if x != 'a'])

print(letter + next_letter + random.choice(last_letter))
'''


import random

six = ['m', 'n', 'o'] 
two = ['a', 'b', 'c'] 
one = ['i', 'l'] 

user_input = input("enter 3 digits(0-9)")

digit_list= []

for digit in user_input:
    if digit == '6':
        digit_list.append(six)
    elif digit == '2':
        digit_list.append(two)
    elif digit == '1':
        digit_list.append(one)
    else:
        pass
        
combinations = []

for first in digit_list[0]:
    for last in digit_list[2]:
        if first in 'mno':
            for mid in digit_list[1]:
                if mid not in ['b', 'c']:
                    combinations.append(first + mid + last)
        else:
            for mid in digit_list[1]:
                if mid in ['a']:
                    combinations.append(first + mid + last)
            
for combination in combinations:
    print(combination)
    
    
