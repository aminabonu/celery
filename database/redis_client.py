from redis import Redis
import random


class RedisDb:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_site = Redis(
            host=host,
            port=port,
            db=db
        )

    # Одноразовые генерация кодов подтверждения
    def generate_verify_code(self, user_phone_number):
        verify_code = random.randint(1212, 9999)

        # создаем временный ключ на 60 секунд
        self.redis_site.set(user_phone_number,
                            verify_code,
                            60)

        return verify_code

    def check_verify_code(self, user_phone_number, user_input):
        # Получаем значение отправленное пользователю по номеру
        checker = self.redis_site.get(user_phone_number)

        if checker and checker == str(user_input):
            return True

        return False
