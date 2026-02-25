# 作者：柚子皮
# 2026年02月25日12时29分57秒
# yexixi2333@gmail.com

my_list = "This is a test string from xixi".split()
print(my_list)


def change_lower(str_name: str):
    return str_name.lower()


print(sorted(my_list, key=change_lower))

print('-' * 55)
student_tuples = [
    ('john', 'A', 15),
    ('amy', 'B', 12),
    ('peter', 'B', 13),
    ('mary', 'A', 10),
]

print(sorted(student_tuples, key=lambda d: d[2]))


class Student:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score

    def __repr__(self):
        return repr((self.name, self.grade, self.score))
    # def __str__(self):
    #     return str((self.name, self.grade, self.score))


student = Student('xixi', 5, 25)
student_objects = [
    Student('xixi', 5, 25),
    Student('john', 8, 15),
    Student('peter', 6, 6)
]
print('-' * 55)
print(sorted(student_objects, key=lambda s: s.score))

from operator import attrgetter, itemgetter

print('使用operator系列')
print(sorted(student_objects, key=attrgetter('score')))
print(sorted(student_tuples, key=itemgetter(2)))

print('operator系列，多列排列')
print(sorted(student_tuples, key=itemgetter(1, 2)))
print(sorted(student_tuples, key=lambda d: (d[1], d[2])))

print('-' * 55)
mydict = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}

print(sorted(mydict.items(), key=lambda x: x[1][1]))

print('-' * 55)

game_result = [
    {"name": "Bob", "wins": 10, "losses": 3, "rating": 55.00},
    {"name": "David", "wins": 3, "losses": 5, "rating": 65.00},
    {"name": "Carol", "wins": 4, "losses": 5, "rating": 75.00},
    {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}
]

for item in sorted(game_result, key=lambda x: (x['losses'], x['name'])):
    print(item)

# for item in sorted(game_result, key=itemgetter('losses', 'rating')):
#     print(item)
