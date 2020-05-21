s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"


def answer(s):
    tbc = list(s)
    output = ''
    for i in tbc:
        if ord(i) in range(97, 123):
            i = chr(97+(26-(ord(i)-97)-1))
        elif i not in range(97, 123):
            i = i
        else:
            i = ' '
        output = output + i
    return str(output)


print(answer(s))
