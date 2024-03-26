from DevOS.kernel import Kernel


class DevOS:
    kernel = Kernel()

    def __init__(self):
        self.start()

    def start(self):
        kernel = Kernel()
        self.kernel.getConfig()
        print("Welcome to DevOS version 0.1, write a command:")
        self.kernel.login()
        self.command_handler()

    def command_handler(self):
        command = input(self.kernel.main_message)

        if command == "help":
            self.kernel.help()
            
        elif command == "clear":
            self.kernel.clear()

        elif command.startswith("calc"):
            self.kernel.send_message(self.kernel.calculate(command))

        elif command == "root":
            self.kernel.loginToRoot()

        elif command == "unroot":
            self.kernel.unloginToRoot()

        elif command == "shutdown":
            return
        
        else:
            print("Unknown command")
        self.command_handler()