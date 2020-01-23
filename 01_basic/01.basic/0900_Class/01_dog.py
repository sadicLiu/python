class Dog():
    """创建类Dog"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下的动作"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

dog = Dog('xiaohei', 6)
print("My dog's name is " + dog.name)
dog.sit()
