#student version



def input_credit():
    global x,y,z
    while True:
                    try:
                        x=int(input("enter volume of credit at pass level : "))
                        if x in c:
                            break
                        else:
                            print("out of range")

                    except ValueError:
                        print("enter integer value")
    while True:
                    try :
                        y=int(input("enter volume of credit at defer level : "))
                        if y in c:
                            break
                        else:
                            print("out of range")

                    except:
                        print("enter integer Value")
    while True:
                    try:
                        z=int(input("enter volume of credit at fail level : "))
                        if z in c:
                            break
                        else:
                            print("out of range")

                    except:
                        print("enter integer Value")

c = [0, 20, 40, 60, 80, 100, 120]
total=0
continue_process = str(input("Would you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: "))
def studentVersion(continue_process):
    global total
    
    if continue_process=='y':


        
            
                input_credit()
                



                total = x + y + z
                while True:

                            if total==120:

                                    if x == 120:
                                        print("progress")

                                    elif x == 100:
                                        print("module trailer")

                                    elif z in range(0, 61):
                                        print("module retriever")

                                    else:
                                        y in range(0, 41)
                                        print("exclude")

                                    break
                                    





                            else:
                                    print("total invalid")
                                    break
                                    







    elif continue_process=='q':
        print("quit program")
        print()




    else:
        print("pls enter validy option q or y ")
