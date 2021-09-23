"""
File: hangman.py
Name: An Lee
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program will play a hangman game with user.
    pre-condition:
    The program will pick up a word randomly as the right answer
    then hide the answer with and show the question.

    post-condition:
    Show user's guess is right or wrong every time until the user win or lose the game.
    One right guess:
    (1)Reveal the right character in the hiding string. (2)The life will not be reduced.
    One wrong guess:
    (1)Maintain the unknown character in hiding string. (2)The life will be reduced 1 time.
    User win:
    When life is bigger than 0 and all the character are answered correctly by user.
    Inform user that he/she win this game and show the correct answer.
    User lose:
    When life is  0 and all the character are not answered correctly by user.
    Inform user 'game over' and show the correct answer.
    """
    ans = random_word()
    # Hide the answer.
    question = show_question(ans)
    life = N_TURNS
    print('The word looks like: '+str(question)+"\n"+'You have '+str(life)+' guesses left.')
    renew_hint = question
    # We must keep playing the game until the user's life reaches 0.
    while life > 0:
        guess = input('Your guess: ').upper()
        check = guess.isalpha()
        next_renew_hint = ''
        # Check whether the character is the illegal format or not.
        # If is not, show the warning and send user back to enter guess again.
        if check is False:
            print('Illegal format.')
        elif len(guess) > 1:
            print('Illegal format.')
        # If the format is fine, then we start to find the guess is a right or wrong one.
        else:
            if ans.find(guess) != -1:
                # If the guess one can be founded in the answer, we rebuild the hint string.
                for i in range(len(ans)):
                    ch = ans[i]
                    # If the guess is match for the character of answer, we show the correct one.
                    if ch == guess:
                        next_renew_hint += guess
                    # If the guess is not included in the character of answer, we maintain the hint string.
                    else:
                        next_renew_hint += renew_hint[i]
            # If the guess is a wrong one, then we reduce the user's life one time.
            else:
                life -= 1
                # We rebuild the string that maintain the previous guess's condition.
                for i in range(len(ans)):
                    ch = renew_hint[i]
                    # If the character has shown before, instead of erase it with'-'.
                    # We must show the right-guess letter before.
                    if ch != '-':
                        next_renew_hint += ch
                    # If the character is '-', we just maintain it.
                    else:
                        next_renew_hint += '-'
                print('There is no ' + str(guess) + '\'s in the word.')
            # Show user the hint and the number of life.
            renew_hint = next_renew_hint
            print('The word looks like: ' + str(renew_hint) + "\n" + 'You have ' + str(life) + ' guesses left.')
        # If number of life is bigger than 0 and all letters of answer are correct, we show win message to user.
        if renew_hint == ans:
            print('You are correct!' + '\n' + 'You win!!' + '\n' + 'The word was:' + ans)
            break
    # If number of life is 0 and all letters of answer are not shown, we show game over message to user.
    if renew_hint != ans:
        print('Oops! game over, the word was: ' + ans)
    else:
        pass


def show_question(ans):
    s = len(ans)
    dashed = ''
    # Each letter of the random word will be replace by '-', in order to hide the answer.
    for i in range(s):
        dashed += '-'
    return dashed


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
