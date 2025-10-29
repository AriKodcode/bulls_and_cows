def prompt_guess() -> str:
    guess = input("Press 4 numbers between 1 - 9")
    return guess

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"guess: {guess}, bulls: {bulls}, cows: {cows}")


def print_status(state_game_state) -> None:
    print(state_game_state)


def print_result() -> None:

