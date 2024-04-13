from searching_framework import Problem, breadth_first_graph_search

# Tocna skroz

class Football(Problem):
    def __init__(self, person, ball):
        initial_state = (tuple(person), tuple(ball))
        super().__init__(initial_state)
        self.opponents = ((3, 3), (5, 4))
        self.goal = ((7, 2), (7, 3))

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()

    def successor(self, state):
        actions = {}

        new_state = self.action_person_up(state)
        if new_state is not None:
            actions["Pomesti coveche gore"] = new_state

        new_state = self.action_person_down(state)
        if new_state is not None:
            actions["Pomesti coveche dolu"] = new_state

        new_state = self.action_person_right(state)
        if new_state is not None:
            actions["Pomesti coveche desno"] = new_state

        new_state = self.action_person_up_right(state)
        if new_state is not None:
            actions["Pomesti coveche gore-desno"] = new_state

        new_state = self.action_person_down_right(state)
        if new_state is not None:
            actions["Pomesti coveche dolu-desno"] = new_state

        new_state = self.action_ball_up(state)
        if new_state is not None:
            actions["Turni topka gore"] = new_state

        new_state = self.action_ball_down(state)
        if new_state is not None:
            actions["Turni topka dolu"] = new_state

        new_state = self.action_ball_right(state)
        if new_state is not None:
            actions["Turni topka desno"] = new_state

        new_state = self.action_ball_up_right(state)
        if new_state is not None:
            actions["Turni topka gore-desno"] = new_state

        new_state = self.action_ball_down_right(state)
        if new_state is not None:
            actions["Turni topka dolu-desno"] = new_state

        return actions

    def action_person_up(self, state):
        person, ball = state
        person = list(person)

        person = (person[0], person[1] + 1)

        new_state = (tuple(person), ball)
        if self.check_valid(new_state):
            return new_state
        else:
            return None

    def action_ball_up(self, state):
        person, ball = state
        x_p, y_p = person
        x_b, y_b = ball

        if (x_p, y_p + 1) == (x_b, y_b):
            new_state = ((x_p, y_p + 1), (x_b, y_b + 1))

            if self.check_valid(new_state):
                return new_state
            else:
                return None

    def action_person_down(self, state):
        person, ball = state
        person = list(person)

        person = (person[0], person[1] - 1)

        new_state = (tuple(person), ball)
        if self.check_valid(new_state):
            return new_state
        else:
            return None

    def action_ball_down(self, state):
        person, ball = state
        x_p, y_p = person
        x_b, y_b = ball

        if (x_p, y_p - 1) == (x_b, y_b):
            new_state = ((x_p, y_p - 1), (x_b, y_b - 1))

            if self.check_valid(new_state):
                return new_state
            else:
                return None

    def action_person_right(self, state):
        person, ball = state
        person = list(person)

        person = (person[0] + 1, person[1])

        new_state = (tuple(person), ball)
        if self.check_valid(new_state):
            return new_state
        else:
            return None

    def action_ball_right(self, state):
        person, ball = state
        x_p, y_p = person
        x_b, y_b = ball

        if (x_p + 1, y_p) == (x_b, y_b):
            new_state = ((x_p + 1, y_p), (x_b + 1, y_b))

            if self.check_valid(new_state):
                return new_state
            else:
                return None

    def action_person_up_right(self, state):
        person, ball = state
        person = list(person)

        person = (person[0] + 1, person[1] + 1)

        new_state = (tuple(person), ball)
        if self.check_valid(new_state):
            return new_state
        else:
            return None

    def action_ball_up_right(self, state):
        person, ball = state
        x_p, y_p = person
        x_b, y_b = ball

        if (x_p + 1, y_p + 1) == (x_b, y_b):
            new_state = ((x_p + 1, y_p + 1), (x_b + 1, y_b + 1))

            if self.check_valid(new_state):
                return new_state
            else:
                return None

    def action_person_down_right(self, state):
        person, ball = state
        person = list(person)

        person = (person[0] + 1, person[1] - 1)

        new_state = (tuple(person), ball)
        if self.check_valid(new_state):
            return new_state
        else:
            return None

    def action_ball_down_right(self, state):
        person, ball = state
        x_p, y_p = person
        x_b, y_b = ball

        if (x_p + 1, y_p - 1) == (x_b, y_b):
            new_state = ((x_p + 1, y_p - 1), (x_b + 1, y_b - 1))

            if self.check_valid(new_state):
                return new_state
            else:
                return None

    def check_valid(self, state):
        person, ball = state
        x_p, y_p = person
        x_b, y_b = ball

        if x_p > 7 or x_p < 0 or y_p > 5 or y_p < 0 or x_b > 7 or x_b < 0 or y_b > 5 or y_p < 0:
            return False
        if (x_p, y_p) == (x_b, y_b):
            return False
        if (x_p, y_p) in self.opponents:
            return False
        if (x_b, y_b) in (
                (3 + 1, 3), (3 - 1, 3), (3, 3 + 1), (3, 3 - 1), (3 + 1, 3 + 1), (3 - 1, 3 - 1), (3 + 1, 3 - 1),
                (3 - 1, 3 + 1),
                (3, 3)):
            return False
        if (x_b, y_b) in (
                (5 + 1, 4), (5 - 1, 4), (5, 4 + 1), (5, 4 - 1), (5 + 1, 4 + 1), (5 - 1, 4 - 1), (5 + 1, 4 - 1),
                (5 - 1, 4 + 1),
                (5, 4)):
            return False

        return True

    def goal_test(self, state):
        person, ball = state
        if ball in self.goal:
            return True
        else:
            return False


if __name__ == '__main__':
    person_xy = tuple(map(int, input().split(",")))
    ball_xy = tuple(map(int, input().split(",")))
    problem = Football(person_xy, ball_xy)

    node = breadth_first_graph_search(problem)
    print(node.solution())
