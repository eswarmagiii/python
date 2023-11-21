#dummy cal

def addition (x, y): #1 
   return x+y 

def subtraction (x, y): #2
   return x-y
 
def multiply (x, y): #3
   return x*y

def divide (x, y): #4
   return x//y

print ("""select operation
         1.addition
         2.subtraction
         3.multiply
         4.divide
         """)

choice = int (input ("enter your choice"))

x = int (input ("enter number 1"))
y = int (input ("enter number 2"))    

if choice == 1:
    print(addition (x, y))
    
elif choice == 2:
    print(subtraction (x, y))
    
elif choice == 3:
    print(multiply (x, y))
    
elif choice == 4:
    print(divide (x, y))
    
else:
    print ("enter correct choice")