from abc import ABC, abstractmethod
from typing import Optional


class MusicalInstrument(ABC):
    """
    Базовый класс для всех музыкальных инструментов.

    Attributes:
        name (str): Название инструмента
        brand (str): Бренд производителя
        price (float): Цена инструмента в рублях
        _year_of_manufacture (int): Год выпуска (непубличный атрибут)
    """

    def __init__(self, name: str, brand: str, price: float, year: int) -> None:
        """
        Инициализация музыкального инструмента.

        Args:
            name: Название инструмента
            brand: Бренд производителя
            price: Цена инструмента
            year: Год выпуска
        """
        self.name = name
        self.brand = brand
        self.price = price
        self._year_of_manufacture = year  # Инкапсуляция: год выпуска не должен меняться после создания

    def __str__(self) -> str:
        """Возвращает строковое представление инструмента."""
        return f"{self.brand} {self.name} - {self.price} руб. ({self._year_of_manufacture} г.)"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление для отладки."""
        return f"MusicalInstrument(name='{self.name}', brand='{self.brand}', price={self.price})"

    def play(self) -> str:
        """
        Базовый метод извлечения звука.

        Returns:
            str: Описание звучания инструмента
        """
        return f"Играет {self.name}"

    def tune(self) -> str:
        """
        Настройка инструмента.

        Returns:
            str: Сообщение о настройке
        """
        return f"{self.name} настроен"

    def get_age(self) -> int:
        """
        Вычисляет возраст инструмента.

        Returns:
            int: Возраст инструмента в годах
        """
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self._year_of_manufacture


class Guitar(MusicalInstrument):
    """
    Класс гитары, наследующийся от MusicalInstrument.

    Additional Attributes:
        strings_count (int): Количество струн
        guitar_type (str): Тип гитары (акустическая, электро, бас)
        _is_tuned (bool): Настроена ли гитара (непубличный атрибут)
    """

    def __init__(self, name: str, brand: str, price: float, year: int,
                 strings_count: int, guitar_type: str) -> None:
        """
        Расширенный конструктор для гитары.

        Args:
            name: Название модели
            brand: Бренд
            price: Цена
            year: Год выпуска
            strings_count: Количество струн
            guitar_type: Тип гитары
        """
        # Наследование конструктора базового класса
        super().__init__(name, brand, price, year)
        self.strings_count = strings_count
        self.guitar_type = guitar_type
        self._is_tuned = False  # Инкапсуляция: состояние настройки - внутренняя логика

    def __str__(self) -> str:
        """Перегруженный метод для гитары."""
        base_string = super().__str__()
        tuned_status = "настроена" if self._is_tuned else "не настроена"
        return f"{base_string} - {self.guitar_type} гитара, {self.strings_count} струн, {tuned_status}"

    def __repr__(self) -> str:
        """Перегруженный метод для гитары."""
        return (f"Guitar(name='{self.name}', brand='{self.brand}', price={self.price}, "
                f"strings_count={self.strings_count}, guitar_type='{self.guitar_type}')")

    def play(self) -> str:
        """
        Перегруженный метод игры на гитаре.

        Причина перегрузки: На гитаре нельзя нормально играть, если она не настроена.
        Метод проверяет состояние настройки перед игрой.

        Returns:
            str: Описание звучания гитары или просьба настроить
        """
        if not self._is_tuned:
            return f"{self.name} не настроена! Сначала вызовите метод tune()"
        return f"Играет {self.strings_count}-струнная {self.guitar_type} гитара: брынь-брынь!"

    def tune(self) -> str:
        """
        Перегруженный метод настройки гитары.

        Returns:
            str: Сообщение о настройке гитары
        """
        self._is_tuned = True
        return f"{self.guitar_type} гитара {self.name} настроена по струнам"

    def change_strings(self) -> str:
        """
        Замена струн на гитаре.

        Returns:
            str: Сообщение о замене струн
        """
        self._is_tuned = False  # После замены струн гитара расстраивается
        return f"Струны на {self.name} заменены. Требуется настройка."


class Piano(MusicalInstrument):
    """
    Класс пианино, наследующийся от MusicalInstrument.

    Additional Attributes:
        key_count (int): Количество клавиш
        piano_type (str): Тип (рояль, пианино, цифровое)
        _need_tuning (bool): Нуждается ли в настройке (непубличный атрибут)
    """

    def __init__(self, name: str, brand: str, price: float, year: int,
                 key_count: int, piano_type: str) -> None:
        """
        Расширенный конструктор для пианино.

        Args:
            name: Название модели
            brand: Бренд
            price: Цена
            year: Год выпуска
            key_count: Количество клавиш
            piano_type: Тип пианино
        """
        super().__init__(name, brand, price, year)
        self.key_count = key_count
        self.piano_type = piano_type
        self._need_tuning = True  # Инкапсуляция: новое пианино обычно требует настройки

    def __str__(self) -> str:
        """Перегруженный метод для пианино."""
        base_string = super().__str__()
        tuning_status = "нуждается в настройке" if self._need_tuning else "настроено"
        return f"{base_string} - {self.piano_type}, {self.key_count} клавиш, {tuning_status}"

    def __repr__(self) -> str:
        """Перегруженный метод для пианино."""
        return (f"Piano(name='{self.name}', brand='{self.brand}', price={self.price}, "
                f"key_count={self.key_count}, piano_type='{self.piano_type}')")

    def play(self) -> str:
        """
        Перегруженный метод игры на пианино.

        Причина перегрузки: Пианино - сложный инструмент, требующий определенной техники.
        Метод учитывает необходимость настройки для качественного звучания.

        Returns:
            str: Описание игры на пианино
        """
        if self._need_tuning:
            return f"{self.piano_type} {self.name} расстроено. Звук может быть неточным."
        return f"Играет {self.piano_type} с {self.key_count} клавишами: динь-дон!"

    def tune(self) -> str:
        """
        Перегруженный метод настройки пианино.

        Returns:
            str: Сообщение о настройке пианино
        """
        self._need_tuning = False
        return f"{self.piano_type} {self.name} настроено профессиональным настройщиком"

    def press_key(self, key_number: int) -> str:
        """
        Нажатие на определенную клавишу.

        Args:
            key_number: Номер клавиши

        Returns:
            str: Звук нажатой клавиши
        """
        if key_number < 1 or key_number > self.key_count:
            return f"Клавиши с номером {key_number} не существует"

        notes = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
        note_index = (key_number - 1) % len(notes)
        return f"Нажата клавиша {key_number} - нота {notes[note_index]}"