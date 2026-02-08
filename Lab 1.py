import doctest

class Lake:
    def __init__(self, name: str, area: float, max_depth: float):
        """
        Создание и подготовка к работе объекта "Озеро"

        :param name: Название озера
        :param area: Площадь озера в квадратных километрах
        :param max_depth: Максимальная глубина озера в метрах

        Примеры:
        >>> lake = Lake("Байкал", 31722, 1642)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название озера должно быть типа str")
        if not name:
            raise ValueError("Название озера не может быть пустым")
        self.name = name

        if not isinstance(area, (int, float)):
            raise TypeError("Площадь озера должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь озера должна быть положительным числом")
        self.area = float(area)

        if not isinstance(max_depth, (int, float)):
            raise TypeError("Максимальная глубина озера должна быть типа int или float")
        if max_depth <= 0:
            raise ValueError("Максимальная глубина озера должна быть положительным числом")
        self.max_depth = float(max_depth)

    def is_deep_lake(self) -> bool:
        """
        Функция которая проверяет является ли озеро глубоким

        :return: Является ли озеро глубоким (глубина более 100 метров считается глубоким)

        Примеры:
        >>> lake = Lake("Байкал", 31722, 1642)
        >>> lake.is_deep_lake()
        True

        >>> lake = Lake("Плещеево", 51, 25)
        >>> lake.is_deep_lake()
        False
        """
        return self.max_depth > 100

    def add_water_to_lake(self, additional_depth: float) -> None:
        """
        Добавление воды в озеро (увеличение глубины).
        :param additional_depth: Дополнительная глубина в метрах

        :raise ValueError: Если дополнительная глубина отрицательная, то вызываем ошибку

        Примеры:
        >>> lake = Lake("Ладожское", 17700, 230)
        >>> lake.add_water_to_lake(10)
        """
        if not isinstance(additional_depth, (int, float)):
            raise TypeError("Дополнительная глубина должна быть типа int или float")
        if additional_depth < 0:
            raise ValueError("Дополнительная глубина должна быть положительным числом")

        self.max_depth += additional_depth

    def remove_water_from_lake(self, depth_reduction: float) -> None:
        """
        Извлечение воды из озера (уменьшение глубины).

        :param depth_reduction: Уменьшение глубины в метрах
        :raise ValueError: Если уменьшение глубины отрицательное или превышает текущую глубину озера,
        то возвращается ошибка.

        Примеры:
        >>> lake = Lake("Онежское", 9720, 120)
        >>> lake.remove_water_from_lake(10)
        """
        if not isinstance(depth_reduction, (int, float)):
            raise TypeError("Уменьшение глубины должно быть типа int или float")
        if depth_reduction < 0:
            raise ValueError("Уменьшение глубины должно быть положительным числом")
        if depth_reduction > self.max_depth:
            raise ValueError("Нельзя извлечь больше воды, чем есть в озере")

        self.max_depth -= depth_reduction


class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param side_a: Длина стороны A
        :param side_b: Длина стороны B
        :param side_c: Длина стороны C

        Примеры:
        >>> triangle = Triangle(3, 4, 5)  # инициализация экземпляра класса
        """
        if not isinstance(side_a, (int, float)):
            raise TypeError("Длина стороны A должна быть типа int или float")
        if side_a <= 0:
            raise ValueError("Длина стороны A должна быть положительным числом")
        self.side_a = float(side_a)

        if not isinstance(side_b, (int, float)):
            raise TypeError("Длина стороны B должна быть типа int или float")
        if side_b <= 0:
            raise ValueError("Длина стороны B должна быть положительным числом")
        self.side_b = float(side_b)

        if not isinstance(side_c, (int, float)):
            raise TypeError("Длина стороны C должна быть типа int или float")
        if side_c <= 0:
            raise ValueError("Длина стороны C должна быть положительным числом")
        self.side_c = float(side_c)

        # Проверка неравенства треугольника
        if (self.side_a + self.side_b <= self.side_c or
                self.side_a + self.side_c <= self.side_b or
                self.side_b + self.side_c <= self.side_a):
            raise ValueError("Такой треугольник не может существовать")

    def is_equilateral_triangle(self) -> bool:
        """
        Функция которая проверяет является ли треугольник равносторонним

        :return: Является ли треугольник равносторонним

        Примеры:
        >>> triangle = Triangle(5, 5, 5)
        >>> triangle.is_equilateral_triangle()
        True
        """
        return self.side_a == self.side_b == self.side_c

    def increase_side(self, side_name: str, increment: float) -> None:
        """
        Увеличение длины стороны треугольника.

        :param side_name: Название стороны для увеличения ('a', 'b' или 'c')
        :param increment: Величина увеличения

        :raise ValueError: Если величина увеличения отрицательная или после увеличения треугольник перестанет существовать,
        то вызываем ошибку

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        >>> triangle.increase_side('a', 1)
        """
        if not isinstance(increment, (int, float)):
            raise TypeError("Величина увеличения должна быть типа int или float")
        if increment < 0:
            raise ValueError("Величина увеличения должна быть положительным числом")

        if side_name == 'a':
            new_side_a = self.side_a + increment
            # Проверяем, может ли существовать треугольник с новой стороной
            if (new_side_a + self.side_b <= self.side_c or
                    new_side_a + self.side_c <= self.side_b or
                    self.side_b + self.side_c <= new_side_a):
                raise ValueError("После увеличения стороны треугольник не может существовать")
            self.side_a = new_side_a
        elif side_name == 'b':
            new_side_b = self.side_b + increment
            if (self.side_a + new_side_b <= self.side_c or
                    self.side_a + self.side_c <= new_side_b or
                    new_side_b + self.side_c <= self.side_a):
                raise ValueError("После увеличения стороны треугольник не может существовать")
            self.side_b = new_side_b
        elif side_name == 'c':
            new_side_c = self.side_c + increment
            if (self.side_a + self.side_b <= new_side_c or
                    self.side_a + new_side_c <= self.side_b or
                    self.side_b + new_side_c <= self.side_a):
                raise ValueError("После увеличения стороны треугольник не может существовать")
            self.side_c = new_side_c
        else:
            raise ValueError("Название стороны должно быть 'a', 'b' или 'c'")

    def decrease_side(self, side_name: str, decrement: float) -> None:
        """
        Уменьшение длины стороны треугольника.

        :param side_name: Название стороны для уменьшения ('a', 'b' или 'c')
        :param decrement: Величина уменьшения

        :raise ValueError: Если величина уменьшения отрицательная, превышает длину стороны
        или после уменьшения треугольник перестанет существовать, то возвращается ошибка.

        Примеры:
        >>> triangle = Triangle(6, 8, 10)
        >>> triangle.decrease_side('a', 2)
        """
        if not isinstance(decrement, (int, float)):
            raise TypeError("Величина уменьшения должна быть типа int или float")
        if decrement < 0:
            raise ValueError("Величина уменьшения должна быть положительным числом")

        if side_name == 'a':
            if decrement > self.side_a:
                raise ValueError("Нельзя уменьшить сторону больше, чем ее длина")
            new_side_a = self.side_a - decrement
            if (new_side_a + self.side_b <= self.side_c or
                    new_side_a + self.side_c <= self.side_b or
                    self.side_b + self.side_c <= new_side_a):
                raise ValueError("После уменьшения стороны треугольник не может существовать")
            self.side_a = new_side_a
        elif side_name == 'b':
            if decrement > self.side_b:
                raise ValueError("Нельзя уменьшить сторону больше, чем ее длина")
            new_side_b = self.side_b - decrement
            if (self.side_a + new_side_b <= self.side_c or
                    self.side_a + self.side_c <= new_side_b or
                    new_side_b + self.side_c <= self.side_a):
                raise ValueError("После уменьшения стороны треугольник не может существовать")
            self.side_b = new_side_b
        elif side_name == 'c':
            if decrement > self.side_c:
                raise ValueError("Нельзя уменьшить сторону больше, чем ее длина")
            new_side_c = self.side_c - decrement
            if (self.side_a + self.side_b <= new_side_c or
                    self.side_a + new_side_c <= self.side_b or
                    self.side_b + new_side_c <= self.side_a):
                raise ValueError("После уменьшения стороны треугольник не может существовать")
            self.side_c = new_side_c
        else:
            raise ValueError("Название стороны должно быть 'a', 'b' или 'c'")


