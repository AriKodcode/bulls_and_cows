def score_guess() -> tuple[int, int]:

def is_won() -> bool:


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


def apply_guess() -> tuple[int, int]:



