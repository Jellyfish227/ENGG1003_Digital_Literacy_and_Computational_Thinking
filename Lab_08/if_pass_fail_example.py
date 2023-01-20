score = int(input("Please enter your score: "))

if score >= 60:
    print("Passed!")
    print("Congratulations!")

if score < 60:
    print("Failed!")

print("Your score is", score)


score = int(input("Please enter your score: "))

if score >= 60:
    print("Passed!")
    print("Congratulations!")
else:		        # Replaces "if score < 60:"
    print("Failed!")

print("Your score is", score)
