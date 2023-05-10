# Task: Explore in Google and Make a document :

# 1. What is function in python?
'''A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.
 A function can return data as a result.'''

# 2. Types of function in python?
'''There are many types of Python Functions. And each of them is very vital in its own way. 
The following are the different types of Python Functions:
* Python Built-in Functions
* Python Recursion Functions
* Python Lambda Functions
* Python User-defined Functions'''

# 3. What is user define function in python?
''' Functions that we define ourselves to do certain specific task are referred as user-defined functions. 
The way in which we define and call functions in Python are already discussed. 
Functions that readily come with Python are called built-in functions.'''

# 4. What is built in funciton in python?
'''The Python built-in functions are defined as the functions whose functionality is pre-defined in Python. 
The python interpreter has several functions that are always present for use. These functions are known as Built-in Functions.'''

# 5. What is spyder tool in python & Why we use it?
'''Spyder is an open-source cross-platform integrated development environment (IDE) for scientific programming in the Python language.
'''

# 6. What is parameter in function?
'''A parameter is a special kind of variable used in a function to refer to one of the pieces of data provided as input to the function.
 These pieces of data are the values of the arguments with which the function is going to be called/invoked. 
 An ordered list of parameters is usually included in the definition of a function, so that, each time the function is called, 
 its arguments for that call are evaluated, and the resulting values can be assigned to the corresponding parameters.'''

# Task: Write a program to create a function.

# Scenario1:
# credit card offer.
#  if your salary is less than 10000.  credit limit 10 times of your salary. 
#  if your salary is 10000 to 30000.  Credit limit is 20 time of your salary.
#  if your salary is more than 30000.  Credit limit is 30 times of your salary.
#  క్రెడిట్ కార్డ్ ఆఫర్. 
#  మీ జీతం 10000 కంటే తక్కువ ఉంటే. క్రెడిట్ పరిమితి మీ జీతంకి 10 రెట్లు. 
#  మీ జీతం 10000 నుండి 30000 వరకు ఉంటే. క్రెడిట్ పరిమితి మీ జీతంలో 20 రెట్లు .
#  మీ జీతం 30000 కంటే ఎక్కువ ఉంటే క్రెడిట్ పరిమితి మీ జీతం కంటే 30 రెట్లు.

def credit_card_offer(salary):
    if salary < 10000:
        limit= salary*10
        print(limit)
    elif salary >= 10000 or salary <= 30000:
        limit= salary*20
        print(limit)
    elif salary >30000:
        limit= salary*30
        print(limit)
    else:
        print("No Offers Available on Your Salary")        
credit_card_offer(10000)
 
#  Scenario2:
#  DMart discount offer. 
#  if your purchase amount is less than 20000. discount is 20%.
# if your purchase amount is 20000 to 40000. discount is 30%. 
# if your purchase amount is more than 50000. discount is 40%.

# DMart తగ్గింపు ఆఫర్. మీ కొనుగోలు మొత్తం 20000 కంటే తక్కువ ఉంటే. తగ్గింపు 20%.
# మీ కొనుగోలు మొత్తం 20000 నుండి 40000 వరకు ఉంటే. తగ్గింపు 30%. 
# మీ కొనుగోలు మొత్తం 50000 కంటే ఎక్కువ ఉంటే. తగ్గింపు 40%.

def Dmart_offer(amount):
    if amount <20000:
        discount= amount*.20
        print(discount)
    elif amount >= 20000 or amount <= 40000:
        discount= amount*.30
        print(discount)
    elif amount > 50000:
        discount= amount*.40
        print(discount) 
    else:
        print("No Offers Available on Your Price")   
Dmart_offer(10000)        

# Scenario3:
# Amazom online offer. 
# if product is electoric type then 20% discount. 
# if product is cloth type then 30% discount. 
# if product is footware then 40% discount.
# Amazom ఆన్‌లైన్ ఆఫర్.
#  ఉత్పత్తి ఎలక్టోరిక్ రకం అయితే 20% తగ్గింపు. 
#  ఉత్పత్తి వస్త్రం రకం అయితే 30% తగ్గింపు. 
#  ఉత్పత్తి ఫుట్‌వేర్ అయితే 40% తగ్గింపు.

def amazon_offer(product):
    if product == "electric":
        print("20% Discount")
    elif product == "cloth":
        print("30% Discount")
    elif product == "footware":
        print("40% Discount")
    else:
        print("NO Discount on Your Product")
amazon_offer("electric")
