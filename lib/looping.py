#!/usr/bin/env python3

"""# while loop
i = 0
while i < 5:
    print(f"{i} Looping!")
    i += 1

# for loop
for i in range(10):
    print("Looping")
    print(f"i is {i}")

player_heights = [
    0.008,
    0.008,
    0.008,
    0.009,
    0.008,
    0.01,
    0.009,
    0.009,
    0.01,
    0.008,
    0.009,
    0.009,
    0.008,
    0.008,
    0.008,
    0.009,
    0.008,
    0.009,
    0.01,
    0.01,
]

inch_heights = list()
for height in player_heights:
    inch_height = height * 7920
    inch_heights.append(inch_height)

player_heights=[height*7920 for height in player_heights]
print(player_heights)"""


def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


happy_new_year()


def square_integers(int_list):
    # code goes here!
    return [int_val * int_val for int_val in int_list]


print(square_integers([1, 2, 3, 4, 5]))


def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


fizzbuzz()
