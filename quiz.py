def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("#-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)

        question_num    +=1
    display_score(correct_guesses, guesses)


#-------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("You answered Correct!")
        return 1
    else:
        print("WRONG!")
        return 0
    pass
#-------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("#-------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is : " +str(score)+"%")
#-------------------------
def play_again():

    response = input("wanna go for round 2 ? (Y/N)")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False

#-------------------------
questions = {
    "an welchem fluss liegt emsdetten?: ": "B",
    "wann wurde dHdR gedreht?: ": "A",
    "python ist ...  : ": "C",
}
options = [["A. Rhein", "B. Ems", "C. Weser", "D. Donau"],
           ["A. 1999-2003", "B. 2003-2004", "C. 1969-1972", "D. 2011-2012"],
           ["A. der mond", "B. eine programmiersprache", "C. eine schlange", "D. eine fernsehsendung"]]

new_game()

while play_again():
    new_game()

print("BYE")