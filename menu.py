from beverage import Beverage # we import the beverage class in order to use it in our menu

import os # We import the os module
prompt = "> " # the prompt is used in order to tell the user when he needs to input something
import math # We imput the math module, in order to be able to make calculations

class formats: # makes a class to change format and colors in the printed menu
    red = '\033[91m'
    green = '\033[92m'
    purple = '\033[95m'
    bold = '\033[1m'
    complete = '\033[0m'

class Menu: # We create a class called Menu, where the user will be able to chose and personalize its beverage
    def show(): # We define show as a function to be able to print our actual menu, the one that the user should see in the screen.
        os.system('cls') # It clears the terminal in order for the menu to show up.
        # Now we are going to show the user the actual options he/she can chose with all the extras.
        print(formats.bold + formats.red + """
         _________________________________________________________________________________________________________
        ¦                                                M E N U                                                  ¦
        ¦_________________________________________________________________________________________________________¦
        ¦                                                                                                         ¦
        ¦            Coffees  ☕                                           Teas    🍵                               ¦
        ¦_________________________________________________________________________________________________________¦""" + formats.complete + """
        ¦                                """+formats.bold + formats.red +"""Price (Kr)                                                  Price (Kr)""" + formats.complete + """   ¦
        ¦                                                                                                         ¦
        ¦                                                                                                         ¦
        ¦    1.Double Espresso  ᕦ(ò_óˇ) """+formats.bold+formats.red+"""     10"""+formats.complete+"""                                  6. Black tea   ⚫ """+formats.bold+formats.red+"""       10  """+formats.complete+"""     ¦
        ¦                                                                                                         ¦
        ¦                ~Black as the devil, hot as hell, pure as an angel, sweet as love.~                      ¦
        ¦                                                                                                         ¦
        ¦    2.Americano   🇺🇸 """+formats.bold+formats.red+"""             10"""+formats.complete+"""                                  7. Chamomile Tea 🏵️ """+formats.bold+formats.red+"""   10  """+formats.complete+"""      ¦
        ¦                                                                                                         ¦
        ¦                                  ~Without coffee something’s missing~                                   ¦
        ¦                                                                                                         ¦
        ¦   3.Cappuccino     ☕ """+formats.bold+formats.red+"""              12"""+formats.complete+"""                                 8. Green Tea   💚 """+formats.bold+formats.red+"""       10  """+formats.complete+"""      ¦
        ¦                                                                                                         ¦
        ¦                                ~Learn from yesterday, live for today.~                                  ¦
        ¦                                                                                                         ¦
        ¦    4. Cafe latte    🥛 """+formats.bold+formats.red+"""            12"""+formats.complete+"""                                   9. Rooibos Tea  🌹 """+formats.bold+formats.red+"""     10"""+formats.complete+"""        ¦
        ¦                                                                                                         ¦
        ¦                                    ~Nothing will work unless you do.~                                   ¦
        ¦                                                                                                         ¦
        ¦   5. Cortado   🇪🇸 """+formats.bold+formats.red+"""                 11"""+formats.complete+"""                                   10. Chai Latte   🕉 """+formats.bold+formats.red+"""15  """+formats.complete+"""      ¦"""+formats.green+formats.bold+ """
        ¦_________________________________________________________________________________________________________¦
        ¦                                                                                                         ¦
        ¦               Need a cup?                                                                               ¦
        ¦                           Big   = +Kr5                                                                  ¦
        ¦               Or be sustainable and use your own!                                                       ¦
        ¦_________________________________________________________________________________________________________¦"""+ formats.complete + formats.bold+ """
        ¦                                                                                                         ¦
        ¦                                   🥛 What kind of milk would you like? 🥛                                 ¦
        ¦                                                                                                         ¦
        ¦                                 1. Whole Milk           2. Semi-Skimmed milk                            ¦
        ¦                                                                                                         ¦
        ¦                                   3. Oat milk              4. No milk!                                  ¦
        ¦_________________________________________________________________________________________________________¦""" +formats.complete)

        beverage_nr = input("Please select a beverage: " + prompt) #This used to be int(input(blahblah)). I have changed it to just input and used the "try, except, exit".
        try: #"Try" contains the code that can have an error.
            beverage_nr= int(beverage_nr)# it tests for errors converting input to int
        except: #"Except" will do the following if an error does occur!
            print("Please, select a number between 1 and 10. Please restart your order.")
            exit()
        if beverage_nr < 1 or beverage_nr > 10:
            exit()

        # We create a dictionary for the beverages that might or might not have milk.
        milk_dictionary = {
        1: "Whole milk",
        2: "Semmi-Skinned milk",
        3: "Oat Milk",
        4: "No Milk"
        }
        # We create a dictionary for the beverages that always have milk e.g Cappuccino
        beverage_always_milk_dictionary = {
        1: "Whole milk",
        2: "Semmi-Skinned milk",
        3: "Oat Milk"
        }
        #We create a dictionary for the level of sugar that the user might select.
        sugar_level = {
        1: "Sugar Free",
        2: "Little Sweet",
        3: "Medium Sweet",
        4: "Sweet",
        5: "Very Sweet"
        }   #we create 3 dictionaries for milk, sugar, and beverages with milk, the variables we create need the values from the dictionaries

        #Here is where we use our imported "Beverage"  class, we create a dictionary where we set the atributes for our Beverages, and we also define where the user can and cannot select an option.
        beverage_dictionary = {
        1: Beverage("Double Espresso", "coffee", True, "10", None, False, True, False),
        2: Beverage("Americano", "coffee", True, "10", 1, 1, True, False),
        3: Beverage("Cappuccino", "coffee", True, "12", 2, 2, True, True),
        4: Beverage("Cafe Latte", "coffee", True, "12", 2, 2, True, True),
        5: Beverage("Cortado", "coffee", True, "11", 1, 2, True, True),
        6: Beverage("Black tea", "tea", True, "11", 1, 1, True, False),
        7: Beverage("Chamomile tea", "tea", True, "10", None, False, True, False),
        8: Beverage("Green tea", "tea", True, "10", None, False, True, False),
        9: Beverage("Rooibos tea", "tea", True, "11", None, 1, True, False),
        10: Beverage("Chai latte", "tea", True, "15", 2, 1, True, True)
        }   #a beverage dictionary that uses the "Beverage" class parameters in order to create it's values

        selected_beverage = beverage_dictionary.get(beverage_nr) # We set a variable that gets the number of the beverage which the user has inputed
        print("You have selected: " + selected_beverage.name) #We print the beverage that the user has selected.
        print(f"Your {selected_beverage.variant} costs {selected_beverage.price} Kr") #We use a formated print in order to tell the user if he selected a coffee or a tea, and the name of the product.

         # We are creating and if statement in order to be able to select drinks with milk or without.
        if selected_beverage.milk == None: # Here we setting to skip the milk question if the beverage cannot contain milk.
            pass


        elif selected_beverage.milk == 1: # Here we take only the beverages that might contain  milk and ask the user which type of milk they would like,or they also have an option when they do not want milk..
            print(f"Choose a type of milk pls: {milk_dictionary} ")
            selected_milk = int(input())
            if selected_milk == 1:
                print("You selected " + milk_dictionary.get(selected_milk) + " type of milk")
            elif selected_milk == 2:
                print("You selected " + milk_dictionary.get(selected_milk) + " type of milk")
            elif selected_milk == 3:
                print("You selected " + milk_dictionary.get(selected_milk) + " type of milk")
            elif selected_milk == 4:
                print(f"You dont want milk in your {selected_beverage.name}")
            else:
                print("You are cancelling your order")
                quit()
        elif selected_beverage.milk == 2: # Here we take only the beverages that contain always milk and ask the user which type of milk they would like.
            print(f"Choose a type of milk pls: {beverage_always_milk_dictionary} ")
            selected_milk = int(input())
            if selected_milk == 1:
                print("You selected " + beverage_always_milk_dictionary.get(selected_milk) + " type of milk")
            elif selected_milk == 2:
                print("You selected " + beverage_always_milk_dictionary.get(selected_milk) + " type of milk")
            elif selected_milk == 3:
                print("You selected " + beverage_always_milk_dictionary.get(selected_milk) + " type of milk")
            else:
                print("You are cancelling your order")
                quit()
        else:
            print("Thiat was not a right option, please start again") # This is no to break the code.

            #We sat the conditions for the possible answers and print out the user's choice.
        print(formats.purple+formats.bold+ """
         _________________________________________________________________________________________________________
        ¦                                                                                                         ¦
        ¦                                    Please, tell me how sweet you are:  💛                                ¦
        ¦                                                                                                         ¦
        ¦                               1         2          3          4            5                            ¦
        ¦                              <O=========O==========O==========O============O>                           ¦
        ¦                            SugarFree   little     medium      sweet       VERY                          ¦
        ¦                                                                                                         ¦
        ¦                                                                                                         ¦
        ¦_________________________________________________________________________________________________________¦
        """ + formats.complete)

        selected_beverage.sugar = input(prompt) #sugar level determined by sugar dictionary, input function takes str

        try:
            selected_beverage.sugar= int(selected_beverage.sugar)# it tests for errors converting input to int
        except:
            print("Please, select a number between 1 and 5. Please restart your order.")
            exit()
        if selected_beverage.sugar < 1 or selected_beverage.sugar > 5:
            print("Please, select a number between 1 and 5. Please restart your order.")
            exit()
        #converted str is used to determine sugar_level_selected from sugar_level dictionary
        sugar_level_selected = sugar_level[selected_beverage.sugar]
        print(f"You selected your {selected_beverage.name} to be {sugar_level_selected}") # We tell the user the amount of sugar he/she selected into his/her beverage, using a formated print.

        decor_choice = "Impossible to make a decor on the coffee you ordered!"
        if selected_beverage.decor == True:
            decor_choice = input(f"Would you like decoration on your {selected_beverage.name}, please specify Yes or No" + prompt)

            if decor_choice.upper() == "YES": #We use the funvtion .upper in order to make sure that the user has inputed the desired resposne , whether or not it has inputed capital leters.
                print(f"You will get a KEA logo on your {selected_beverage.variant}")
            else:
                print("Your coffee will not have any decoration")
        else:
            decor_choice = "NONE"
            pass

        own_cup = input("Would you like to use your own cup to be sustainable? Please tap in 'yes' to confirm " + prompt)
        if own_cup.upper() == "YES": #a variable that asks the user if he/she brought her own cup; can be skipped entirely if input equals "No"
            print("Please, prepare your cup and place it in the designated place in the machine")
            print(f"Your {selected_beverage.name} will be served in your own cup, THANK YOU for taking care of our world")
        else:
            own_cup = "NO"
            pass
        global new_size_price  #global new_size_price used to for payment function
        new_size_price = int(selected_beverage.price) #variable that converts price str to int for calculation of final coffee price
        big_size = input(f"Would you like your {selected_beverage.name} double for only extra 5 kr? Please tap in 'yes' to confirm" + prompt )
        if big_size.upper() == "YES":
            new_size_price += 5 #calculation of the new_size_price, here is where we use the imported math.
            print(f"Your {selected_beverage.name} now is double ammount for" + str(new_size_price) + "kr")
            selected_beverage.price = new_size_price
        else:
            big_size = "NO"
            pass

        if selected_beverage.milk == None:
               print(f"""
                     -You order is:-
               Product type: {selected_beverage.variant}
                Product name: {selected_beverage.name}
                   Sugar: {sugar_level_selected}
         Decoration: {decor_choice}
                  Sustainability: {own_cup}
                  Bigger Size: {big_size}
                 """)
        elif selected_beverage.milk == 1:
            print(f"""
                  -You order is:-
            Product type: {selected_beverage.variant}
             Product name: {selected_beverage.name}
             Milk: {milk_dictionary[selected_milk]}
                Sugar: {sugar_level_selected}
                Decoration: {decor_choice}
               Sustainability: {own_cup}
               Bigger Size: {big_size}
              """)
        elif selected_beverage.milk == 2:
          print(f"""
                      -You order is:-
          Product type: {selected_beverage.variant}
           Product name: {selected_beverage.name}
           Milk: {beverage_always_milk_dictionary[selected_milk]}
              Sugar: {sugar_level_selected}
              Decoration: {decor_choice}
             Sustainability: {own_cup}
             Bigger Size: {big_size}
            """)
            #These last three conditions, will show the final product with all the user choices.

    def Returnfunc(): #This function is used in the main file in order to substract the price of the beverage from the user's balance.
        return new_size_price
