def deposit():
    while True:
        my_amount = input("How much deposit do you want : $ ")

        if my_amount.isdigit():
            my_amount = int(my_amount)
            if my_amount > 0 :
                break
            else:
                print("Amount must be greater than o")
        else:
            print("Please enter a number.")

    return my_amount
        

deposit()