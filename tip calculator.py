
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip_percentage = input(
    "What percentage tip would you like to give? 10, 12 or 15? ")
persons = input("How many people to split the bill? ")

bill_number = float(bill)
tip = int(tip_percentage) / 100
total = bill_number * (1 + tip)
persons_num = int(persons)

person_cheque = round(total / persons_num, 2)
person_cheque = "{:.2f}".format(person_cheque)

print(f"Each person should pay: ${person_cheque}")
