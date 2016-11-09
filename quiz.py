def write_questions():
    print "Welcome, please add 3 questions and answers to the quiz..."
    with open("questions.txt", "a") as f:
        count = 2
        while count > 0:
            question = raw_input("Add your question here:")
            count -= 1
            if not question:
                break
            answer = raw_input("Add the answer to your question here:")
            if not answer:
                break
            f.write(question)
            f.write("\n")
            f.write(answer)
            f.write("\n")
write_questions()

def get_questions():
    with open("questions.txt") as f:
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

