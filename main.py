# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("sng53@calpoly.edu")
print(message)

def smallest (n:float, m:float) -> float:          # Task 3
   if n < m:
      return n       # For which calls below is this statement evaluated?
   else:
      return m

first = smallest(2,3)      # What is the value of first? The value is 2
second = smallest(2,2)     # What is the value of second? Is this reasonable result? Why or Why not? The value is 2. Yes this is reasonable because both values are equal and same minimum so either one is a valid "smallest" and returning m is correct.
print ()

def function2 (a: int, b: int, c:int)-> int:
   if a > b and a > c:
      return a - b      # In general, when will a call to this function evaluate this statement? When a is greater than both b and c.
   elif b > c:
      return b + c      # In general, when will a call to this function evaluate this statement? When a isn't the largest and b is greater than c meaning b is the largest.
   else:
      return 2 * c      # In general, when will a call to this function evaluate this statement? When a and b is smaller than c as c is the largest.

answer1 = function2(3,2,1) # What is the value of answer1? The value is 1
answer2 = function2(2,3,1) # What is the value of answer2? The value is 4
answer3 = function2(2,1,3) # What is the value of answer3? The value is 6
print()

from typing import Optional      # Task 4

def checked_access (L: list[list], idx:int) -> Optional[int]:
   test = idx >= 0 and idx < len(L)  # What is the value of test on each cell? The value of test for first is False and the value of test in second is True. 
   if test:                          # What is this check preventing? The check prevents an Index error so the program doesn't attempt to access an index that doesn't exist in the list.
      return L[idx]
   else:
      return None

first = checked_access([1,0,1], 9) # What is the value of first? The value is None.
second = checked_access([1,0,1], 2) # What is the value of second? The value is 1.
print ()

def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0] + len(L[1]) + len(L[2]))   # For which call below is this statement evaluated and what are the  values being added? The call is first. The values being added is 4, 2, and 3.
   elif len (L) > 1:
      result = len(L[0] + len(L[1]))               # For which call below is this statement evaluated and what are the values being added? The call is third. The values being added is 7 and 4.
   elif len(L) > 0:
      result = len(L[0])                           # For which call below is this statement evaluated and what are the values being added? The call is second. The value being added is 11.
   else:
      result = 0
   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum (["second call"])
third = length_sum (["another", "call"])
print ()