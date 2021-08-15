import os
import time
import random

import keyboard
from numpy import array

lines = 13
cols = 26
os.system("mode con cols={} lines={}".format(cols, lines))

class Snake(object):

    def __init__(self):
        self.snake = [[random.randrange(0, lines), random.randrange(0, cols)]]
        self.display_ar = array([0] * lines * cols)
        self.display_ar.shape = (lines, cols)
        self.direction = (-1, 0)
        self.is_have_eat = True
        self.is_moved = False
        self.food = [random.randrange(0, lines), random.randrange(0, cols)]

    def flush(self, time_interval=0.4):
        while True:
            # 绘制打印
            display = self.display_ar.copy()
            is_first = True
            for j in self.snake:
                if is_first:
                    head_index = tuple(j)
                    is_first = False
                else:
                    display[tuple(j)] = 1
            display[head_index] = 2
            if len(self.snake) == lines * cols:
                print('win!')
                break
            if not self.is_have_eat:
                display[tuple(self.food)] = 3
            if self.is_have_eat:
                food = [random.randrange(0, lines), random.randrange(0, cols)]
                if food not in self.snake:
                    self.food = food
                    self.is_have_eat = False
            display_str = ''
            for j, k in enumerate(display):
                line_str = "".join(map(str, k.tolist()))
                line_str = line_str.replace('0', ".")
                line_str = line_str.replace('1', "*")
                line_str = line_str.replace('2', "o")
                line_str = line_str.replace('3', "x")
                display_str = display_str + line_str + '\n'
            print(display_str[:-1], end='')
            self.is_moved = True
            # 移动
            time.sleep(time_interval)
            head = [(self.snake[0][0] + self.direction[0]) % lines, (self.snake[0][1] + self.direction[1]) % cols]
            self.snake.insert(0, head)
            self.is_moved = False
            if head == self.food:
                self.is_have_eat = True
                time_interval -= 0.002
                continue
            if head in self.snake[1:]:
                break
            self.snake.pop(-1)

        len_display = len(display_str)
        display_str = '.'*len_display
        print(display_str[:len_display//2-4]+' Failed '+display_str[len_display//2-2:len_display-cols-1], end='')
        input()

    def start(self):
        keyboard.add_hotkey('up', self.key_control, args=('up',))
        keyboard.add_hotkey('down', self.key_control, args=('down',))
        keyboard.add_hotkey('right', self.key_control, args=('right',))
        keyboard.add_hotkey('left', self.key_control, args=('left',))
        self.flush()

    def key_control(self, key):
        if not self.is_moved:
            return
        if key == 'up' and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == 'down' and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif key == 'right' and self.direction != (0, -1):
            self.direction = (0, 1)
        elif key == 'left' and self.direction != (0, 1):
            self.direction = (0, -1)


if __name__ == '__main__':
    snake = Snake()
    snake.start()
