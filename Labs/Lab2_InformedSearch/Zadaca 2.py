from searching_framework import Problem, astar_search


class labyrinth(Problem):
    def __init__(self, n, walls, covece, kukja):
        self.n = n
        self.walls = walls
        self.kukja = kukja
        self.covece = covece
        initial = covece
        super().__init__(initial)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):
        actions = {}

        new_state = self.action_gore(state)
        if self.is_valid(new_state):
            actions["Gore"] = new_state

        new_state = self.action_dolu(state)
        if self.is_valid(new_state):
            actions["Dolu"] = new_state

        new_state = self.action_levo(state)
        if self.is_valid(new_state):
            actions["Levo"] = new_state

        new_state = self.action_desno(state)
        if self.is_valid(new_state):
            new_state = self.action_desno(new_state)
            if self.is_valid(new_state):
                actions["Desno 2"] = new_state

        new_state = self.action_desno(state)
        if self.is_valid(new_state):
            new_state = self.action_desno(new_state)
            if self.is_valid(new_state):
                new_state = self.action_desno(new_state)
                if self.is_valid(new_state):
                    actions["Desno 3"] = new_state

        return actions

    def action_gore(self, state):
        covece = state
        x_c, y_c = covece
        covece = (x_c, y_c + 1)
        return covece

    def action_dolu(self, state):
        covece = state
        x_c, y_c = covece
        covece = (x_c, y_c - 1)
        return covece

    def action_levo(self, state):
        covece = state
        x_c, y_c = covece
        covece = (x_c - 1, y_c)
        return covece

    def action_desno(self, state):
        covece = state
        x_c, y_c = covece
        covece = (x_c + 1, y_c)
        return covece


    def is_valid(self, state):
        covece = state
        x_c, y_c = covece
        if covece in self.walls:
            return False

        if x_c < 0 or y_c < 0 or x_c > (self.n-1) or y_c > (self.n-1):
            return False

        return True

    def goal_test(self, state):
        covece = state

        if covece == self.kukja:
            return True
        else:
            return False

    def h(self, node):
        covece = node.state
        c_x, c_y = covece
        k_x, k_y = self.kukja

        dx = abs(c_x - k_x)
        dy = abs(c_y - k_y)
        distance = max(dx, dy)

        return distance/3


if __name__ == '__main__':
    N = int(input())
    num_walls = int(input())
    walls = list()
    for wall in range(num_walls):
        walls.append(tuple(map(int, input().split(","))))

    covece = tuple(map(int, input().split(",")))
    kukja = tuple(map(int, input().split(",")))

    problem = labyrinth(N, walls, covece, kukja)
    sol = astar_search(problem)
    if sol is not None:
        print(sol.solution())

    else:
        print("[]")
