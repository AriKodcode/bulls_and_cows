import random


def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False,
                    rng: random.Random | None = None) -> str:
    secret_nums = ""
    list_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while len(secret_nums) != 4:
        num = list_nums[random.randrange(len(list_nums))]
        if num not in secret_nums:
            secret_nums += num
    return secret_nums


print(generate_secret())
