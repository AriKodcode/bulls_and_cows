def is_valid_guess(guess: str, length: int = 4, *, unique_digits: bool = True) -> tuple[bool, str]:
    check_guess = ""
    result = ()
    while len(check_guess) != 4:
        for num in guess:
            if not num.isdigit():
                result = (False, "pleas input numbers only")
                break
        if result == (False, "pleas input numbers only"):
            break
        if len(guess) != length:
            result = (False, "not input 4 numbers")
            break
        else:
            for num in guess:
                if num in check_guess:
                    result = (False, "Error. You entered two identical numbers.")
                    break
                else:
                    check_guess += num
            if len(check_guess) == 4:
                result = (True, "good!")
            break
    return result

def is_new_guess(guess: str, history: set[str]) -> bool:
    if guess in history:
        return False
    else:
        return True
