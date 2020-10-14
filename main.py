import csv #we are importing a database with card details. (card_nr, student vs employee, name, balance)
import os # We import the os module
from card import Card # We import the Card class to use it to validate first the user, and in the end the payment.
from menu import Menu #this imports only the function show from my menu.py file
from beverage import Beverage # we import our Beverage class, to be able to work with it when the user selects a product.
import math # We import math in order to be able to make calculations.
prompt = "> " # the prompt is used in order to tell the user when he needs to input something




#We are asking the user to insert his card
card_nr = input("Please, scan your card " + prompt)
with open("card.csv") as csvfile:
    #here we openned the csv file, and with delimiter we are saying that inside the csv the different values are delimited by comas.
    reader = csv.reader(csvfile, delimiter=",")
    #Now we are findig the rows in the reader. We are validating the card.
    valid_card_id = "" #We are creating an empty string to see if the ID is good or not
    for row in reader: #read the row
        if card_nr == row[0]:
            print("Hi, " + row[2]) #Here we told our programme that if the card id number (sacnned card) it is find in the first row of our csv file, then the user can continue to the next step.
            valid_card_id = card_nr #we are seting a variable.
            card = Card(card_nr, row[1], row[2], row[3]) #I am initializing my valid card if the condition of valid card id is true.
            break

csvfile.close()  #With this function we close our csv file in order not to overwrite information during the order.

if valid_card_id == "": # It cannot find the valid card id, because the initial value did not change
    print("Sorry, this is not a valid card, please insert a valid KEA Student or KEA employee card")
    exit(0)

if card.balance < 20: #if the card balance is below 20 kr the user will not be able to continue with his or her order
    print("Your balance is below 20 kr, please top up")
    exit(0)
else:
    Menu.show() #here the menu shows,from the Menu class that we have imported

print("Have a great day,  " + row[2] + ". Looking forward to see you again!")


price_of_coffee = Menu.Returnfunc() # We use the return function we sat in the Menu class in order to give us the finl price of the beverage.

with open("card.csv") as csvfile:
    #here we openned the csv file, and with delimiter we are saying that inside the csv the different values are delimited by comas.
    reader = csv.reader(csvfile, delimiter=",") #!!! we tell python what sign is used to delimit the different values within the csv file


    data = [] # We create an empty list in order to store data, meaning balance inside.
    for row in reader: # we are setting to read the rows in or csv file
        data.append(row) # We are appending the date from our csv file's rows in the list we created before.

    i = 0 # We are setting a counter in order to count the rows that we are at.
    for row in data:
        if card.id == row[0]: # We are setting that the first row of our csv file equels the attribute card id from our card class.
            card.pay(price_of_coffee) # We are using our predefined operation in order to make the payment, and change the balance of the person in the csv file.
            data[i] = [row[0], row[1], row[2], float(card.balance)] # Here we are setting that the 4th row in our csv file equals the balance in the card class.
        i+=1 # When we change to the new line to the csv file, the computer memorisez the number of the row we are at.

csvfile.close()  # Here we close our csv fle.


with open('card.csv', mode='w', newline='\n') as myfile: # Here we open and create a copy of our csv file, and we name it as myfile.
    writer = csv.writer(myfile, delimiter=',') # we set the delimiter for our new file. And we also are abble to write on it now.

    for row in data:
        writer.writerow(row) #We overwrite the new balance and we merge the two files.

myfile.close() # We close the csv file.
print("Your new balance is " + str(card.balance) + "kr") # We print out the new balance.
