class Note:
    def __init__(self, title: str = "Без заголовка", content: str = 'Без содержания'):
        self.title = title
        self.content = content

    def display(self):  # переделать с помощью переопределния str
        print(f'{self.title}\n{self.content}')

