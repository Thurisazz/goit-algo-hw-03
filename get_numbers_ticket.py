import random

def get_numbers_ticket():
    while True:
        try:
            in_min = int(input("Min number: "))
            in_max = int(input("Max number: "))
            in_quantity = int(input("Quantity: "))
            numb = random.sample(range(in_min, in_max), in_quantity)
            sort = sorted(numb)
            print("Your lottery numbers", sort)
            return sort
        except ValueError:
            print("Please enter a number, not a letter.")
        



get_numbers_ticket()
#except ValueError:
#    print("Enter th number")