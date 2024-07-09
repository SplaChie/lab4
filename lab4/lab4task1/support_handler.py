from abc import ABC, abstractmethod


class SupportHandler(ABC):
    def __init__(self, level):
        self.level = level
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler
        return next_handler

    @abstractmethod
    def handle_request(self):
        pass
