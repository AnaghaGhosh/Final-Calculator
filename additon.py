def add(l):
    print('---------')
    if len(l)<2:
        print("enter atleast two numbers to add")
    else:
        for i in range(len(l)):
            print(l[i],end="+")
        print('=',sum(l))
        print('-----------')
