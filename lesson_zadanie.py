from _datetime import datetime
import logging


class Greeter:
    def greet(self, name):
        name = name.rstrip()
        name = name.lstrip()
        name = name.title()
        greet = 'Привет'
        hour_str = datetime.now().hour
        if 0 <= hour_str < 6 or 22 <= hour_str < 0:
            greet = 'Доброй ночи'
        if 6 <= hour_str < 12:
            greet = 'Доброе утро'
        elif 20 <= hour_str < 22:
            greet = 'Добрый вечер'
        result = greet + ' ' + name
        logging.warning(result)
        return result