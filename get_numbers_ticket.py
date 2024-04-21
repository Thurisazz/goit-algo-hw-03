import random

def get_numbers_ticket(min, max, quantity):  
    while True:    
        try:
                min = int(min)
                max = int(max)
                quantity = int(quantity)
            
                if min < 1 or min > max or max > 1000 or quantity < 1 or quantity > ((max + 1) - min):
                    print("Incorect values")
                    return []                   
                numb = random.sample(range(min, max + 1), quantity)    
                sort = sorted(numb)
                print("Your lottery numbers", sort)
                return sort
        except ValueError:
            print("You entered a number, not a letter.")
            return []
        

in_min = input("Min number: ")
in_max = input("Max number: ")
in_quantity = input("Quantity: ")

get_numbers_ticket(in_min, in_max, in_quantity)
