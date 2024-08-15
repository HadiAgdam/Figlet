
f = open("chars.txt")
f = f.read().split("n\n")

d = {}
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
for i in range(0, len(chars)):
    d[chars[i]] = f[i]


def convert(text: str) -> str:
    result = ""
    for i in range(0, 5):
        for j in range(0, len(text)):
            t = text[j]
            if t == " ":
                a = "  "
                if j != len(text) - 1:
                    a += d[text[j + 1]].splitlines()[i][0]
            else:
                x = d[t].splitlines()[i]
                if j != 0:
                    x = x[1:]
                c1 = x[len(x) - 1]

                c = c1
                
                if j != len(text) - 1:
                    if text[j + 1] == " ":
                        c = c1
                    else: c2 = d[text[j + 1]].splitlines()[i][0]
                else: c2 = " "

                if c2 != " ":
                    c = c2

                a = x[:len(x) - 1] + c
            result += a
        result += "\n"
    return result

