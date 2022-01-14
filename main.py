import numpy as np
import sys

class Tape:
    def __init__(self):
        self.arr = np.zeros((64, 2), np.int8)
        self.sarr = np.zeros((32, 2), np.int8)
        self.OP = 0
        self.DP = 0
        self.SOP = 0
        self.SDP = 0
        self.cache = 0
        self.sub = False
    def load_ROM(self, fname):
        f = open(fname, 'r').read()
        data = ''
        for c in f:
            if c in '0123456789abcdef':
                data = data + c
        print(data)
        i = 0
        j = 0
        while j < len(data):
            self.arr[i][0], self.arr[i][1] = int(data[j], 16), int(data[j+1], 16)
            i += 1
            j += 2
        while i < 64:
            self.arr[i][0] = 15
            self.arr[i][1] = 0
            i += 1
    def get_DP(self):
        if not self.sub:
            return self.arr[self.DP][1]
        else:
            return self.sarr[self.SDP][1]
    def get_OP(self):
        return self.arr[self.OP]
    def get_OP_data(self):
        return self.get_OP()[1]
    def set_DP(self, data):
        self.arr[self.DP][1] = data
    def set_OP(self, data):
        self.arr[self.OP][1] = data
    def inc_DP(self, inc):
        self.arr[self.DP][1] += inc
        
        

        
def run_tape(tape):
    while True:
        if tape.OP > 63:
            sys.exit()
        o, d = tape.get_OP()
        op_inc = 1
        dp_inc = 0
        
        if o == 0:
            op_inc = d
            # print('setting op to : ', d)
        if o == 1:
            dp_inc = d
            # print('setting dp to : ', d)
        if o == 2:
            tape.set_DP(d)
        if o == 3:
            tape.set_OP(tape.get_DP())
        if o == 4:
            tape.inc_DP(d)
        if o == 5:
            tape.inc_DP(d*-1)
        if o == 6:
            tape.set_DP(int(hex(ord(input())).lstrip('0x') ,16))
        if o == 7:
            print(tape.get_DP())
        if o == 15:
            tape.cache = d
        # print(f'{tape.OP}:{tape.DP}')
        tape.OP += op_inc
        tape.DP += dp_inc

        
        
t = Tape()
t.load_ROM('main.2s')
run_tape(t)            
             
        
        