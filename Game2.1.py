import math
import random
from functools import reduce


def lcm(a, b):
    """Вычисляет наименьшее общее кратное двух чисел."""
    return abs(a * b) // math.gcd(a, b)


def lcm_multiple(numbers):
    """Вычисляет НОК для списка чисел."""
    return reduce(lcm, numbers)


def main():
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    print("Find the smallest common multiple of given numbers.")

    score = 0
    rounds = 3

    for _ in range(rounds):
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = lcm_multiple(numbers)

        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return  # Завершение игры при ошибке

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()