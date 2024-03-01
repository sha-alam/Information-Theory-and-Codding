message = 'AABABBBABAABABBBABBABB'
dictionary = {}
tmp, i, last = '', 1, 0
Flag = True
for x in message:
    tmp += x
    Flag = False
    if tmp not in dictionary.keys():
        dictionary[tmp] = i
        tmp = ''
        i += 1
        Flag = True

if not Flag:
    last = dictionary[tmp]

res = ['1']
for char, idx in list(dictionary.items())[1:]:
    tmp, s = '', ''
    for x, j in zip(char[:-1], range(len(char))):
        tmp += x
        if tmp in dictionary.keys():
            take = dictionary[tmp]
            s = str(take) + char[j + 1:]
    if len(char) == 1:
        s = char
    res.append(s)
if last:
    res.append(str(last))

mark = {
    'A': 0,
    'B': 1
}

final_res = []
for x in res:
    tmp = ""
    for char in x:
        if char.isalpha():
            tmp += bin(mark[char])[2:]
        else:
            tmp += bin(int(char))[2:]
    final_res.append(tmp.zfill(4))

print(res)
print("Encoded: ", final_res)