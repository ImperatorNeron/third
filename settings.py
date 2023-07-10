class Settings:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


if __name__ == '__main__':
    print(Settings(15, 25).add())
