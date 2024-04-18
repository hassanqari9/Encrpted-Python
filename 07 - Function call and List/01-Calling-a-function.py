# Missed class on 29th November 2023.
# Notes on Notion: https://7thsemester.notion.site/Call-by-Value-and-Call-by-reference-Missed-Class-fd5794f3b2134362bf7a5c7a6d5e50db
# Call by Value
'''
Values are copied to the function
e.g opt(2,4)
it does not effect the Original Variable
'''

# Call by Reference
"""
Two types of data 
1) Mutable - Can be changed 
    List, Dictionary, Set
        For Mutable, Python uses call by reference
2) Immutable - Once defined it cant be changed
    int, float, tuple, String
        For immutable, Python uses call by Value
"""

# Example of Call by value (CBR)
x = 10
def CBR(Sage):
    Sage = 100
    print(Sage)
CBR(x)
print(x)

# Example of Call by Reference (CBR)
x = [10]
def CBR(Sage):
    Sage[0] = 100
    print(Sage)
CBR(x)
print(x)

