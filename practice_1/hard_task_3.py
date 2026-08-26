class Files:
    def __init__(self):
        self._events = {"read": "r", "write": "w", "execute": "x"}
        self.files = {}  # {w: bool, r: bool, x: bool}

    def addFile(self, inp: str):
        temp = inp.split(" ", 1)
        file = temp[0]
        access = {"w": False, "r": False, "x": False}
        for item in temp[1]:
            match item:
                case "w":
                    access["w"] = True
                case "r":
                    access["r"] = True
                case "x":
                    access["x"] = True
        self.files[file] = access

    def doEvent(self, inp: str):
        temp = inp.split(" ", 1)
        event = temp[0]
        file = temp[1]
        if file in self.files and self.files[file][self._events[event]]:
            return "OK"
        else:
            return "Access denied"


files = Files()


def main():
    n = int(input())

    for _ in range(n):
        files.addFile(input())  # python.exe x

    m = int(input())

    for _ in range(m):
        print(files.doEvent(input()))  # read python.exe


if __name__ == "__main__":
    main()
