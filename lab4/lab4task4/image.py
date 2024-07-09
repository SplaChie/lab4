import os
from urllib.request import urlopen

class Image:
    def __init__(self, href, strategy):
        self.href = href
        self.strategy = strategy

    def display(self):
        strategy = None
        if self.strategy == "file":
            strategy = FileImageLoadingStrategy()
        elif self.strategy == "web":
            strategy = WebImageLoadingStrategy()

        if strategy:
            strategy.load_image(self.href)


class ImageLoadingStrategy:
    def load_image(self, href):
        raise NotImplementedError("Subclasses should implement load_image method.")


class FileImageLoadingStrategy(ImageLoadingStrategy):
    def load_image(self, file_path):
        if os.path.exists(file_path):
            print(f"Loading image from file: {file_path}")
            # Логіка завантаження зображення з файлової системи
        else:
            print(f"Image file not found: {file_path}")


class WebImageLoadingStrategy(ImageLoadingStrategy):
    def load_image(self, url):
        try:
            with urlopen(url) as response:
                print(f"Loading image from URL: {url}")
                # Логіка завантаження зображення з мережі
        except Exception as e:
            print(f"Failed to load image from URL: {url}")
            print(f"Error: {e}")
