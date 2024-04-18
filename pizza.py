print("Thank you for choosing Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M, or L")  # What size pizza do you want? S, M, or L
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N")  # Do you want pepperoni? Y or N
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N")  # Do you want extra cheese? Y or N
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill:.2f}")
