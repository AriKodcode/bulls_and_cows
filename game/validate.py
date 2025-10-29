def is_valid_guess(guess: str, length: int = 4, *, unique_digits: bool = True) -> tuple[bool, str]:
    check_guess = ""
    result = ()
    while len(check_guess) != 4:
        for num in guess:
            if not num.isdigit():
                result = (False, guess)
                break
        if result == (False, guess):
            break
        if len(guess) != length:
            result = (False, guess)
            break
        else:
            for num in guess:
                if num in check_guess:
                    result = (False, guess)
                    break
                else:
                    check_guess += num
            if len(check_guess) == 4:
                result = (True, guess)
            break
    return result

def is_new_guess(guess: str, history: set[str]) -> bool:
    if guess in history:
        return False
    else:
        return True
