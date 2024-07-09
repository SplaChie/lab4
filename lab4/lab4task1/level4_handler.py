from support_handler import SupportHandler

class Level4Handler(SupportHandler):
    def handle_request(self):
        print("Welcome to Level 4 Support.")
        print("This is the highest level of support. Problem should be resolved by now.")
        print("Goodbye.")
