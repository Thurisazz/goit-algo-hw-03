import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1:
        return ""
    numb = random.sample(range(min, max), quantity)
    sort = sorted(numb)
    return sort


lottery_numbers = get_numbers_ticket(1, 200, 5)
print("Ваші лотерейні числа:", lottery_numbers)
