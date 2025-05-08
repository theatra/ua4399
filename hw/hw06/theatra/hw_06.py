# Task 1
by_2 = [x for x in range(10) if x % 2 == 0]
odd = [x for x in range(10) if x % 2 != 0]
not_by_3_or_2 = [x for x in range(10) if x % 2 != 0 and x % 3 != 0]
print(by_2, odd, not_by_3_or_2)

# Task 2
login = input("Please enter your login here: ")

while login != "First":
    print("Sorry, invalid login.")
    break
else:
    print("Hello, dear!")