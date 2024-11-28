import requests

from config import API_KEY, API_URL

class APIException(Exception):
    """Класс для пользовательских исключений."""
    pass

class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        """Получение стоимости валюты."""
        # Проверка на одинаковые валюты
        if base == quote:
            raise APIException("Невозможно перевести одинаковые валюты.")

        # Проверка числа
        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Количество должно быть числом.")

        # Запрос к API
        try:
            response = requests.get(f"{API_URL}latest", params={"access_key": API_KEY})
            response.raise_for_status()
            data = response.json()

            # Проверка на ошибки в данных
            if "error" in data:
                raise APIException(data["error"]["info"])

            rates = data.get("rates", {})
            if base not in rates or quote not in rates:
                raise APIException(f"Валюта {base} или {quote} не найдена.")

            # Вычисление стоимости
            base_rate = rates[base]
            quote_rate = rates[quote]
            return round((quote_rate / base_rate) * amount, 2)
        except requests.exceptions.RequestException as e:
            raise APIException(f"Ошибка сети: {e}")
        except KeyError:
            raise APIException("Ошибка обработки данных от API.")

    @staticmethod
    def get_currencies():
        """Получение списка доступных валют."""
        try:
            response = requests.get(f"{API_URL}latest", params={"access_key": API_KEY})
            response.raise_for_status()
            data = response.json()

            # Проверка на ошибки в данных
            if "error" in data:
                raise APIException(data["error"]["info"])

            return list(data.get("rates", {}).keys())
        except requests.exceptions.RequestException as e:
            raise APIException(f"Ошибка сети: {e}")
