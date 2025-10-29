def prompt_guess() -> str:
    guess = input("Press 4 numbers between 1 - 9")
    return guess

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"guess: {guess}, bulls: {bulls}, cows: {cows}")


def print_status(state_game_state) -> None:
    print(f"Summary: \n tries used: {state_game_state["tries_used"]} \n history: {state_game_state["history"]}")


def print_result(state_game_state, won: bool) -> None:
    print(f"you win! The secret numbers is: {state_game_state["secret"]}  ")
