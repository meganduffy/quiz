import sys

def get_questions():
    with open("questions.txt", "a+") as f:
        f.write("\n")
        f.writelines(raw_input("Add your own question here:"))
        f.write("\n")
        f.writelines(raw_input("Add the answer to your question here:"))
        f.writelines("\n")
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]

questions = get_questions()
trys = 3
score = 0
total = len(questions)


for question, answer in questions:
    guess = raw_input(question)
    while trys > 0:
        if guess == answer:
            score += 1
        else:
            trys -= 1
print "You got %s out of %s questions right" % (score, total)