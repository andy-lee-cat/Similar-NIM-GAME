from collections import defaultdict

class SGtable:
    def __init__(self, maxlen, maxval=30):
        """
        sgtable[len][nxtsg] = set([(l0, r0), (l1, r1), ...])
        means that with length len, the next SG value is nxtsg,
        and the possible moves are [(l0, r0), (l1, r1), ...]
        """
        self.sgtable = [[] for _ in range(maxval + 1)]
        self.maxlen = maxlen
        self.maxval = maxval
        self.preCal()

    def preCal(self):
        self.sgtable[0] = []
        self.sgtable[1] = [[(0, 0)]]
        for i in range(2, self.maxval + 1):
            d = defaultdict(set)
            for j in range(i):
                for l in range(1, 1 + min(self.maxlen, i - j)):
                    l, r = min(j, i - j - l), max(j, i - j - l)
                    d[len(self.sgtable[l]) ^ len(self.sgtable[r])].add((l, r))
            for j in range(len(d)):
                if j not in d:
                    break
                self.sgtable[i].append(d[j])

    def appendCal(self, maxval):
        for i in range(len(self.sgtable), maxval + 1):
            d = defaultdict(set)
            for j in range(i):
                for l in range(1, 1 + min(self.maxlen, i - j)):
                    l, r = min(j, i - j - l), max(j, i - j - l)
                    d[self.sgtable[j] ^ self.sgtable[i - j - l]].add((l, r))
            for j in range(len(d)):
                if j not in d:
                    break
                self.sgtable.append(d[j])

    def solve(self, arr, win=0):
        # win=0 when last loss, win=1 when last win
        if win == 0:
            self.solve_last_loss(arr)
        else:
            self.solve_last_win(arr)

    def solve_last_loss(self, arr):
        # 还是没有解决
        sg = [0] * len(arr)
        xor = 0
        for i in range(len(arr)):
            sg[i] = len(self.sgtable[arr[i]])
            xor ^= sg[i]
        ok = False
        for i in range(len(arr)):
            if sg[i] not in (0, 1):
                ok = True
                break
        if not ok:
            # all 0 or 1
            countOne = 0
            for i in range(len(arr)):
                if sg[i] == 1:
                    countOne += 1
            if countOne % 2 == 1:
                print("GG")
            ## 一个给定的长度，maxlen!=1时，sg(len)一定不是0吗
            ## 确实不是
            ## 考虑记数sg=1的个数
            ## 但是这里无法处理一个长度为n，sg为1，转化成长度为x, y，sg(x) = sg(y)的场景
            ## 给两个相同的长度x, x, 和一个长度为0的，效果不一致

    def solve_last_win(self, arr):
        sg = [0] * len(arr)
        xor = 0
        for i in range(len(arr)):
            sg[i] = len(self.sgtable[arr[i]])
            xor ^= sg[i]
        if xor == 0:
            print("GG")
            return
        moves = set()
        for i in range(len(arr)):
            except_sg = xor ^ sg[i]
            if except_sg > sg[i]:
                continue
            for move in self.sgtable[arr[i]][except_sg]:
                moves.add((arr[i], move))
        for move in moves:
            if move[1][0] == 0:
                print(f"{move[0]} -> {move[1][1]}")
            else:
                print(f"{move[0]} -> {move[1][0]}, {move[1][1]}")

def mex(s):
    for i in range(len(s) + 1):
        if i not in s:
            return i
    return -1

def preCal(sg, maxlen, maxval=30):
    # cal SG values
    sg.clear
    sg.extend([0] * (maxval + 1))
    sg[1] = 1
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
    maxlen = 3  # maximum cut length
    maxval = 30  # maximum value of the array
    
    """
    sg[now][nxt] = [[l0, r0], [l1, r1], ...]
    """
    sg = []
    print("SG values:")
    for ml in range(1, 6):
        print(f"maxlen={ml}", end=": ")
        preCal(sg, ml, maxval)
        print(sg[:10])

    sgtable = SGtable(maxlen)
    while True:
        line = input("Enter the array(> 0): ")
        arr = list(map(int, line.split()))
        # 尝试用SG函数解决last loss，处理一些特殊情况，但不太行
        # if len(arr) == sum(arr):
        #     print("ALL ONEs")
        #     continue
        if max(arr) > sgtable.maxval:
            sgtable.appendCal(max(arr))

        sgtable.solve(arr, win)
