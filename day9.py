from collections import defaultdict

class Intcomp:
    def __init__(self, data):
        self.data = defaultdict(lambda: 0)
        for i, d in enumerate(data):
            self.data[i] = d
        self.i = 0
        self.relative_base = 0

    def mode0(self, idx):
        return self.data[self.data[idx]]

    def mode1(self, idx):
        return self.data[idx]

    def mode2(self, idx):
        return self.data[self.data[idx]+self.relative_base]
    # NEED TO ADJUST ALL ASSIGNMENTS to be able to accept relative mode
    def code01(self, modes):
        if modes[0] == '2':
            self.data[self.data[self.i+3]+self.relative_base] = eval(f'self.mode{modes[2]}({self.i+1})') + eval(f'self.mode{modes[1]}({self.i+2})')
        else:
            self.data[self.data[self.i+3]] = eval(f'self.mode{modes[2]}({self.i+1})') + eval(f'self.mode{modes[1]}({self.i+2})')

    def code02(self, modes):
        if modes[0] == '2':
            self.data[self.data[self.i+3]+self.relative_base] = eval(f'self.mode{modes[2]}({self.i+1})') * eval(f'self.mode{modes[1]}({self.i+2})')
        else:
            self.data[self.data[self.i+3]] = eval(f'self.mode{modes[2]}({self.i+1})') * eval(f'self.mode{modes[1]}({self.i+2})')

    def code03(self, input_, mode='0'):
        if mode=='2':
            self.data[self.data[self.i+1]+self.relative_base] = input_
        else:
            self.data[self.data[self.i+1]] = input_

    def code04(self, mode):
        self.i += 2
        return eval(f'self.mode{mode}({self.i-1})')

    def code07(self, modes):
        if eval(f'self.mode{modes[2]}({self.i+1})') < eval(f'self.mode{modes[1]}({self.i+2})'):
            self.data[self.data[self.i+3] + (self.relative_base if modes[0]=='2' else 0)] = 1
        else:
            self.data[self.data[self.i+3] + (self.relative_base if modes[0]=='2' else 0)] = 0

    def code08(self, modes):
        if eval(f'self.mode{modes[2]}({self.i+1})') == eval(f'self.mode{modes[1]}({self.i+2})'):
            self.data[self.data[self.i+3] + (self.relative_base if modes[0]=='2' else 0)] = 1
        else:
            self.data[self.data[self.i+3] + (self.relative_base if modes[0]=='2' else 0)] = 0

    def code09(self, mode):
        self.relative_base += eval(f'self.mode{mode}({self.i+1})')

    def process(self, inputs=[]):
        inputs = inputs[::-1]
        while True:
            code = str(self.data[self.i])[-2:].zfill(2)
            self.last_code = code
            # print(code)
            if code in ('01', '02', '07', '08'):
                modes = str(self.data[self.i])[:-2].zfill(3)
                eval(f'self.code{code}(modes)')
                self.i += 4
            elif code == '03':
                mode = str(self.data[self.i])[:-2].zfill(1)
                self.code03(inputs.pop(), mode)
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
            elif code == '09':
                mode = str(self.data[self.i])[:-2].zfill(1)
                self.code09(mode) 
                self.i += 2
            elif code == '99':
                # self.i += 1
                break
            else:
                print('ERROR')
                break


if __name__ == '__main__':
    with open('day9data.txt') as f:
        data = list(map(int, f.read().split(',')))
    comp = Intcomp(data)
    print(comp.process([2]))



