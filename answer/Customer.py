# Kabba Bangura
# 27.09.2022
# ISQA 390

# csv library is used to operate the functions of this file
import csv

FILENAME = "customers_1.csv"
all_list = [];


# this is the customer class which holds the information
class Customer:

    # this is the defining of customer class attributes.
    def __int__(self, cust_id, fname, lname, company, street, city, state, zipcode):
        self.cust_id = cust_id;
        self.fname = fname;
        self.lname = lname;
        self.company = company;
        self.stret = street;
        self.city = city;
        self.state = state;
        self.zipcode = zipcode;

    # this is the string representation of the object.
    def __str__(self):
        return (f'{self.fname}, {self.lname}, \
                {self.company},\
                {self.stret},\
                {self.city}, {self.state}, {self.zipcode}')  # this method shoudl be changed according to question.

    # this function returns the name of the customer according the requested format.
    def cust_name(self):
        try:
            csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");

            for row in csv_file:
                all_list.append(row)

            for i in all_list:
                if self.cust_id == (i[0]):
                    self.fname = i[1]
                    self.lname = (i[2])

                    print(f'{self.fname} {self.lname}')
                    break


        except FileNotFoundError as e:
            print(f"Could not find {FILENAME} file.")

    # this function returns the full address of the customer as requested in the example.
    def cust_fullAddress(self):
        try:
            csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");

            for row in csv_file:
                all_list.append(row)

            for i in all_list:
                if self.cust_id == (i[0]):
                    self.company = i[3]
                    self.stret = i[4]
                    self.city = i[5]
                    self.state = i[6]
                    self.zipcode = i[7]

                    print(f'{self.company} \n'
                          f'{self.stret} \n'
                          f'{self.city} {self.state} {self.zipcode}')
                    break

                else:
                    pass
        except FileNotFoundError as e:
            print(f"Could not find {FILENAME} file.")

    # this function returns the customer ID.
    def cust_ID(self):
        try:
            csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");

            for row in csv_file:
                all_list.append(row)
            for i in all_list:
                if self.cust_id == (i[0]):
                    x = self.cust_id
                    print(x)
                    break
                else:
                    pass
        except FileNotFoundError as e:
            print(f"Could not find {FILENAME} file.")

    # this function returns the customer company.
    def cust_company(self):
        try:
            csv_file = csv.reader(open("customers_1.csv", "r"), delimiter=",");

            for row in csv_file:
                all_list.append(row)
            for i in all_list:
                if self.cust_id == (i[0]):
                    self.company = (i[3])
                    a = self.company
                    print(a)
                    break
                else:
                    pass
        except FileNotFoundError as e:
            print(f"Could not find {FILENAME} file.")


# this main function is additionally made to demonstrate the execution of the above functions.

cust1 = Customer()

cust1.cust_id = '109'

cust1.cust_ID()
cust1.cust_fullAddress()
