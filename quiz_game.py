print("Welcome to this quiz game!")

score = 0
count = 3
name = input("What is your name? ")
print("Hello " + name + ", let's play :)")


answer = input("What is Duc's favourite food? ")
if answer.lower() == "pho":
    print("Correct!")
    score += 1
else:
    print("Incorrect! How can you not know it????")

answer = input("What is Duc's favourite animal ")
if answer.lower() == "dog":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is 9 + 10? ")
if answer == "21":
    print("Wow, Correct!")
    score += 1
else:
    print("No, it's 21")

print(f"You got {score} correct out of {count}")
# Only the first 4 Characters of the string
print(f"You got " + str((score / 3) * 100)[:4] + "%.")

