class TextDocument:
    def __init__(self):
        self.content = ""

    def append(self, text):
        self.content += text

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content


class TextEditor:
    def __init__(self):
        self.document = TextDocument()
        self.history = []

    def type(self, text):
        # Додаємо текст до документа
        self.document.append(text)
        print(f"Current content: {self.document.get_content()}")

    def save(self):
        # Зберігаємо поточний стан документа (створюємо мементо)
        self.history.append(self.document.get_content())
        print("Document state saved.")

    def undo(self):
        # Відміняємо останні зміни
        if self.history:
            last_saved_state = self.history.pop()
            self.document.set_content(last_saved_state)
            print(f"Undoing last change. Current content: {self.document.get_content()}")
        else:
            print("Nothing to undo.")

    def restore(self):
        # Відновлюємо до останнього збереженого стану
        if self.history:
            last_saved_state = self.history[-1]
            self.document.set_content(last_saved_state)
            print(f"Restoring to last saved state. Current content: {self.document.get_content()}")
        else:
            print("No saved state to restore.")

