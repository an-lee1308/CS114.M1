def solve(number_legs, number_heads):
    for number_chickens in range(0, number_heads + 1):
        number_dogs = number_heads - number_chickens 
        total_legs = 4 * number_dogs + 2* number_chickens 
        if total_legs == number_legs: 
           return [number_dogs, number_chickens] 
    return[None, None] 

def animals():
    heads, legs = map(int, input().split())
    dogs, chickens = solve(legs, heads)
    if dogs == None:
       print('Khong the tim ra ket qua')
    else:
        print(chickens,dogs)
animals()