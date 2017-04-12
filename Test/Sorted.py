class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return repr((self.name, self.score))

    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return -cmp(self.score, s.score)


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)

'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return str(t[0]).lower()

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print L2

L3 = sorted(L, key=by_score)
print L3
'''



from operator import itemgetter, attrgetter

student_trubles = [
('Tim', '99'),
('Bob', '88'),
('Alice', '99'),
]
print sorted(student_trubles, key=itemgetter(1,0), reverse=True)

'''
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return repr((self.name, self.score))

student_objects = [
Student('john', '90'),
Student('jane', '80'),
Student('dave', '80'),
Student('abcg', '89'),
Student('devc', '75'),
Student('ufod', '75'),
]
#print sorted(student_objects, key=lambda student: student.score)
#print sorted(student_objects, key=lambda student: student.name)
print sorted(student_objects, key=attrgetter('score', 'name'), reverse=True)
'''

