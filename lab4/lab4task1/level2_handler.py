from support_handler import SupportHandler

class Level2Handler(SupportHandler):
    def handle_request(self):
        print("Welcome to Level 2 Support.")
        choice = input("Is the device plugged in? (yes/no): ")
        if choice.lower() == 'yes':
            print("Problem solved! Goodbye.")
        else:
            print("Let's try another solution.")
            self.next_handler.handle_request() if self.next_handler else print("No higher level support available.")
