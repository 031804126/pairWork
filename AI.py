# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time     : 2020/10/17 23:06
# @author   : Mo
# @function : 滑动拼图, 类似leetcode 773.滑动拼图 (https://leetcode-cn.com/problems/sliding-puzzle)
# @url      : 类似题目, 773.滑动拼图(https://leetcode-cn.com/problems/sliding-puzzle)
# @algorithm: BFS + A*


from queue import PriorityQueue
import random
import copy


class SlidingPuzzle:
    def parse(self, board):
        """
        sliding puzzle
        Args:
            board: List<List<int>>, like [[2,1,0], [6,5,4], [8,7,3]]
        Returns:
            depth, move_str, board_roads: 移动次数, 按键移动序列(上下左右,wsad), 序列移动过程
        """

        # board的形状：3 * 3, 获取队列高度和宽度
        hight, width = len(board), len(board[0])
        # 将board展成一列, 初始值和目标值
        board_start = tuple([board[i][j] for i in range(hight) for j in range(width)])
        # 目标值为[1,2,3,4,5,6,7,8,9,0]
        board_end = tuple([x for x in range(1, hight * width)] + [0])
        # 计算当前点到目标点的距离, 即A*算法的估计函数
        def cal_distance(idxs):
            distance = 0
            for i in range(len(idxs)):
                if idxs[i] == 0:
                    continue
                distance += abs(i // width - (idxs[i] - 1) // width) + \
                            abs(i % width - (idxs[i] - 1) % width)
            return distance
        # 优先队列，值越小，优先级越高
        pq = PriorityQueue()
        # [优先级, 中间List(3*3=9), 初始值的0索引, 步数, 按键顺序输出序列, 拼图中间转换过程]
        pq.put([0 + cal_distance(board_start), board_start, board_start.index(0), 0, "", []])
        # 已遍历过的序列
        visited = set(board_start)
        # BFS搜索
        while not pq.empty():
            # 获取中间值
            _, board, position, step, move_str, board_roads = pq.get()
            # 最终结果返回, 循环停止条件
            if board == board_end:
                return step, move_str, board_roads
            # BFS遍历上下左右的相邻结点
            for idx in (-width, width, -1, 1):
                # wsad字母 对应 上下左右 的按钮
                id2button = {-1:"a", 1:"d", -width:"w", width:"s"}
                # 下一个需要遍历的点
                neighbor = position + idx
                # 不是相邻点的跳过
                if abs(neighbor // width - position // width) + abs(neighbor % width - position % width) != 1:
                    continue
                # 遍历上下左右符合边界条件的相邻数字(图片)
                if 0 <= neighbor < width * hight:
                    board_mid = list(board)
                    # 交换, 即移动0(即空图片)
                    board_mid[position], board_mid[neighbor] = board_mid[neighbor], board_mid[position]
                    board_new = tuple(board_mid)
                    if board_new not in visited:
                        visited.add(board_new)
                        pq.put([cal_distance(board_new) + step + 1, board_new, neighbor, step + 1,
                                    move_str + id2button[idx], board_roads + [board_mid]])
        # 遍历整个循环都没有，则无解，返回-1
        return -1, None, None


def sliding_puzzle_2(boards, step, swap):
    """
    sliding puzzle
    Args:
        board: List<List<int>>, like [[2,1,0], [6,5,4], [8,7,3]]
        step: Int, like 10, 停止步数
        swap: List<int>, like [3,2], 交换的格子
    Returns:
        move_str_res, swap_res: 按键移动序列(上下左右,wsad), 移动交换的格子list
    """
    def sliding_puzzle_1(board):
        """
        sliding puzzle
        Args:
            board: List<List<int>>, like [[2,1,0], [6,5,4], [8,7,3]]
            step_swap: Int, like 10, 停止步数
        Returns:
            depth, move_str, board_roads: 移动次数, 按键移动序列(上下左右,wsad), 序列移动过程
        """

        # board的形状：3 * 3, 获取队列高度和宽度
        hight, width = len(board), len(board[0])
        # 将board展成一列, 初始值和目标值
        board_start = tuple([board[i][j] for i in range(hight) for j in range(width)])
        # 目标值为[1,2,3,4,5,6,7,8,9,0]
        board_end = tuple([x for x in range(1, hight * width)] + [0])

        # 计算当前点到目标点的距离, 即A*算法的估计函数
        def cal_distance(idxs):
            distance = 0
            for i in range(len(idxs)):
                if idxs[i] == 0:
                    continue
                distance += abs(i // width - (idxs[i] - 1) // width) + \
                            abs(i % width - (idxs[i] - 1) % width)
            return distance

        # 优先队列，值越小，优先级越高
        pq = PriorityQueue()
        # [优先级, 中间List(3*3=9), 初始值的0索引, 步数, 按键顺序输出序列, 拼图中间转换过程]
        pq.put([0 + cal_distance(board_start), board_start, board_start.index(0), 0, "", []])
        # 已遍历过的序列
        visited = set(board_start)
        # BFS搜索
        while not pq.empty():
            # 获取中间值
            _, board, position, step, move_str, board_roads = pq.get()
            # 最终结果返回, 循环停止条件
            if board == board_end:
                return step, move_str, board_roads
            # BFS遍历上下左右的相邻结点
            for idx in (-width, width, -1, 1):
                # wsad字母 对应 上下左右 的按钮
                id2button = {-1: "a", 1: "d", -width: "w", width: "s"}
                # 下一个需要遍历的点
                neighbor = position + idx
                # 不是相邻点的跳过
                if abs(neighbor // width - position // width) + abs(neighbor % width - position % width) != 1:
                    continue
                # 遍历上下左右符合边界条件的相邻数字(图片)
                if 0 <= neighbor < width * hight:
                    board_mid = list(board)
                    # 交换, 即移动0(即空图片)
                    board_mid[position], board_mid[neighbor] = board_mid[neighbor], board_mid[position]
                    board_new = tuple(board_mid)
                    if board_new not in visited:
                        visited.add(board_new)
                        pq.put([cal_distance(board_new) + step + 1, board_new, neighbor, step + 1,
                                move_str + id2button[idx], board_roads + [board_mid]])
        # 遍历整个循环都没有，则无解，返回-1
        return -1, None, None

    swap_res = []
    # 返回完整结果, 取截止到step步数时
    _, move_str_1, board_roads_1 = sliding_puzzle_1(boards)
    move_str = move_str_1[:step]
    board_step = board_roads_1[step-1]
    # 强制交换格子
    board_step[swap[0] - 1], board_step[swap[1] - 1] = board_step[swap[1] - 1], board_step[swap[0] - 1]
    # 强转二维数组
    board_step_33 = [board_step[0:3], board_step[3:6], board_step[6:9]]
    # 再次遍历
    step_2, move_str_2, board_roads_2 = sliding_puzzle_1(board_step_33)
    # 有解则返回
    if step_2 != -1:
        print(0)
        move_str_res = move_str + move_str_2
    else:  # 无解的时候使用了随机法获取 一对交换格子, 直到有解为止
        while True:
            swap_0 = random.randint(0, 8)
            swap_1 = random.randint(0, 8)
            if swap_0 != swap_1:
                board_step_copy = copy.deepcopy(board_step)
                board_step_copy[swap_0], board_step_copy[swap_1] = board_step_copy[swap_1], board_step_copy[swap_0]
                board_step_copy_33 = [board_step_copy[0:3], board_step_copy[3:6], board_step_copy[6:9]]
                step_3, move_str_3, board_roads_3 = sliding_puzzle_1(board_step_copy_33)
                print(-1)
                print(step_3)
                if step_3 != -1:
                    move_str_res = move_str + move_str_3
                    swap_res = [swap_0 + 1, swap_1 + 1]
                    return move_str_res, swap_res
    return move_str_res, swap_res



if __name__ == "__main__":
    #########
    # 测试一, 纯粹的滑动拼图
    # #########
    sp = SlidingPuzzle()
    board = [[2,1,0],
             [6,5,4],
             [8,7,3]]
    res = sp.parse(board)
    if res[0] != -1:
        print(res)
        print(res[0])
        print(res[1])
        print(res[2])

        sps = 0


    ##########
    # 测试二, 增加规则2(移动到一定步数的时候，我们会强制调换此时棋盘上的两个格子，由于此时棋盘不一定有解。
    # 所以我们给了你一次自由调换的机会，你可以调换任意两个图片的位置，注意这个自由调换只能在棋盘无解的情况下使用，且需紧接着强制调换的操作。
    ##########
    move_str_res = ""
    swap_res = []
    # 第二个条件, step步时则替换图片
    step = 10
    swap = [3, 5]
    # board = [[1, 8, 0],
    #          [6, 5, 4],
    #          [2, 7, 3]]
    board = [[2, 1, 0],
             [6, 5, 4],
             [8, 7, 3]]
    res = sliding_puzzle_2(board, step, swap)
    if res[0] != -1:
        print(res)
        print(res[0])
        print(res[1])
    sps = 0

