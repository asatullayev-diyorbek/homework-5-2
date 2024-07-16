class Homework:
    @staticmethod
    def check(value, type_):
        assert isinstance(value, type_), TypeError

    def task1(self, list1: list, list2: list):
        self.check(list1, list)
        self.check(list2, list)
        list3 = []
        for i in range(min(len(list1), len(list2))):
            list3.append(list1[i] + list2[i])
        return list3

    def task2(self, number: int):
        self.check(number, int)
        n_old = number
        n_new = 0
        while number > 0:
            n_new = n_new * 10 + number % 10
            number //= 10
        return n_new == n_old

    def task3(self, text: str):
        self.check(text, str)
        character_count = {}
        for character in text:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
        most = max(character_count, key=character_count.get)
        return most

    def task4(self, text: str):
        self.check(text, str)
        bracket_dict = {
            1: ['(', ')'],
            2: ['{', '}'],
            3: ['[', ']']
        }
        try:
            bracket = int(input("Qavs turini tanlang: \n1. ( )\n2. { }\n3. [ ]\nRaqamni kiriting:"))
        except:
            raise TypeError
        if bracket in [1, 2, 3]:
            return text.count(bracket_dict[bracket][0]) == text.count(bracket_dict[bracket][1])
        else:
            raise ValueError

    def task5(self, text: str, character: str):
        self.check(text, str)
        self.check(character, str)
        return text.index(character)


if __name__ == '__main__':
    homework = Homework()

    # Task 1
    l1 = [1, 2, 3]
    l2 = [4, 5]
    print("Task 1:", homework.task1(l1, l2))

    # Task 2
    print("Task 2:", homework.task2(565))

    # Task 3
    t = "Assalomu alaykum"
    print("Task 3:", homework.task3(t))

    # Task 4
    t2 = "{assalomu alaykum}"
    print("Task 4:", homework.task4(t2))

    # Task 5
    print("Task 5:", homework.task5(t, 'k'))
