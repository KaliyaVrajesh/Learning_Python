import random
import time


operators = ["-","+","*"]
min_operand = 3
max_operand =12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    oeprator = random.choice(operators)

    expr = str(left)+" " + oeprator+" " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input ("Press enter to start!")
print("___________________________")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i+1) + ": " + expr + " : ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round( end_time - start_time, 2)

print("______________________________")

print("Nice work! You finished in",total_time,"seconds")