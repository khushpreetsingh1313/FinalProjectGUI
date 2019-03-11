# Author: Khushpreet Singh
# version: 1.0
# Date Created: 13 Jan 2019
# Date Modified: 13 Jan 2019
import csv as file

def main():
    """this method is running all other method with the class object"""
    obj = Finalproject()
    obj.name()
    obj.read()


class Finalproject:
    """
    This class named project is developed by khushpreet singh to perform I/O on csv file and putting data in list and performing
    Create,Read,update and Delete operations on list
    """
    def name(self):
        print("Program written by Khushpreet singh")
        return "Author"

    def read(self):
        """this read function read csv and perform CRUD operations"""
        try:
            path = 'Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv'
            #opening csv file and putting file in object
            with open(path, encoding = "ISO-8859-1") as csvfile:
                csv_read = file.reader(csvfile)
                crud_list = [] #arraylist / data structure
                choice = 'y'

                """loop through csv object to get data without
                column names
                """
                j = 0
                for index_data in csv_read:
                    if (j > 1 and j <= 11):
                        crud_list.append(index_data)
                    j += 1

                cols = ['Species','Year','Julian Day of Year', 'Plant Identification Number','Number of Buds',
                       'Number of Flowers',
                       'Number of Flowers that have Reached Maturity',
                       'Observer Initials',
                       'Observer Comments']

                # while choice is y/Y program will keep running
                while (choice =='y' or choice =='Y'):
                    print("Enter between 1 to 4")
                    print("Enter 1 for Read")
                    print("Enter 2 for add")
                    print("Enter 3 for update")
                    print("Enter 4 for Delete")

                    #user input to runa particular operation on data
                    case = input("Enter case ")

                    if(case == "1"):
                        print("Program written by Khushpreet singh")
                        print(cols)  # print column names from cols array
                        # For Loop for print data of list
                        for data in crud_list:
                            print(data)
                        print("you are running case #"+case)



                    if (case == '2'):
                        print("Program written by Khushpreet singh")
                        #user inputs to insert record in arraylist
                        name_flower = input("enter species ")
                        year = input("enter year ")
                        Julian_Day_of_Year = input("Julian Day of Year ")
                        Plant_Identification_Number = input("Plant Identification Number ")
                        Number_of_buds = input("Number of Buds ")
                        Number_of_Flowers = input("Number of Flowers ")
                        Maturity = input("Number of Flowers that have Reached Maturity ")
                        Observer_Initials = input("observer Initials ")
                        Observer_Comments = input("observer comments ")
                        crud_list.append([name_flower, year, Julian_Day_of_Year,Plant_Identification_Number,Number_of_buds,Number_of_Flowers,Maturity,Observer_Initials,Observer_Comments])
                        print(cols)
                        for data in crud_list:
                            print(data)
                        print("list is updated successfully")
                        print("you are running case #"+case)
                    # Case 3 for update data in list and print
                    if (case == '3'):
                        print("Program written by Khushpreet singh")
                        print(cols) # print column names from cols array
                        # for loop to print data of list before updation
                        for data in crud_list:
                            print(data)
                        #user input index which user want to update
                        j = input("enter index (index start from 0) ")

                        # converting string to Integer
                        index_id = int(j)
                        # user inputs for update record
                        name_flower = input("enter species ")
                        year = input("enter year ")
                        Julian_Day_of_Year = input("Julian Day of Year ")
                        Plant_Identification_Number = input("Plant Identification Number ")
                        Number_of_buds = input("Number of Buds ")
                        Number_of_Flowers = input("Number of Flowers ")
                        Maturity = input("Number of Flowers that have Reached Maturity ")
                        Observer_Initials = input("observer Initials ")
                        Observer_Comments = input("observer comments ")
                        #updating index with new entries
                        crud_list[index_id]=[name_flower, year, Julian_Day_of_Year, Plant_Identification_Number, Number_of_buds,
                             Number_of_Flowers, Maturity, Observer_Initials, Observer_Comments]
                        for data in crud_list:
                            print(data)
                        print("list is updated successfully")
                        print("you are running case #" + case)
                    # Case 4 for print data in list
                    if (case == '4'):
                        print("Program written by Khushpreet singh")
                        print(cols)  # print column names from cols array
                        for data in crud_list:
                            print(data)
                        print("you are running case #" + case)
                        # user input for deleting index
                        i = input("enter index to delete number(index start from 0) ")
                        # converting string to integer
                        index_data = int(i)
                        # Deleting entered index
                        del crud_list[index_data]
                        for data in crud_list:
                            print(data)

                    choice = input("Do you want to continue....(Enter y/Y to continue) ")

        except FileNotFoundError:
            print('file not found')
        return "done"

if __name__ == '__main__':
    main()