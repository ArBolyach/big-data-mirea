morze = {
    "a": ".-",
    "b": "-…",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "….",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "…",
    "t": "-",
    "u": "..-",
    "v": "…-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

def main():
    text = input().lower()
    result = ""
    for symbol in text:
        if symbol == " ":
            result += "\n"
        else:
            result += morze[symbol] + " "

    print(result)


if __name__ == "__main__":
    main()
