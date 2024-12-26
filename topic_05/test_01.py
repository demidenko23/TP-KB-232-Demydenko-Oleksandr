import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (
        (user_choice == "stone" and computer_choice == "scissor") or
        (user_choice == "scissor" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "stone")
    ):
        return "Ви виграли!"
    else:
        return "Комп'ютер виграв!"

def main():
    choices = ["stone", "scissor", "paper"]

    print("Гра: Камінь, ножиці, папір")
    user_choice = input("Введіть ваш вибір (stone, scissor, paper): ").strip().lower()

    if user_choice not in choices:
        print("Неправильний вибір! Спробуйте знову.")
        return

    computer_choice = random.choice(choices)

    print(f"Ваш вибір: {user_choice}")
    print(f"Вибір комп'ютера: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
