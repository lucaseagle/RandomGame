from random import randint


def shoot(a, b):
    if a > b:
        return "My random number is bigger"
    elif a < b:
        return "My random number is smaller"
    else:
        return "You made it!"


sample = 0

a = input("Enter the first number range from which the number will be drawn: ").split(maxsplit=2)
x = randint(int(a[0]), int(a[1]))

while True:
    sample += 1
    user = int(input("Type your guess: "))
    print(shoot(x, user))
    if x == user: break

print("You got in {} attempts".format(sample))
