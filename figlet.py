
f = open("chars.txt")
f = f.read().split("n\n")

d = {}
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
for i in range(0, len(chars)):
    d[chars[i]] = f[i]
    # print(chars[i])
    # print(f[i])




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
                    else: 
                        try:
                            c2 = d[text[j + 1]].splitlines()[i][0]
                        except Exception as ex:
                            print(text[j + 1])
                            input("error")
                            print(ex)
                else: c2 = " "

                if c2 != " ":
                    c = c2

                a = x[:len(x) - 1] + c
            result += a
        result += "\n"
    return result

