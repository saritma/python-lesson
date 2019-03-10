# sarit malayev 311397582
# question 2
def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition.

   Note: It should print out the first number (with a palindrome in its last 4 digits),
   not all 4 "versions" of it.
   """
   l=[]
   for i in range(100000,999999):
       s=str(i)
       if s[2]==s[5] and s[3]==s[4]:
           i=i+1
           s=str(i)
           if s[1]==s[5] and s[2]==s[4]:
               i=i+1
               s=str(i)
               if s[1]==s[4] and s[2]==s[3]:
                   i=i+1
                   s=str(i)
                   if s[0]==s[5] and s[1]==s[4] and s[2]==s[3]:
                        l.append(i-3)
        
   return l


print(check_palindrome())

