import requests


def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']  # Повертаємо курс обміну
        else:
            raise ValueError("Не вдалося отримати курс валют.")
    else:
        raise ConnectionError(f"Помилка підключення до API НБУ: {response.status_code}")

def convert_to_uah(amount, currency_code):
    try:
        rate = get_exchange_rate(currency_code)
        return amount * rate
    except Exception as e:
        print(f"Помилка: {e}")
        return None

def main():
    supported_currencies = {"EUR": "Євро", "USD": "Долар США", "PLN": "Польський злотий"}

    print("Програма конвертації валют в українську гривню")
    print("Доступні валюти: EUR, USD, PLN")

    currency_code = input("Введіть код валюти (EUR, USD, PLN): ").strip().upper()
    if currency_code not in supported_currencies:
        print("Неправильний код валюти. Спробуйте знову.")
        return

    try:
        amount = float(input("Введіть кількість валюти: "))
        if amount <= 0:
            print("Кількість повинна бути більше нуля.")
            return
    except ValueError:
        print("Неправильне значення. Введіть число.")
        return

    converted_amount = convert_to_uah(amount, currency_code)

    if converted_amount is not None:
        print(f"{amount} {currency_code} = {converted_amount:.2f} UAH")

if __name__ == "__main__":
    main()