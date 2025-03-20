import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

lottery_number = random.sample(lottery_pool, 4) + [random.choice(['A', 'B', 'C', 'D', 'E'])]
random.shuffle(lottery_number)  

lottery_number_str = ''.join(map(str, lottery_number))

user_input = input("Enter your lottery number (four numbers and one letter, e.g., 3B291): ")

if user_input.upper() == lottery_number_str:
    print("Congratulations! You won the lottery!")
else:
    print(f"Sorry, you lost. The winning number was: {lottery_number_str}")

