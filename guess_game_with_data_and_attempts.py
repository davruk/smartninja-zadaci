import json
import random
import datetime
current_time = datetime.datetime.now()
print(current_time)

player = input("Hi, what is your name?")

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    score = json.loads(score_file.read())
    print("Top scores: " + str(score))

for score_dict in score:
    print(str(score_dict["attempts"]) + "attempts, date:" + score_dict.get("date"))
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        with open("score.txt", "w") as score_file:
            score_file.write(json.dumps(score))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
