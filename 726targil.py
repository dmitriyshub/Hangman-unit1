
"""Choose from following options:

1: print your list
2: print how much items in your list
3: check if item in list
4: check how much times the item in list


"""

def targil():

    user_string = input("Please input your shoping list (Items must be separated by ','): ")
    user_list = user_string.split(',')
    count_goods = len(user_list)
    power = True

    while power == True:
        user_number = int(input("Please press a number from 1 - 9: "))
        answer3 = ""
        answer4 = ""
        if user_number == 1:
            print("Your list: ", user_list)

        elif user_number == 2:
            print("Number of items in list: ", count_goods)

        elif user_number == 3:
            answer3 = input("Find item in list: ")

            if answer3 in user_list:
                print(answer3, "is in list")
            else:
                print("The item not in list!")

        elif user_number == 4:
            answer4 = input("Count specific item: ")
            print(user_list.count(answer4), "from this item in list!")

        elif user_number == 5:
            print("")

        elif user_number == 9:
            print("Goodbay!")
            power = False

targil()







