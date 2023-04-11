from operator import length_hint


class Backpack:
    
    def __init__(self, color, size) -> None:
        self.items = []
        self.color = color
        self.size = size


class Circle:

    def __init__(self, radius) -> None:
        self.pi = 3.14
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius


class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        self.area = self.width * self.length


class Movie:

    def __init__(self, title, year, language, rating) -> None:
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


