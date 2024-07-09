from text_editor import TextEditor

def main():
    editor = TextEditor()

    # Робимо зміни в документі
    editor.type("Hello, world!")
    editor.type(" This is a test document.")

    # Зберігаємо стан документа
    editor.save()

    # Продовжуємо редагування
    editor.type(" Adding more text.")

    # Відмінюємо останні зміни
    editor.undo()

    # Відновлюємо до збереженого стану
    editor.restore()

if __name__ == "__main__":
    main()
