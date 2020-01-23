class Parent():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('My name is ' + self.name + ", I'm " + str(self.age) + ' years old.')


p = Parent('zhangsan', 33)
p.info()

class Child(Parent):

	def __init__(self, name, age):
		super().__init__(name, age)
		self.grade = 'high school'

	def cur_grade(self):
		print("I'm now in " + self.grade)

c = Child('lisi', 11)
c.info()
c.cur_grade()
