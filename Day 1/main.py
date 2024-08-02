print ("Day 1 - Python Print Function\n")
print ("The function is declared like this: \n")
print ("print('what to print')") 

    # String Concatenation 

print ("Iftekhar" " Hossain" " Tanveer")
print ("Iftekhar" + " " + "Hossain"+ " " +  " Tanveer")

    # String Manipulation
print ("Day 1 - String Manipulation")
print ("String concatenation is done with the " "+" " sign")
print ('e.g. print("Hello " + "world")')
print ("New lines can be created with a backslash and n.")

    # Input function 
print ("What is your name? ") #Only prints. Cannot take input 
# input ("What is your name? ") # Takes input as an answer 
# print('Hello '+ input("What is your name? "))


    #length function 
#write a program that prints the number of characters in a users name. 
#we use len() to count the number of a string 
print ("The length of the name is " + ( len ( input ("What is your name?"))) + " characters")

# There's an error. because we cannot concatenate a string with an integer in python. karon python ekta bokachoda lang. 
# So we have to convert it to string or change the format. 

# Here is how to convert it to string 
print("The length of the name is " + str(len(input("What is your name?"))) + " characters")

# Here is how to change the format 
name = input("What is your name?")
print(f"The length of the name is {len(name)} characters")


# Why the f is outside braces 
# In Python, the `f` before the string literal indicates that it is an f-string (formatted string literal). This syntax allows you to embed expressions inside string literals, using curly braces `{}`. The `f` should be placed immediately before the opening quote of the string, not inside the braces.

# Here's the correct way to use f-strings:

# ```python
# name = input("What is your name?")
# print(f"The length of the name is {len(name)} characters")
# ```

# In this example:
# - `f"` starts the f-string.
# - `{len(name)}` is an embedded expression inside the f-string.
# - The result of `len(name)` is inserted into the string at that position.

# So the `f` is placed before the opening quote to indicate that the string is an f-string and allows you to use the curly braces for expression interpolation.

