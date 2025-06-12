from note import Note


class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def delete_note(self, index: int):
        self.notes.pop(index)

    def list_notes(self):
        for note in self.notes:
            note.display()
            print('-----------')
        print('\n')
