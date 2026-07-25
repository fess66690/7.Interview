

class Stack:
    # Инициализация стека
    def __init__(self):
        self._stack = []

    # is_empty — проверка стека на пустоту. Метод возвращает True или False;
    def is_empty(self):
        return len(self._stack) == 0

    # push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
    def push(self, element):
        self._stack.append(element)

    # pop — удаляет верхний элемент стека. Стек изменяется.
    # Метод возвращает верхний элемент стека;
    def pop(self):
        return  self._stack.pop()

    # peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
    def peek(self):
        return self._stack[-1]

    # size — возвращает количество элементов в стеке.
    def size(self):
        return len(self._stack)

"""Проверка на сбалансированность.
1. Начинаться строка должна с открытой скобки.
2. Все открытые добавляем в конец. Если закрытая соответствует крайней открытой то удаляем крайнюю.
3. Если на выходе стек пуст - Сбалансировано"""
def balance_brackets(brackets_string):

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    open_brackets = set(brackets.values())

    stack = Stack()

    for bracket in brackets_string:
        # Если символ - открывающая скобка
        if bracket in open_brackets:
            stack.push(bracket)
        # Если символ - закрывающая скобка
        elif bracket in brackets:
            # Если стек пуст - нет соответствующей открывающей скобки
            if stack.is_empty():
                return False
            # Проверяем соответствие верхней скобки

            if stack.pop() != brackets[bracket]:
                return False

    return stack.is_empty()


def main():

    test = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}", "}{}", "{{[(])]}}", "[[{())}]", "{([db])}"]

    for test_string in test:
        result = "Сбалансированно" if balance_brackets(test_string) else "Несбалансированно"
        print(f"Строка: {test_string:30} -> {result}")


if __name__ == "__main__":
    main()