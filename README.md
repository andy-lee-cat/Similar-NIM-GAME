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

Each player can draw 1-3 horizontal lines, and the player who draws the last one wins.

For example, the following is a winning position for the first player because only 3 single `|` are left, so the first player is guaranteed to reach the last line:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

The following configuration is a winning position for the second player, as all possible moves result in a win for the opponent:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

#### Mathematical Representation of the Problem

This problem can be simplified as follows: given an array `arr`, where each element represents the number of `|` in each separate group, and a maximum line length `maxlen`, determine if the first player has a winning strategy.

#### Solution

This problem can be solved using the SG function (Sprague-Grundy function), which avoids the need to examine every possible move.

In the script `ans.py`, you first input `maxlen`, followed by `arr`. If there exists a winning move, it will output the solution; otherwise, it will display "GG" (indicating a guaranteed loss).

Here’s a sample input-output sequence:
```
Enter the maximum length of the subarray: 3
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

Attempts were made to modify the rules so that the player who draws the last line loses, similar to a reverse NIM game. However, this poses challenges as defining the SG function becomes problematic.

If 1 is a losing state, then `SG([1])=0`, but if `[1, 1]` is a winning state, `SG([1, 1]) != 0`. This contradicts the result of `SG([1, 1]) = SG([1]) ^ SG([1])`.

Unlike the reverse NIM problem, it is challenging to apply this approach here, as arbitrary values cannot be simplified to 1 or 0. This indicates that alternative methods might be needed to solve this problem.

---

### 中文

#### 问题来源

本项目源自如下一个小游戏：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

每次可以画1-3个横杠，画最后一个的人赢。

如下面是一个先手必胜的局面，因为只剩下3个单|，先手必然走到最后一个

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;

下图是一个后手必胜的局面，这里可以简单列出所有情况得知。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;

&nbsp;&nbsp;&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;~~&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;

#### 问题数学表达
这个问题可以简化为，给定一个数组`arr`，每个元素为相互独立的 | 个数，给定最大划线长度`maxlen`，问是否先手可取胜。

#### 问题求解
这个问题可以用SG函数辅助解答，不需要遍历所有情况。

`ans.py`中输入`maxlen`，再输入`arr`，如存在可行解，会输出解，否则输出"GG"。

如下是一组典型输入输出:
```
Enter the maximum length of the subarray: 3
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

尝试修改为划掉最后一个的输，类比反NIM问题。但是这里存在问题，SG函数难以定义。

1为必败态，则有`SG([1])=0`，但是又有[1, 1]为必胜态，应具有`SG([1, 1]) != 0`，这里与`SG([1, 1]) = SG([1]) ^ SG([1])`矛盾

类比反NIM问题，将全1单独讨论，但是反NIM问题可将任意大数字转化为1或0，而本问题不具备这个性质，因此可能需要其他工具解决这一问题。