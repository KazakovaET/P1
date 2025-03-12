import random


def generate_geometric_progression(length):
    """Генерирует геометрическую прогрессию заданной длины."""
    start = random.randint(1, 10)  # Начальное число
    ratio = random.randint(2, 5)  # Коэффициент прогрессии
    progression = [start * (ratio ** i) for i in range(length)]
    return progression


def main():
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    print("What number is missing in the progression?")

    score = 0
    rounds = 3

    for _ in range(rounds):
        length = random.randint(5, 10)  # Длина прогрессии от 5 до 10
        progression = generate_geometric_progression(length)

        missing_index = random.randint(0, length - 1)
        correct_answer = progression[missing_index]

        progression[missing_index] = '..'

        print(f"Question: {' '.join(map(str, progression))}")

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