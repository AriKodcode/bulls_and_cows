from game.secret import generate_secret
from game.validate import is_valid_guess
from game.logic import is_won,init_state,apply_guess
from game.io import prompt_guess,print_result,print_status,print_feedback

def play(length: int = 4)->None:
    print("wellcome to bulls and cows game! \n good lock!")
    bulls_and_cows = (0,0)
    won = "you lose the game"
    dict1 = init_state(generate_secret(),length)
    game_on = True
    while game_on:
        if is_won(dict1["bulls"],length):
            game_on = False
            won = "you won"
            break
        dict1["bulls"] = 0
        dict1["cows"] = 0
        guess = prompt_guess()
        if is_valid_guess(guess) == (True, "good!"):
            print("nice! try again")
            if guess:
                apply_guess(dict1,guess)
                print_status(dict1)
                print("")
                print_feedback(guess,dict1["bulls"],dict1["cows"])
                print("")
        if dict1["tries_used"] == dict1["max_tries"]:
            break
        else:
            print(is_valid_guess(guess)[1])

    if won == "you won":
        print_result(dict1,won)
    else:
        print_result(dict1,won)





if __name__=="__main__":
    play()