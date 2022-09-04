Я изучила работу Мадины(https://github.com/madina-lk/HomeWork_21)
Я обнаружил следующие запахи:

1) bad_smell_comments
файл store.py строка 23-27
я бы удалила параметр title, и заменила бы его на name_item, что было бы более говорящим:

def add(self, name_item: str, quantity: int):
        """
        Метод увеличивает запас items
        """
        if self.get_free_space(name_item=name_item) >= quantity:
            self.items[name_item] = self.items.get(name_item, 0) + quantity
        else:
            return "Недостаточно места для добавления товара"

Название quantity итак говорит за себя, его заменять не потребуется. Таким образом из кода можно удалить огромное
количество строк и значительно уучшить читабельность.

2) Дублирование кода smell_doubles
файл request.py строка 18-21
можно заменить два блока на один:
if input_text.amount is None or input_text.product is None:
    print("Неврно указаны данные. Пожалуйста, перепроверьте")

Это также несколько сократит код


Но вообще работа у Мадины выполнена идеально, на мой взгляд.