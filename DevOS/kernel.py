import json

class Kernel:
    user = ""
    pc_name = ""
    password = ""
    main_message = ""
    isLoginedToRoot = False

    errorPass = False

    commands = ["help", "calc", "root", "unroot"]
    description_commands = ["See all commands", "calculator", "login to admin user", "exit of the admin user"]

    def __init__(self):
        pass

    def help(self):
        print(len(self.commands))
        #for i in len(self.commands):
        #    print("{} - {}".format(self.commands[i], self.description_commands[i]))

    def getConfig(self):
        with open('config.json', 'r') as f:
            data = json.load(f)
        self.user = data["user"]
        self.pc_name = data["pc-name"]
        self.password = data["password"]
        self.changePermissions()

    def changePermissions(self):
        if self.isLoginedToRoot == True:
            self.main_message = "{}@{}~#: ".format(self.user, self.pc_name)
        else:
            self.main_message = "{}@{}~$: ".format(self.user, self.pc_name)


    def login(self):
        if self.errorPass == False:
            input_pas = input("Login to {}, write password: ".format(self.user))
        elif self.errorPass == True:
            input_pas = input("Error! Login to {}, write password: ".format(self.user))
        if(input_pas != self.password):
            self.errorPass = True
            self.login()
        self.isLoginedToRoot = False
        self.errorPass = False
        self.changePermissions()

    def loginToRoot(self):
        if self.errorPass == False:
            input_pas = input("Write root password: ")
        elif self.errorPass == True:
            input_pas = input("Error! Write root password: ")
        if(input_pas != self.password):
            self.errorPass = True
            self.loginToRoot()
        self.isLoginedToRoot = True
        self.errorPass = False
        self.changePermissions()

    def unloginToRoot(self):
        print("Exit of the root.")
        self.isLoginedToRoot = False
        self.changePermissions()

    def send_message(self, message):
        print("{}: {}".format(self.main_message, message))

    def calculate(self, command):
        args = command.split("=")
        return eval(args[1])