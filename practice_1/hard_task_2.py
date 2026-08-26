class Users:
    def __init__(self):
        self.users = {}
        self.max_user_number = {}

    def addUser(self, name: str):
        if name not in self.users:
            self.users[name] = True
            self.max_user_number[name] = 0
            return "OK"
        else:
            maxnum = self.max_user_number[name]
            new_name = name + str(maxnum + 1)
            self.users[new_name] = True
            self.max_user_number[name] = maxnum + 1
            return "suggested name: " + new_name


def main():
    n: int = int(input())
    users_system = Users()

    for i in range(n):
        print(users_system.addUser(input()))


if __name__ == "__main__":
    main()
