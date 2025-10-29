from game.io import prompt_guess
from game.secret import generate_secret
from game.validate import is_valid_guess,is_new_guess

def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            for j in range(4):
                if guess[i] == secret[j]:
                    cows += 1
    result = (bulls,cows)
    return result

def is_won(bulls: int, length: int) -> bool:
    return bulls == length


def init_state(secret: str, length: int) -> dict:
    max_tries = int(input("Enter max tries"))
    game_state = {
        "secret": secret,
        "length": length,
        "max_tries": max_tries,
        "tries_used": 0,
        "bulls": 0,
        "cows": 0,
        "history": [],
        "seen": set()
    }
    return game_state

def apply_guess(state: dict, guess: str,) -> tuple[int, int]:
    if not is_new_guess(guess,state["seen"]):
        state["seen"].add(guess)
        state["tries_used"] += 1
    bulls_cows = score_guess(state["secret"],guess)
    state["history"].append((f"guess: {guess}",bulls_cows[0],bulls_cows[1]))
    state["bulls"] += bulls_cows[0]
    state["cows"] += bulls_cows[1]
    return bulls_cows



