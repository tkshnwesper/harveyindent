from sys import argv

filename = argv[1]
f = open(filename)

if '-s' in argv:
    ind = int(argv[argv.index('-s') + 1]) * ' '

elif '-t' in argv:
    ind = int(argv[argv.index('-t') + 1]) * '\t'

else:
    ind = 4 * ' '

if '-u' in argv:
    usymbol = argv[argv.index('-u') + 1]

else:
    usymbol = '#~'

if '-i' in argv:
    isymbol = argv[argv.index('-i') + 1]

else:
    isymbol = ':'

level = 0    # indentation level
stringStack = []
output = []

def bracketCheck(line, i, op, cl):
    if stringStack == [] and line[i] == op:
        if i == 0 or line[i - 1] != "\\":
            stringStack.append(line[i])
    elif stringStack != [] and line[i] == cl:
        if i == 0 or line[i - 1] != "\\":
            stringStack.pop()


while True:
    line = f.readline()
    if line == '':
        break

    if line != '\n':
        line = line.lstrip()

    output.append(level * ind + line)

    for i in range(0, len(line)):
        if stringStack == [] and line[i] == usymbol[0]:
            if line.find(usymbol, i, i + len(usymbol)) != -1 and level > 0:
                level = level - 1

        if stringStack == [] and line[i] == isymbol[0]:
            if line.find(isymbol, i, i + len(isymbol)) != -1:
                level = level + 1

        if line[i] == '\'' and line.find('\'\'\'', i, i + 2) != -1:
            if i == 0 or line[i - 1] != "\\":
                if stringStack == []:
                    stringStack.append(line[i])
                elif stringStack[len(stringStack) - 1] != '\'\'\'':
                    stringStack.append('\'\'\'')
                else:
                    stringStack.pop()

        if line[i] == '\'' or line[i] == '\"':
            if i == 0 or line[i - 1] != "\\":
                if stringStack == []:
                    stringStack.append(line[i])
                elif stringStack[len(stringStack) - 1] != line[i]:
                    stringStack.append(line[i])
                else:
                    stringStack.pop()


        bracketCheck(line, i, '[', ']')

        bracketCheck(line, i, '(', ')')

        bracketCheck(line, i, '{', '}')

f.close()

f = open(str(filename[:-3] if filename.endswith('.py') else filename) + '.hi.py', 'w')

f.writelines(output)

f.close()