import random as rand #to generate the instances 

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5,
}

symbol_value = {
    "A": 6,
    "B": 4,
    "C": 3,
    "D": 2,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range (symbol_count):
            all_symbols.append(symbol)

    columns = [] 
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = rand.choice(current_symbols)
            current_symbols.remove(value)

            column.append(value)

        columns.append(column)

    return columns

def check_winnings(columns, lines, bet, values):
    for line in range(lines):

        winnings = 0
        winnings_lines = []

        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                symbol = None
                break
            else:
                winnings += values[symbol] * bet
                winnings_lines.append(line + 1)

        return winnings, winnings_lines


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end = " ")

            else:
                print(column[row])


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

def get_bet():
    while True:
        my_amount = input("What would you like to bet on each line? $ ")
        if my_amount.isdigit():
            my_amount = int(my_amount)
            if MIN_BET <= my_amount <= MAX_BET:
                break

            else:
                print(f" Amount must be between $ {MIN_BET} - $ {MAX_BET} .")
        else:
            print("Please enter a Number.")

    return my_amount
          
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Sorry, you only have ${balance} left. You can't bet ${total_bet}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is : $ {total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print (f"You won ${winnings} !")
    print(f"Winning lines: ", *winnings_lines)


main()
