import part1_studentversion
import part_staffversion_horizontal_histogram
import part2_staff_version_vertical_histogram
import part3_staff_version_vertical_histogram_extension
import part4_writeToFile
import part4_ReadFromFile

def menu():
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    print('1 :select ''1'' for student version')
    print('2 :select ''2'' for staff version_horizontal Histogram')
    print('3 :select ''3'' for staff version_vertical Histogram ')
    print('4 :select ''4'' for staff version_vertical Histogram extension')
    print('5 :select ''5'' for staff version_store_data_to_text')
    print('6 :select ''6'' for staff version read textfile')
    print('q :select ''q'' to quit')
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    c = [0, 20, 40, 60, 80, 100, 120]
    select=str(input("select a number: "))

    if select=='1':
        
            c = (0, 20, 40, 60, 80, 100, 120)
            total=0
            continue_process = str(input("Would you like to enter another set of data? \n Enter 'y' to proceed or 'q' to quit and view results: "))
            part1_studentversion.studentVersion(continue_process)
            menu()
    elif select=='2':
        progress=[]
        module_trailer=[]
        exclude=[]
        model_retriver=[]
        c = (0, 20, 40, 60, 80, 100, 120)
        total=0
        part_staffversion_horizontal_histogram.Staff_version_horizontal_Histogram()
        menu()
    elif select=='3':
        progress = []
        module_trailer = []
        exclude = []
        model_retriver = []

        listpro = (progress, module_trailer, model_retriver, exclude)
        total_outcomes = 0
        
        part2_staff_version_vertical_histogram.Staff_version_vertical_Histogram()
        menu()


    elif select=='4':
        progress = []
        module_trailer = []
        exclude = []
        model_retriver = []
        progress1 = []
        module_trailer1 = []
        exclude1 = []
        model_retriver1 = []
        listpro = (progress, module_trailer, model_retriver, exclude)
        total_outcomes = 0
        progressdata = []
        totaldata = []
        part3_staff_version_vertical_histogram_extension.Staff_version_vertical_Histogram_extension()
        menu()



    elif select=='5':
        progress = []
        module_trailer = []
        exclude = []
        model_retriver = []
        progress1 = []
        module_trailer1 = []
        exclude1 = []
        model_retriver1 = []
        listpro = (progress, module_trailer, model_retriver, exclude)
        total_outcomes = 0
        progressdata = []
        totaldata = []
        part4_writeToFile.writeToText()
        menu()


    elif select=='6':
        part4_ReadFromFile.readfile()
        menu()


    else:
        print('Quit programme')


    

menu()