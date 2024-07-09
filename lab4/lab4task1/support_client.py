from level1_handler import Level1Handler
from level2_handler import Level2Handler
from level3_handler import Level3Handler
from level4_handler import Level4Handler


class SupportClient:
    def __init__(self):
        self.handler1 = Level1Handler(1)
        self.handler2 = Level2Handler(2)
        self.handler3 = Level3Handler(3)
        self.handler4 = Level4Handler(4)

        self.handler1.set_next_handler(self.handler2).set_next_handler(self.handler3).set_next_handler(self.handler4)

    def start(self):
        print("Welcome to Customer Support.")
        self.handler1.handle_request()


def main():
    client = SupportClient()
    client.start()


if __name__ == "__main__":
    main()
