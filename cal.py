import divide,multiply,additon,subtract                 #Importing user define modules

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
            print('Given digit is not a number')
            print("---------------------------")
            print('Taking out of calculation')
            print("---------------------------")
            options()
    additon.add(l)                                              # calling usere define module fuctions
    aa=input('Wanna do use more this section(y/n)=' )   # verifying user
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
        print('Given digit is not a number')
        print("---------------------------")
        print('Taking out of calculation')
        print("---------------------------")
        options()
    aa=input('Wanna do use more this section(y/n)=')                # verifying user
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
            print('Given digit is not a number')
            print("---------------------------")
            print('Taking out of calculation')
            print("---------------------------")
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
        print('Given digit is not a number')
        print("---------------------------")
        print('Taking out of calculation')
        print("---------------------------")
        options()
    aa=input('Wanna do use more this section(y/n)=')                            # verifying user
    if aa=='y' or aa=='Y':
        div()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ()
    else:
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
Divide:4''')
    a=int(input("Enter your choice(1,2,3,4)="))          # asking user to choose its calculation method
    if a==1:
        add()
    elif a==2:
        sub()
    elif a==3:
        multipl()
    elif a==4:
        div()
    else:
        print('''
-------------------
THANKYOU FOR USING|
-------------------''')
options()



        

            
