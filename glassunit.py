"""
Класс создания стеклопакета.
"""


class BaseProduct:
    def __init__(self, type_const: str, fittings: str, color_in: str, color_ex: str, width: int,
                 height: int):
        self.type_const = type_const
        self.fittings = fittings
        self.color_in = color_in
        self.color_ex = color_ex
        self.width = width
        self.height = height


class GlassUnit(BaseProduct):
    """Создание стеклопакета"""

    def __init__(self, width: int, height: int, type_const: str, fittings: str, color_in: str, color_ex: str):
        super().__init__()

    def __str__(self):
        return self.type_const

    def show(self):
        return f'{self.type_const} {self.fittings}'
