class NewString:

    def __init__(self):
        self.string = input('Enter string:  ')

    def enter_the_string(self):
        return self.string


person2 = NewString()
person2.enter_the_string()
print(person2.enter_the_string().upper())