from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabetOrder(Iterator):
    # Как я понял, это класс сортирует элемент и выводит его

    _position: int = None #Хранит текущее положение обхода
    _reverse: bool = False #Указывает порядок обхода

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0   #Выбирает как мы будем обходить массив,
                                                # в зависимости от reverse. -1 = последний элемент

    def __next__(self):
        try:
            value = self._collection[self._position] #Обращение по
            self._position += -1 if self._reverse else 1 #Позиция следующего элемента
        except IndexError:
            raise StopIteration() # Останавливает иттерацию, когда все обошел

        return value


class WordsCollection(Iterable): #Итерируемый обьект, который будем проходить

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self): #Следующий элемент в прямом порядке
        return AlphabetOrder(self._collection)

    def reverse_iterator(self): #Следующий элемент в обратном порядке
        return AlphabetOrder(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)