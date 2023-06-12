import divide,multiply,additon,math,subtract        #Importing user define modules
def checking():
    print('Given digit is not a number')
    print("---------------------------")
    print('Taking out of calculation')
    print("---------------------------")

def add():                                                #function that responsible for addition calculations
    print("""-----------------------------               
INSTRUCTION FOR USERS
****PRESS 0 TO COMPLETE THE CALCULATION AND GET THE ANSWER****
--------------------------------------------------------------""")    # Giving user instructions how to use the calculator
    l=[]
    for i in range(10000):
        b=eval(input("Enter number="))
        if (type(b)==int and b!=0) or type(b)==float :      # checking numbers by well conditional expression
            l.append(b)
        elif b==0:
            print('--------------')
            print('ANSWER IS:')
            print('---------------')
            break
        else:
            checking()
            options()
    additon.add(l)                                              # calling usere define module fuctions
    aa=input('Want enter more numbers(y/n)=' )   # verifying user
    if aa=='y' or aa=='Y':
        add()
    else:
        options()
        
def sub():                                                          #function that responsible for subtraction section
    x=eval(input("Enter first number="))
    y=eval(input("Enter second number="))
    if (type(x)==int or type(x)==float) and (type(y)==int or type(y)==float):               # checking numbers by well conditional expression
        subtract.sub(x,y)                                    # calling usere define module fuctions                                      
    else:
        checking()
        options()
    aa=input('you want to enter more numbers(y/n)=')                # verifying user
    if aa=='y' or aa=='Y':
        sub()                                                
    else:
        options()
        
def multipl():                                                          # functions that responsible for multiplication sections
    print("""-----------------------------
INSTRUCTION FOR USERS
****PRESS 0 TO COMPLETE THE CALCULATION AND GET THE ANSWER****
--------------------------------------------------------------""")           # Giving user instructions how to use the calculator
    l=[]
    for i in range(10000):
        b=eval(input("Enter number="))
        if (type(b)==int and b!=0)  or type(b)==float :            # checking numbers by well conditional expression
            l.append(b)
        elif b==0:
            print('--------------')
            print('ANSWER IS:')
            print('---------------')
            break
        else:
            checking()
            options()
    multiply.multiply(l)               # calling usere define module fuctions                                          
    aa=input('Wanna do use more this section(y/n)=')                       # verifying user
    if aa=='y' or aa=='Y':
        multipl()
    else:
        options()
def div():                                                                     # function responsible for division calculations
    x=eval(input("Enter first number="))
    y=eval(input("Enter second number="))
    if (type(x)==int or type(x)==float) and (type(y)==int or type(y)==float):                                       # checking numbers by well conditional expression
        divide.divide(x,y)                              # calling usere define module fuctions
    else:
        checking()
        options()
    aa=input('Wanna do use more this section(y/n)=')                            # verifying user
    if aa=='y' or aa=='Y':
        div()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ()
    else:
        options()

def trigno(x):
    if type(x)==int or type(x)==float:
        print('''-----------------------
Press
sin=1
cos=2
tan=3
log=4:
--------------------------''')
        a=int(input('Enter your choice(1/2/3)'))
        print('--------------------------')
        if a==1:
            print('Value is :',math.sin(x))
            print('-----------------')
            options()
        elif a==2:
            print('Value is :',math.cos(x))
            print('-------------------')
            options()
        elif a==3:
            print('Value is :',math.tan(x))
            print('-------------------')
            options()
        elif a==4:
            print('Value is :',math.log(x))
            print('-------------------')
            options()
        else:
            print()
            options()
    
    else:
        checking()
        options()
def power():
    ba=eval(input('Enter base value='))
    baa=int(input('Enter exponent to be raised='))
    print('------------------------------------')
    if type(baa)==int and (type(ba)==int or type(ba)==float):               # checking numbers by well conditional expression
            print('Value is :',math.pow(ba,baa))
            print('-----------------')
            options()
    else:
        checking()
        options()
def factor():
    c=int(input('Enter number for factor='))
    print('-------------------')
    print('Value is :',math.factorial(c))
    print('-------------------')
    options()

                
def options():
    print("----------------------------")                       # Giving user instructions how to use the calculator
    print('''INSTRUCTIONS FOR THE USERS
-------
PRESS:
-------
Add:1
Subtract:2
Multiply:3
Divide:4
Trigonomertic calculations or log=5
power=6
factorial=7
exit=8
------------------------------------''')
    a=int(input("Enter your choice(1,2,3,4)="))          # asking user to choose its calculation method
    if a==1:
        add()
    elif a==2:
        sub()
    elif a==3:
        multipl()
    elif a==4:
        div()
    elif a==5:
        c=eval(input('Enter number='))
        trigno(c)
    elif a==6: 
        power()
    elif a==7:
        factorial()
    elif a==8:
        print('''
-------------------
THANKYOU FOR USING|
-------------------''')
    else:
        print('''INVALID OPTION!!!!!!
--------------------
PLEASE ENTER A VALID OPTION
---------------------------
RENTER OPTION
-------------
THANK YOU!!!!!!!
----------------''')
        options()


#MAIN PROGRAM
print('WELCOME USERS!!!!!! ')
print('''CALCULATOR IS STARTING........
WAIT A MOMENT.......
READ ALL THE INSTRUCTIONS CAREFULLY....
IT BEGINS................!!!''')

options()  #Starting function 
        

            
