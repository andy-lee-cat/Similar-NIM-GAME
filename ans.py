def mex(s):
    for i in range(len(s) + 1):
        if i not in s:
            return i
    return -1

def preCal(sg, win, maxlen, maxval=30):
    # cal SG values
    sg.extend([0] * (maxval + 1))
    if win == 1:
        # last win
        sg[0] = 0
        sg[1] = 1
    else:
        # last loss, but can't use SG function to solve
        # cant work
        sg[1] = 0
        sg[0] = 0
    for i in range(2, maxval + 1):
        s = set()
        for j in range(i):
            for l in range(1, 1 + min(maxlen, i - j)):
                s.add(sg[j] ^ sg[i - j - l])
        sg[i] = mex(s)

if __name__ == '__main__':
    # win = int(input("Enter 1 when winner is the last player, 0 otherwise: "))
    win = 1  # last win. last loss is much more difficult
    # example:
    # [1, 5] maxlen=3
    # gg when last win, but win when last loss
    # when last loss, sg(1) should be 0, but sg([1, 1]) should be 1
    # sg([1, 1]) != sg(1) ^ sg(1), maybe cant use SG function to solve
    maxlen = int(input("Enter the maximum length of the subarray: "))
    sg = []
    maxlen = 3  # maximum cut length
    maxval = 30  # maximum value of the array
    
    for ml in range(1, 6):
        print(f"maxlen={ml}", end=": ")
        preCal(sg, win, ml, maxval)
        print(sg[:10])

    preCal(sg, win, maxlen, maxval)
    while True:
        line = input("Enter the array(> 0): ")
        arr = list(map(int, line.split()))
        # 尝试用SG函数解决last loss，处理一些特殊情况，但不太行
        # if len(arr) == sum(arr):
        #     print("ALL ONEs")
        #     continue
        if max(arr) > maxval:
            maxval = max(arr)
            preCal(sg, win, maxlen, maxval)
            
        xor = 0
        d = dict()
        for v in arr:
            xor ^= sg[v]
            d.setdefault(sg[v], []).append(v)
        
        if xor == 0:
            print("GG")
            continue
        # win
        possible_moves = dict()
        for sgval, vs in d.items():
            for v in vs:
                nxtsg = xor ^ sgval
                for j in range(v):
                    for l in range(1, 1 + min(maxlen, v - j)):
                        if sg[j] ^ sg[v - j - l] == nxtsg:
                            left, right = j, v - j - l
                            if left > right:
                                left, right = right, left
                            possible_moves.setdefault(v, set()).add((left, right))
        
        print("Possible moves:")
        for v, moves in possible_moves.items():
            for move in moves:
                if move[0] == 0:
                    print(f"{v} -> {move[1]}")
                else:
                    print(f"{v} -> {move[0]}, {move[1]}")
