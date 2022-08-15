class person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def get_older(self):
        print('My name is', self.name)
        print('I was ',self.age)
        self.age+=1
        print('Now I am ',self.age)
        print('I was ', self.height,' cms tall')
        if self.age<=21:
            self.height+=0.5
            print('Now I am ',self.height, ' cms tall')
        else:
            print('Now I am still ',self.height,' cms tall')

person1= person('eduardo',10,150)
person2= person('juja',30,180)


person1.get_older()
print(' ')
person2.get_older()
