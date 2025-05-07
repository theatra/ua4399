import random

number = random.randint(1, 100)
print(number)

print("I've conceived a number between 1 and 100, fancy guessing?")

def ask_user():
    try:
        user_version = int(input("So, your best guess is..."))
        return int(user_version)
    except ValueError as e:
        print("Only numbers are allowed!")
    ask_user()

attempt_count = 9

for attempt in range(10):
    if ask_user() == number:
        print("Witchcraft! You guessed!")
        break
    else:
        print(f"Nope. You've got {attempt_count} attempts left")
        attempt_count -=1
        if attempt_count < 0:
            print("Seemingly, your intuition needs some 'me time'.")
        continue
