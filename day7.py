from itertools import permutations

class Intcomp:
    def __init__(self, data):
        self.data = data
        self.i = 0
        self.last_code = None

    def mode0(self, idx):
        return self.data[self.data[idx]]

    def mode1(self, idx):
        return self.data[idx]

    def code01(self, modes):
        self.data[self.data[self.i+3]] = eval(f'self.mode{modes[2]}({self.i+1})') + eval(f'self.mode{modes[1]}({self.i+2})')

    def code02(self, modes):
        self.data[self.data[self.i+3]] = eval(f'self.mode{modes[2]}({self.i+1})') * eval(f'self.mode{modes[1]}({self.i+2})')

    def code03(self, input_):
        self.data[self.data[self.i+1]] = input_

    def code04(self, mode):
        self.i += 2
        return eval(f'self.mode{mode}({self.i-1})')

    def code07(self, modes):
        if eval(f'self.mode{modes[2]}({self.i+1})') < eval(f'self.mode{modes[1]}({self.i+2})'):
            self.data[self.data[self.i+3]] = 1
        else:
            self.data[self.data[self.i+3]] = 0

    def code08(self, modes):
        if eval(f'self.mode{modes[2]}({self.i+1})') == eval(f'self.mode{modes[1]}({self.i+2})'):
            self.data[self.data[self.i+3]] = 1
        else:
            self.data[self.data[self.i+3]] = 0

    def process(self, inputs):
        # if first instruction ends in (0)1 or (0)2 then it needs a total of 5 digits.
        # 3 will be 3
        # 4 will be 4 or 104
        # so look at the last digit, if its a 1 or 2 drop last 2 then fill with 0s up to 3 digits
        # if its a 4 drop last 2 then fill with 0 if empty
        inputs = inputs[::-1]
        while self.i < len(self.data):
            code = str(self.data[self.i])[-2:].zfill(2)
            self.last_code = code
            # print(code)
            if code in ('01', '02', '07', '08'):
                modes = str(self.data[self.i])[:-2].zfill(3)
                eval(f'self.code{code}(modes)')
                self.i += 4
            elif code == '03':
                self.code03(inputs.pop())
                self.i += 2
            elif code == '04':
                mode = str(self.data[self.i])[:-2].zfill(1)
                return self.code04(mode)
            elif code == '05':
                modes = str(self.data[self.i])[:-2].zfill(2)
                if eval(f'self.mode{modes[1]}({self.i+1})') != 0:
                    self.i = eval(f'self.mode{modes[0]}({self.i+2})')
                else:
                    self.i += 3
            elif code == '06':
                modes = str(self.data[self.i])[:-2].zfill(2)
                if eval(f'self.mode{modes[1]}({self.i+1})') == 0:
                    self.i = eval(f'self.mode{modes[0]}({self.i+2})')
                else:
                    self.i += 3
            elif code == '99':
                # self.i += 1
                break
            else:
                break


if __name__ == '__main__':
    # start program, give it first the setting (0, 4) then the input from the previous
    outputs = []
    for e, phase_order in enumerate(permutations([5, 6, 7, 8, 9])):
        with open('day7data.txt') as f:
            data = list(map(int, f.read().split(',')))
        amps = {n: Intcomp(data[:]) for n in range(5)}
        prev_out = 0
        for k, p in zip(range(5), phase_order):
            prev_out = amps[k].process([p, prev_out])
        counter = 0
        next_out = prev_out
        while next_out is not None:
            prev_out = next_out
            next_out = amps[counter%5].process([prev_out])
            counter += 1
        outputs.append(prev_out)
    print(max(outputs)) 



