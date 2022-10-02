# Kabba Bangura
# 27.09.2022
# ISQA 390

# csv library is used for this programme.
import csv

FILENAME = "customers_1.csv"

total_list = []

my_objects = []

# this is the main class which holds the objects of customer information.
class CustDetails:
    try:
        csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");

        def __int__(self, cust_id, fname, lname, company, street, city, state, zipcode, number):
            self.cust_id = cust_id
            self.fname = fname
            self.lname = lname
            self.company = company
            self.stret = street
            self.city = city
            self.state = state
            self.zipcode = zipcode
            self.nuber = number

    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")

    # this function reads the details from .csv file and store those in a list of objects called total_list.
    def file_reader(self):
        try:
            csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");

            for row in csv_file:
                total_list.append(row)

                for i in total_list:
                    self.cust_id = i[0]
                    self.fname = i[1]
                    self.lname = i[2]
                    self.company = i[3]
                    self.stret = i[4]
                    self.city = i[5]
                    self.state = i[6]
                    self.zipcode = i[7]
        except FileNotFoundError as e:
            print(f"Could not find {FILENAME} file.")

    # this function reads the data from .csv file and display the customer ID and name as requested in the assignment.
    def id_and_name(self):
        try:
            csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");
            for row in csv_file:
                total_list.append(row)

                for i in total_list:
                    self.cust_id = i[0]
                    self.fname = i[1]
                    self.lname = i[2]
                    self.company = i[3]
                    self.stret = i[4]
                    self.city = i[5]
                    self.state = i[6]
                    self.zipcode = i[7]

                print(f'{self.cust_id} : {self.fname}  {self.lname}')

        except FileNotFoundError as e:
            print(f"Could not find {FILENAME} file.")

    # this function search a customer with a specific customer ID.
    def find_customer(self, cnumber):

            try:
                csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");

                for row in csv_file:
                    total_list.append(row)

                    for i in total_list:
                        if cnumber == i[0]:
                            print(f'{self.fname} {self.lname} \n'
                                  f'{self.company} \n'
                                  f'{self.stret} \n'
                                  f'{self.city} {self.state} {self.zipcode}')
                            break
                        if int(cnumber) > 500 or int(cnumber) < 101:
                            print(f'Customer {cnumber} does not exist')
                            break
                    break
            except FileNotFoundError as e:
                print(f"Could not find {FILENAME} file.")
            except ValueError as e:
                print("Customer a does not exist")

# this function is doing the basic interaction with the user by using all above functions.
# this function is not belonged to the class mentioned above but this is not the main function.
def customer_interaction():
    cust1 = CustDetails()

    cust1.file_reader()

    cust1.id_and_name()

    print(" ")
    user_input= input("Enter Customer ID: ")

    cust1.find_customer(cnumber=str(user_input))
    print(" ")

# this is the main function. a while loop is used to repeatedly continue the task.
while True:

    customer_interaction()


    response = input("Would you like to continue? y/n: ")

    if response == "y":
        pass
    elif response == "n":
        exit()
    else:
        print("Not a valid response")
        exit()



