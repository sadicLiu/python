class Fish:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        print(self.name)

fish = Fish('golden fish')
fish.get_name()

class Cat:
    def eat(self, fish):
        print('Eating: ', fish.name)

    def __call__(self, fish):
        print('Eating: ', fish.name)

cat = Cat()
cat.eat(fish)
cat(fish)
