# your code goes here!
import time

def countdown(wait):
    x = wait
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(wait):
    x = wait
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

countdown(5)
