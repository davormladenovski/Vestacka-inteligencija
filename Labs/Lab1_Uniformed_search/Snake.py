from searching_framework import Problem, breadth_first_graph_search


#Tocna skroz

class Snake3(Problem):

    def __init__(self, zeleni_jabolki, crveni_jabolki):
        self.crveni_jabolki = crveni_jabolki
        initial_state = (((0, 9), (0, 8), (0, 7)), "-y", zeleni_jabolki)
        super().__init__(initial_state)

    def successor(self, state):
        actions = {}

        new_state_left = self.action_left(state)
        if new_state_left is not None:
            new_state_left = self.check_apple(new_state_left)
            actions["SvrtiLevo"] = new_state_left

        new_state_right = self.action_right(state)
        if new_state_right is not None:
            new_state_right = self.check_apple(new_state_right)
            actions["SvrtiDesno"] = new_state_right

        new_state_forward = self.action_forward(state)
        if new_state_forward is not None:
            new_state_forward = self.check_apple(new_state_forward)
            actions["ProdolzhiPravo"] = new_state_forward

        return actions

    def check_apple(self, state):
        zmija, face, jabolki = list(state[0]), state[1], list(state[2])

        if zmija[-1] not in jabolki:
            zmija.pop(0)
        else:
            jabolki.remove(zmija[-1])

        return (tuple(zmija), face, tuple(jabolki))

    def is_state_valid(self, state):
        zmija, face, jabolki = list(state[0]), state[1], list(state[2])
        x, y = zmija[-1][0], zmija[-1][1]
        if x < 0 or y < 0 or x >= 10 or y >= 10:
            return False

        if (x, y) in self.crveni_jabolki:
            return False

        if (x, y) in zmija and zmija.count((x, y)) > 1:
            return False

        return True

    def actions(self, state):
        return self.successor(state).keys()

    def action_left(self, state):
        zmija, face, jabolki = list(state[0]), state[1], list(state[2])
        x, y = zmija[-1][0], zmija[-1][1]

        if face == "-y":
            zmija.append((x + 1, y))
            face = "+x"

        elif face == "-x":
            zmija.append((x, y - 1))
            face = "-y"

        elif face == "+y":
            zmija.append((x - 1, y))
            face = "-x"

        elif face == "+x":
            zmija.append((x, y + 1))
            face = "+y"

        new_state = (tuple(zmija), face, tuple(jabolki))
        if self.is_state_valid(new_state):
            return new_state
        else:
            return None

    def action_right(self, state):
        zmija, face, jabolki = list(state[0]), state[1], list(state[2])
        x, y = zmija[-1][0], zmija[-1][1]

        if face == "-y":
            zmija.append((x - 1, y))
            face = "-x"

        elif face == "-x":
            zmija.append((x, y + 1))
            face = "+y"

        elif face == "+y":
            zmija.append((x + 1, y))
            face = "+x"

        elif face == "+x":
            zmija.append((x, y - 1))
            face = "-y"

        new_state = (tuple(zmija), face, tuple(jabolki))
        if self.is_state_valid(new_state):
            return new_state
        else:
            return None

    def action_forward(self, state):
        zmija, face, jabolki = list(state[0]), state[1], list(state[2])
        x, y = zmija[-1][0], zmija[-1][1]

        if face == "-y":
            zmija.append((x, y - 1))

        elif face == "-x":
            zmija.append((x - 1, y))

        elif face == "+y":
            zmija.append((x, y + 1))

        elif face == "+x":
            zmija.append((x + 1, y))

        new_state = (tuple(zmija), face, tuple(jabolki))
        if self.is_state_valid(new_state):
            return new_state
        else:
            return None

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        if len(state[2]) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    broj_z = int(input())
    zeleni = list()
    for i in range(broj_z):
        zeleni.append(tuple(map(int, input().split(","))))

    broj_c = int(input())
    crveni = list()
    for i in range(broj_c):
        crveni.append(tuple(map(int, input().split(","))))

    crveni = tuple(crveni)
    zeleni = tuple(zeleni)

    problem = Snake3(zeleni, crveni)

    node = breadth_first_graph_search(problem)
    if node is not None:

        print(node.solution())
    else:
        print("[]")
