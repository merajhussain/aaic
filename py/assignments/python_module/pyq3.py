# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import re
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input examples

# you can free to change all these codes/structure
# String: it will be the input to your program
ip =input ("Enter String :")
String  = str(ip)
 
def replace_digits(String):
    s=''
    for c in String:
        
        if c.isdigit():
            s+='#'
   
    return s # modified string which is after replacing the # with digits

print(replace_digits(String))