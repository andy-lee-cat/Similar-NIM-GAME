## Language

- [English](#english)
- [中文](#中文)

---

### English

#### Problem Source

This project originates from a simple game as shown below:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

Each player can draw a single continuous horizontal line with a length of 1 to 3, and the player who draws the last one wins.

Here's an example of a winning position for the first player: since there are only 3 (an odd number of) single `|` left, the first player is guaranteed to draw the last line.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;~~

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

The following configuration is a winning position for the second player, as all possible moves result in a win for the opponent:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

#### Mathematical Representation of the Problem

This problem can be simplified as follows: given an array `arr`, where each element represents an independent count of `|` , and a maximum horizontal line length `maxlen`, determine if the first player has a winning strategy.

#### Solution

This problem can be solved using the SG function (Sprague-Grundy function), which avoids the need to examine every possible move.

In the script `ans.py`, you first input `maxlen`, followed by `arr`. If there exists a winning move, it will output the solution; otherwise, it will display "GG" (indicating a guaranteed loss).

Here’s a sample input-output sequence:
```
Enter the maximum length of the subarray: 3
SG values:
maxlen=1: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
maxlen=2: [0, 1, 2, 3, 1, 4, 3, 2, 1, 4]
maxlen=3: [0, 1, 2, 3, 4, 1, 6, 3, 2, 1]
maxlen=4: [0, 1, 2, 3, 4, 5, 6, 7, 3, 2]
maxlen=5: [0, 1, 2, 3, 4, 5, 6, 7, 8, 3]
Enter the array(> 0): 1 3 5 7
GG
Enter the array(> 0): 1 5 7
Possible moves:
5 -> 2
5 -> 1, 3
7 -> 3, 3
7 -> 2, 2
7 -> 1, 5
Enter the array(> 0): 1 5 1
Possible moves:
1 -> 0
5 -> 1, 1
5 -> 2, 2
Enter the array(> 0): 5 1
GG
Enter the array(> 0): 2 1
Possible moves:
2 -> 1
Enter the array(> 0): 1 1
GG
Enter the array(> 0): 1
Possible moves:
1 -> 0
Enter the array(> 0): 0
GG
```
Here, we first set `maxlen` to 3 and display the SG function values for different lengths. We then input the current configuration.

For example, when the configuration is `1 3 5 7`, it is a losing position, so print("GG"). If we choose reduce 3 to 0, then we get `1 5 7`.

In the configuration `1 5 7`, various winning moves are available, such as reducing 5 to 2 by crossing out 3, or splitting 5 into two independent groups of `1` and `3`.

The following moves follow the same logic.

#### Other Attempts

Attempts were made to modify the rules so that the player who draws the last line loses, similar to a misere Nim game [Misère Nim](https://www.hackerrank.com/challenges/misere-nim-1/problem). However, there are issues here.

Analogous to the anti-NIM problem, if we discuss the cases where all sg=1 separately, the anti-NIM problem allows any large number to be converted into 1 or 0, but in this problem, such property only exists when considering the sg function of each number.

However, in the anti-NIM problem, sg=1 means that you can only operate on it once, but in this problem, sg=1 might mean it can be transformed into two independent parts of the same length.

For example, when `maxlen=3`, `SG(5)=1` only means that this state can be transformed into `SG([2, 2])=0`, where the original sg=0 means no operations can be performed anymore, thus it can be ignored. We need to count the parity of the number of 1s. However, here sg=0 just means that the xor result of several segments is 0, it does not guarantee that no operations can be performed. In fact, under the `[2, 2]` state, the player can still make a move.

This issue has not been fully resolved and may require further analysis.

---

### 中文

#### 问题来源

本项目源自如下一个小游戏：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

每次可以画一条连续的横杠，长度为1-3，画最后一个的人赢。

如下面是一个先手必胜的局面，因为只剩下3个（奇数个）单 `|` ，先手必然可以画最后一条横杠

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;~~

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

下图是一个后手必胜的局面，这里可以简单列出所有情况得知。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

#### 问题数学表达
这个问题可以简化为，给定一个数组`arr`，每个元素为相互独立的 | 个数，给定划线长度的最大值`maxlen`，问是否先手可取胜。

#### 问题求解
这个问题可以用SG函数辅助解答，不需要遍历所有情况。

`ans.py`中输入`maxlen`，再输入`arr`，如存在可行解，会输出解，否则输出"GG"。

如下是一组典型输入输出:
```
Enter the maximum length of the subarray: 3
SG values:
maxlen=1: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
maxlen=2: [0, 1, 2, 3, 1, 4, 3, 2, 1, 4]
maxlen=3: [0, 1, 2, 3, 4, 1, 6, 3, 2, 1]
maxlen=4: [0, 1, 2, 3, 4, 5, 6, 7, 3, 2]
maxlen=5: [0, 1, 2, 3, 4, 5, 6, 7, 8, 3]
Enter the array(> 0): 1 3 5 7
GG
Enter the array(> 0): 1 5 7
Possible moves:
5 -> 2
5 -> 1, 3
7 -> 3, 3
7 -> 2, 2
7 -> 1, 5
Enter the array(> 0): 1 5 1
Possible moves:
1 -> 0
5 -> 1, 1
5 -> 2, 2
Enter the array(> 0): 5 1
GG
Enter the array(> 0): 2 1
Possible moves:
2 -> 1
Enter the array(> 0): 1 1
GG
Enter the array(> 0): 1
Possible moves:
1 -> 0
Enter the array(> 0): 0
GG
```
首先指定`maxlen`为3，首先打印不同`maxlen`时的SG函数，然后开始输入当前局面。

当局面为1 3 5 7 时是必败局面，因此输出"GG"，走任意一步，比如说将3全部划掉，得到局面1 5 7

局面1 5 7给出了多种可行解，比如将5划3个变成2，或5划掉中间1个得到独立的1 3，都是必胜解。

后面同理。

#### 其他尝试

尝试修改为划掉最后一个的输，类比反常NIM问题 [OI Wiki 反常游戏](https://next.oi-wiki.org/math/game-theory/misere-game/) 。但是这里存在问题。

类比反NIM问题，将全sg=1单独讨论，反NIM问题可将任意大数字转化为1或0，而本问题在考虑每个数字的sg函数时才具备这个性质。

但是反NIM问题的sg=1意味着只能在上面操作一次，但这个问题可能意味着sg=1可以转化成两段独立的长度相同的部分。

如`maxlen=3`时，`SG(5)=1`仅仅以为着这个状态可以转化成`SG([2, 2])=0`，原始的sg=0以为着不能在上面进行操作了，因此可以忽略，统计1的个数的奇偶性，但是这里sg=0只是意味着几段数据异或的结果是0，不能保证在上面不能操作了，事实上`[2,2]`状态下，先手方还可以操作。

这里这个问题还没有完全解决，可能还需要深入分析。
