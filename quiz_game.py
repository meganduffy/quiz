def get_questions():
    with open("quiz_game_sample.txt") as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]

questions = get_questions()
score = 0
total = len(questions)


for question, answer in questions:
    count = 1
    while True:
        guess = raw_input(question)
        if guess == answer:
            score += 1
            break
        elif guess != answer and count > 0:
            count -= 1
            print "One more try!"
            continue
        else:
            print "...incorrect"
            break

print "You got %s out of %s questions right" % (score, total)