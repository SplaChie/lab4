from support_handler import SupportHandler

class Level3Handler(SupportHandler):
    def handle_request(self):
        print("Welcome to Level 3 Support.")
        choice = input("Have you checked the device's documentation? (yes/no): ")
        if choice.lower() == 'yes':
            print("Problem solved! Goodbye.")
        else:
            print("Let's try another solution.")
            self.next_handler.handle_request() if self.next_handler else print("No higher level support available.")
