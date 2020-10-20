import unittest
from AI import sliding_puzzle_2

class MyTestCase(unittest.TestCase):


    def test_something(self):
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
            # print(res)
            print(res[0])
            print(res[1])


if __name__ == '__main__':
    unittest.main()
