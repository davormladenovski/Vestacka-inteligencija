from searching_framework import Problem
from searching_framework import astar_search
import math


class find_the_house(Problem):

    def __init__(self, covece, kukja, nasoka_kukja):
        self.covece = covece
        self.kukja = kukja
        self.nasoka_kukja = nasoka_kukja

        initial_state = (covece, kukja, nasoka_kukja)

        super().__init__(initial_state)

        self.allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4),
                        (2, 4), (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):

        actions = {}

        new_state = self.stoj(state)
        if self.is_valid(new_state):
            actions["Stoj"] = new_state

        new_state = self.gore_1(state)
        if self.is_valid(new_state):
            actions["Gore 1"] = new_state

        new_state = self.gore_2(state)
        if self.is_valid(new_state):
            actions["Gore 2"] = new_state

        new_state = self.gore_desno_1(state)
        if self.is_valid(new_state):
            actions["Gore-desno 1"] = new_state

        new_state = self.gore_desno_2(state)
        if self.is_valid(new_state):
            actions["Gore-desno 2"] = new_state

        new_state = self.gore_levo_1(state)
        if self.is_valid(new_state):
            actions["Gore-levo 1"] = new_state

        new_state = self.gore_levo_2(state)
        if self.is_valid(new_state):
            actions["Gore-levo 2"] = new_state

        return actions

    def gore_levo_1(self, state):
        covece, kukja, nasoka = state
        c_x, c_y = covece
        kukja, nasoka = self.pomesti_kukja(kukja, nasoka)
        covece = (c_x - 1, c_y + 1)

        return covece, kukja, nasoka

    def gore_levo_2(self, state):
        covece, kukja, nasoka = state
        c_x, c_y = covece
        kukja, nasoka = self.pomesti_kukja(kukja, nasoka)
        covece = (c_x - 2, c_y + 2)

        return covece, kukja, nasoka

    def gore_desno_1(self, state):
        covece, kukja, nasoka = state
        c_x, c_y = covece
        kukja, nasoka = self.pomesti_kukja(kukja, nasoka)
        covece = (c_x + 1, c_y + 1)

        return covece, kukja, nasoka

    def gore_desno_2(self, state):
        covece, kukja, nasoka = state
        c_x, c_y = covece
        kukja, nasoka = self.pomesti_kukja(kukja, nasoka)
        covece = (c_x + 2, c_y + 2)

        return covece, kukja, nasoka

    def stoj(self, state):
        covece, kukja, nasoka = state
        kukja, nasoka = self.pomesti_kukja(kukja, nasoka)

        return covece, kukja, nasoka

    def gore_2(self, state):
        covece, kukja, nasoka = state
        c_x, c_y = covece
        kukja, nasoka = self.pomesti_kukja(kukja, nasoka)
        covece = (c_x, c_y + 2)

        return covece, kukja, nasoka

    def gore_1(self, state):
        covece, kukja, nasoka = state
        c_x, c_y = covece
        kukja, nasoka = self.pomesti_kukja(kukja, nasoka)
        covece = (c_x, c_y + 1)

        return covece, kukja, nasoka

    def pomesti_kukja(self, kukja, nasoka):

        k_x, k_y = kukja

        if nasoka == "desno":
            k_x += 1
            if 0 <= k_x <= 4:
                kukja = (k_x, k_y)
            else:
                nasoka = "levo"
                kukja = (k_x - 2, k_y)
        elif nasoka == "levo":
            k_x -= 1
            if 0 <= k_x <= 4:
                kukja = (k_x, k_y)
            else:
                nasoka = "desno"
                kukja = (k_x + 2, k_y)

        return kukja, nasoka

    def is_valid(self, state):
        covece, kukja, nasoka = state
        c_x, c_y = covece

        if covece not in self.allowed and covece != kukja:
            return False

        if c_x < 0 or c_y < 0 or c_x > 4 or c_y > 8:
            return False

        return True

    def goal_test(self, state):
        covece, kukja, nasoka = state
        if covece == kukja:
            return True
        else:
            return False

    def h(self, node):
        covece, kukja, nasoka = node.state
        c_x, c_y = covece
        k_x, k_y = kukja

        dx = abs(c_x - k_x)
        dy = abs(c_y - k_y)
        distance = max(dx, dy)

        return distance / 3


if __name__ == '__main__':
    covece_koordinati = tuple(map(int, input().split(",")))
    kukja_koordinati = tuple(map(int, input().split(",")))
    nasoka_kukja = input()

    problem = find_the_house(covece_koordinati, kukja_koordinati, nasoka_kukja)
    solution = astar_search(problem)

    if solution is not None:
        print(solution.solution())
    else:
        print("[]")
