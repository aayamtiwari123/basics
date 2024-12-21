mport random
import sys

a = input("Guess the number! Do you want a range or prefer without a range? Type 'with' or 'without': ").strip().lower()
try1 = 0
try2 = 0

def with_range(r):
    play = 5
    global try1
    lose = 0
    while play > 0:
        num = int(input("Enter number: "))
        if num == r:
            print("You won! Lucky guess!")
            print("Don't get too full of yourself; this is easy mode, noob.")
            return
        if play > 1:  # Only display messages if not the last attempt
            if num > r:
                print("Number is too big, you idiot.")
            elif num < r:
                print("Number is too small, like you.")
        play -= 1
        if play > 0:
            print(f"You still have {play} chances left. Don't cry, ok.")
        elif play == 0:  # On the final attempt
            resetdiff = input("You're on your last chance! Do you want me to reduce the difficulty? (Type 'T' for yes): ").strip()
            if resetdiff.upper() == "T":
                play += 2
                if play > 20:
                    play = 20
                print(f"Difficulty adjusted! You now have {play} chances.")
            else:
                print("You lost here? Do you have anything resembling a brain? I bet you don't.")
                lose += 1
                print(f"The correct answer was {r}")
                if lose > 10:
                    print("You failed here. What is wrong with you? Are you a monkey?")
                try1 += 1
                sys.exit()

def without_range(r):
    play = 5
    global try2
    lose = 0
    print("Just so you won't complain, I'll tell you the range: 1 to 100000000 (1 billion).")
    while play > 0:
        num = int(input("Enter number: "))
        if num == r:
            print("You won! Lucky guess!")
            return
        if play > 1:  # Only display messages if not the last attempt
            if num > r:
                print("Number is too big, you idiot.")
            elif num < r:
                print("Number is too small, like you.")
        play -= 1
        if play > 0:
            print(f"You still have {play} chances left. Don't cry, ok.")
        elif play == 0:  # On the final attempt
            resetdiff = input("You're on your last chance! Do you want me to reduce the difficulty? (Type 'T' for yes): ").strip()
            if resetdiff.upper() == "T":
                play += 2
                if play > 20:
                    play = 20
                print(f"Difficulty adjusted! You now have {play} chances.")
            else:
                print("Haha loser, I knew you would lose.")
                lose += 1
                print(f"The correct answer was {r}")
                if lose > 10:
                    print("Well, try again and again and again till eternity, and you'll still fail.")
                try2 += 1
                sys.exit()

if a == "with":
    n = int(input("What is the range at which you want to end? "))
    if n > 10000000:
        print("Ok, now you're being funny, hehe.")
        sys.exit()
    r = random.randint(1, n)
    with_range(r)
elif a == "without":
    r1 = random.randint(1, 100000000)
    without_range(r1)
else:
    print("Invalid input. Please type 'with' or 'without'.")
    sys.exit()