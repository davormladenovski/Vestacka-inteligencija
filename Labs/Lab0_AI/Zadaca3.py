import os
import random

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, position):
        self.x, self.y = position


class Game:
    def __init__(self, width, height, matrix):
        self.points = 0
        self.matrix = matrix
        self.width = width
        self.height = height
        self.player = Player()
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == ".":
                    self.points += 1

    def check_valid_position(self, i, j):
        if (0 <= i < self.height and 0 <= j < self.width ):
            return True

    def play_game(self):
        while self.points > 0:
            possible_moves = []
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in moves:
                new_x = self.player.x + dx
                new_y = self.player.y + dy
                if self.check_valid_position(new_x, new_y):
                    possible_moves.append((new_x, new_y))

            if not possible_moves:
                break

            newx, newy = random.choice(possible_moves)

            self.player.move((newx, newy))

            print(f"[{newx}, {newy}]")

            if self.matrix[newx][newy] == ".":
                self.points -= 1
                self.matrix[newx][newy] = "#"


class Pacman:
    def __init__(self, width, height, matrix):
        self.game = Game(width, height, matrix)

    def play_game(self):
        self.game.play_game()


if __name__ == "__main__":
    width = int(input())
    height = int(input())

    matrix = []

    for i in range(height):
        row = input().strip()
        matrix.append(list(row))

    pacman = Pacman(width, height, matrix)
    pacman.play_game()
