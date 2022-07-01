'''
Contact Database

The program creates a number formatting system for a contacts database.
The program will take the phone number as input, and if the number starts with "0", replace it with "+254".
The number is printed after formatting.
'''
import re
num = input()

pattern = r"0"
match = re.search(pattern, num)

if match.start()==0:
    res = re.sub(pattern, "+254", num, 1)
    print(int(res))
else:
    print(int(num))
