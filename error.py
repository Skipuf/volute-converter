class Not_Found_Exception(Exception):
    def __str__(self):
        return "Указанная валюта не найдена!"


class Сount_Exception(Exception):
    def __str__(self):
        return "Число не может быть меньше нуля!"


class Syntax_Exception(Exception):
    def __str__(self):
        return "Неправильный синтаксис команды!"