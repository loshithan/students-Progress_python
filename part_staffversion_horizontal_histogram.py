progress=[]
module_trailer=[]
exclude=[]
model_retriver=[]
c = (0, 20, 40, 60, 80, 100, 120)
total=0
def Staff_version_horizontal_Histogram():
    while True:
        continue_process = str(
            input("Would you like to enter another set of data? \n Enter 'y' to proceed or 'q' to quit and view results: "))
        if continue_process=='y':



            while True:
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



                total = x + y + z
                while True:

                        if total==120:

                            if x == 120:
                                print("progress")
                                progress.append(1)
                            elif x == 100:
                                print("module trailer")
                                module_trailer.append(2)
                            elif z in range(0, 61):
                                print("module retriever")
                                model_retriver.append(3)
                            else:
                                y in range(0, 41)
                                print("exclude")
                                exclude.append(4)
                            break




                        else:
                            print("total invalid")
                            break



                break




        elif continue_process=='q':
            print("quit program")
            print()


            print('--------------------------------------------------------------------------------------------------------------------------------------')
            print('progress :',len(progress)*"*" )
            print('module trailer :',len(module_trailer)*"*" )
            print('module retriever :',len(model_retriver)*"*")
            print('exclude :',len(exclude)*"*" )
            print('--------------------------------------------------------------------------------------------------------------------------------------')
            break
        else:
            print("pls enter validy option q or y ")
