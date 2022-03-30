def code1(i, data):
    data[data[i+3]] = data[data[i+1]] + data[data[i+2]]

def code2(i, data):
    data[data[i+3]] = data[data[i+1]] * data[data[i+2]]

def process(data):
    for i in range(0, len(data), 4):
        x = data[i]
        if x == 1:
            code1(i, data)
        elif x == 2:
            code2(i, data)
        elif x == 99:
            break
        else:
            print('ERROR')
            break
    return data[0]


def answer1():
    with open('day2data.txt') as f:
        data = list(map(int, f.read().split(',')))
    data[1] = 12
    data[2] = 2

    return process(data)


def answer2():
    with open('day2data.txt') as f:
        data = list(map(int, f.read().split(',')))

    for noun in range(100):
        for verb in range(100):
            data_copy = data[:]
            data_copy[1], data_copy[2] = noun, verb
            output = process(data_copy)
            if output == 19690720:
                return 100 * noun + verb

if __name__ == '__main__':
    print(answer2())