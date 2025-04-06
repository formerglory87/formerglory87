import random
counter = 0
die = ""
rolls_needed = 0
adventurer_name = ""

# which die is being rolled
print("Hello adventurer, what is your name.")
adventurer_name = input("")

print("Hello "+ adventurer_name +", May the dice gods smile upon you this day.")
print("Which die would you like to roll?")

die = input()

# How many roles are needed of the die.
print("How many do you need to roll?")

rolls_needed = int(input())

#code for the dice to be rolled.

if die == "D20" or "d20":
    while counter < rolls_needed:
        result = random.randint(1,20)
        print(result)
        counter+= 1

elif die == "D12" or "d12":
    while counter < rolls_needed:
        result = random.randint(1,12)
        print(result)
        counter += 1

elif die == "D10" or "d10":
    print("Do you want uppers, lowers, or both?")
    input()
    while counter < rolls_needed:
        
        if "uppers":
            result = random.randint(1,9)
            print(result * 10)
            counter += 1

        elif "lowers":
            result = random.randint(0,9)
            print(result)
            counter += 1
        elif "both":
            result = random.randint(10,90) + random.randint(0,9)
            print(result)
            counter += 1

elif die == "D8" or "d8":
    while counter < rolls_needed:
        result = random.randint(1,8)
        print(result)
        counter += 1

elif die == "D6" or "d6":
    while counter < rolls_needed:
        result = random.randint(1,6)
        print(result)
        counter += 1

elif die == "D4" or "d4":
    while counter < rolls_needed:
        result = random.randint(1,4)
        print(result)
        counter += 1

else:
    print("That was not an option, choose again.")