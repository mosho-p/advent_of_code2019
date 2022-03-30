with open('day5data.txt') as f:
    data = list(map(int, f.read().split(',')))

def mode0(i):
    return data[data[i]]

def mode1(i):
    return data[i]

def code1(i, modes):
    data[data[i+2]] = eval(f'mode{modes[2]}({i})') + eval(f'mode{modes[1]}({i+1})')

def code2(i, modes):
    data[data[i+2]] = eval(f'mode{modes[2]}({i})') * eval(f'mode{modes[1]}({i+1})')

def code3(i):
    data[data[i]] = int(input("Input: "))

def code4(i, mode):
    return eval(f'mode{mode}(i)')

def code7(i, modes):
    if eval(f'mode{modes[2]}({i})') < eval(f'mode{modes[1]}({i+1})'):
        data[data[i+2]] = 1
    else:
        data[data[i+2]] = 0

def code8(i, modes):
    if eval(f'mode{modes[2]}({i})') == eval(f'mode{modes[1]}({i+1})'):
        data[data[i+2]] = 1
    else:
        data[data[i+2]] = 0

def process():
    # if first instruction ends in (0)1 or (0)2 then it needs a total of 5 digits.
    # 3 will be 3
    # 4 will be 4 or 104
    # so look at the last digit, if its a 1 or 2 drop last 2 then fill with 0s up to 3 digits
    # if its a 4 drop last 2 then fill with 0 if empty
    i = 0
    while i < len(data):
        code = str(data[i])[-1]
        # print(code)
        if code in ('1', '2', '7', '8'):
            modes = str(data[i])[:-2].zfill(3)
            eval(f'code{code}({i+1}, modes)')
            i += 4
        elif code == '3':
            code3(i+1)
            i += 2
        elif code == '4':
            mode = str(data[i])[:-2].zfill(1)
            print(code4(i+1, mode))
            i += 2
        elif code == '5':
            modes = str(data[i])[:-2].zfill(2)
            if eval(f'mode{modes[1]}({i+1})') != 0:
                i = eval(f'mode{modes[0]}({i+2})')
            else:
                i += 3
        elif code == '6':
            modes = str(data[i])[:-2].zfill(2)
            if eval(f'mode{modes[1]}({i+1})') == 0:
                i = eval(f'mode{modes[0]}({i+2})')
            else:
                i += 3
        else:
            break


if __name__ == '__main__':
    process()