from image import Image

def main():
    # Зображення з файлової системи
    file_image = Image(href="C:\cat", strategy="file")
    file_image.display()

    print()

    # Зображення з мережі
    web_image = Image(href="https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg", strategy="web")
    web_image.display()

if __name__ == "__main__":
    main()
