MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1


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

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines .")
        else:
            print("Please enter a number.")

    return lines


        
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()