class Movie:
    def __init__(self, title: str, duration_minutes: int, rating: float):
        """
        Создание и подготовка к работе объекта "Фильм"

        :param title: Название фильма
        :param duration_minutes: Продолжительность фильма в минутах
        :param rating: Рейтинг фильма (от 0.0 до 10.0)

        Примеры:
        >>> movie = Movie("Зеленая миля", 189, 9.3)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название фильма должно быть типа str")
        if not title:
            raise ValueError("Название фильма не может быть пустым")
        self.title = title

        if not isinstance(duration_minutes, int):
            raise TypeError("Продолжительность фильма должна быть типа int")
        if duration_minutes <= 0:
            raise ValueError("Продолжительность фильма должна быть положительным числом")
        if duration_minutes > 600:  # 10 часов максимум
            raise ValueError("Продолжительность фильма не может превышать 600 минут")
        self.duration_minutes = duration_minutes

        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг фильма должен быть типа int или float")
        if rating < 0 or rating > 10:
            raise ValueError("Рейтинг фильма должен быть в диапазоне от 0.0 до 10.0")
        self.rating = float(rating)

    def is_long_movie(self) -> bool:
        """
        Функция которая проверяет является ли фильм длинным

        :return: Является ли фильм длинным (продолжительность более 150 минут считается длинным)

        Примеры:
        >>> movie = Movie("Властелин колец: Возвращение короля", 201, 9.0)
        >>> movie.is_long_movie()
        True

        >>> movie = Movie("Короткометражка", 30, 7.5)
        >>> movie.is_long_movie()
        False
        """
        return self.duration_minutes > 150

    def increase_rating(self, increase_amount: float) -> None:
        """
        Увеличение рейтинга фильма.
        :param increase_amount: Величина увеличения рейтинга

        :raise ValueError: Если величина увеличения отрицательная или после увеличения рейтинг превысит 10.0,
        то вызываем ошибку

        Примеры:
        >>> movie = Movie("Интерстеллар", 169, 8.6)
        >>> movie.increase_rating(0.2)
        """
        if not isinstance(increase_amount, (int, float)):
            raise TypeError("Величина увеличения рейтинга должна быть типа int или float")
        if increase_amount < 0:
            raise ValueError("Величина увеличения рейтинга должна быть положительным числом")

        new_rating = self.rating + increase_amount
        if new_rating > 10.0:
            raise ValueError("После увеличения рейтинг фильма превысит максимально допустимый (10.0)")

        self.rating = new_rating

    def decrease_rating(self, decrease_amount: float) -> None:
        """
        Уменьшение рейтинга фильма.

        :param decrease_amount: Величина уменьшения рейтинга
        :raise ValueError: Если величина уменьшения отрицательная или после уменьшения рейтинг станет менее 0.0,
        то возвращается ошибка.

        Примеры:
        >>> movie = Movie("Побег из Шоушенка", 142, 9.3)
        >>> movie.decrease_rating(0.1)
        """
        if not isinstance(decrease_amount, (int, float)):
            raise TypeError("Величина уменьшения рейтинга должна быть типа int или float")
        if decrease_amount < 0:
            raise ValueError("Величина уменьшения рейтинга должна быть положительным числом")

        new_rating = self.rating - decrease_amount
        if new_rating < 0.0:
            raise ValueError("После уменьшения рейтинг фильма станет менее 0.0")

        self.rating = new_rating

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации