from note import Note
from note_manager import NoteManager

manager = NoteManager()
print('1: Создать новую заметку\n2: Удалить заметку\n3: Вывести список заметок\n4: Выход')
while True:
    option = int(input('Выберите действие: \n'))
    if option == 1:
        name = input('Введите название заметки: ')
        text = input('Введите текст заметки: ')
        note = Note(name, text)
        manager.add_note(note)

    elif option == 2:
        index = int(input('Введите номер заметки, которую нужно удалить: '))
        manager.delete_note(index - 1)

    elif option == 3:
        manager.list_notes()

    elif option == 4:
        break




