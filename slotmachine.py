import random



MAX_LINES =3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count= {
    "A" : 3,
    "B" : 3,
    "C" : 3,
    "D" : 3
}
symbol_value= {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line +1)
        
    return winnings, winnings_lines



def getslotmachinespin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column =[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()





def deposit():
    while True:
        amount = input("what would you like to deposit $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a number")
    return amount

def numberoflines():
    while True:
        nooflines = input("enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if nooflines.isdigit():
            nooflines=int(nooflines)
            if 1<=nooflines<=MAX_LINES:
                break
            else:
                print("enter a valid no of lines")
        else:
            print("please Enter a number")
    return nooflines


def getbet():
    while True:
        amount = input("what would you like to bet on each line$")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Enter a number")
    return amount


def spin(balance):
    nooflines = numberoflines()
    while True:    
        bet=getbet()
        totalbet=bet*nooflines
        if totalbet > balance:
            print(f"you dont have enough money to bet on,your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on lines{nooflines}.Total bet is equal to: ${totalbet}")
    
    slots = getslotmachinespin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,nooflines,bet,symbol_value)
    print(f"You win ${winnings}.")
    print(f"You win on lines:",*winning_lines)
    return winnings-totalbet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is:${balance}")
        answer= input("press enter to spin(q to quit)")
        if spin == "q":
            break
        balance+=spin(balance)

    print(f"you left with ${balance}")

    

main()
