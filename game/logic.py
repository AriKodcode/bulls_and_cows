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
    if bulls == length:
        return True
    else:
        return False


game_state = {
  "secret": str,
  "length": int,
  "max_tries": int | None,
  "tries_used": int,
  "unique_digits": bool,
  "allow_leading_zero": bool,
  "history": list[tuple[str, int, int]],
  "seen": set[str]
}

def init_state() -> dict:
    return {}

def apply_guess() -> tuple[int, int]:
    return (3,3)


