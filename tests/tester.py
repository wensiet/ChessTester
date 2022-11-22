from random import randint


class Tester:

    @staticmethod
    def generate_valid_test(n_bound: int, m_bound: int):
        figures = ["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"]
        colors = ["White", "Black"]
        bk = False
        wk = False
        test_list = []
        taken_pos = []

        # generate a random number from 1 to 20
        n = n_bound
        m = m_bound
        for i in range(m):
            # generate a random position
            pos = [randint(1, n), randint(1, n)]
            while pos in taken_pos:
                pos = [randint(1, n), randint(1, n)]
            taken_pos.append(pos)
            # generate a random figure
            figure = figures[randint(0, 5)]
            if figure == "King" and wk or figure == "King" and bk:
                while figure == "King":
                    figure = figures[randint(0, 5)]

            # generate a random color
            color = colors[randint(0, 1)]
            if figure == "King":
                if color == "White":
                    wk = True
                else:
                    bk = True
            test_list.append({"pos": pos, "figure": figure, "color": color})
        return test_list

    @staticmethod
    def generate_invalid_test(n_bound: int, m_bound: int, invalid_type: str = "invalid"):
        figures = ["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"]
        invalid_figures = ["Knig", "Quen", "Rok", "Bihsop", "Knigt", "Panw"]
        colors = ["White", "Black"]
        invalid_colors = ["Whit", "Blak"]
        bk = False
        wk = False
        test_list = []
        taken_pos = []
        # generate a random number from 1 to 20
        n = n_bound
        m = m_bound

        if invalid_type == "Invalid piece position":
            for i in range(m):
                # generate a random position
                pos = [randint(1, n) + randint(randint(1, n), n + 10), randint(1, n)]
                # generate a random figure
                figure = figures[randint(0, 5)]
                if figure == "King" and wk or figure == "King" and bk:
                    while figure == "King":
                        figure = figures[randint(0, 5)]

                color = colors[randint(0, 1)]
                if figure == "King":
                    if color == "White":
                        wk = True
                    else:
                        bk = True
                test_list.append({"pos": pos, "figure": figure, "color": color})
            return test_list
        elif invalid_type == "Invalid piece type":
            for i in range(m):
                # generate a random position
                pos = [randint(1, n), randint(1, n)]
                while pos in taken_pos:
                    pos = [randint(1, n), randint(1, n)]
                taken_pos.append(pos)
                # generate a random figure
                figure = invalid_figures[randint(0, 5)]
                if figure == "King" and wk or figure == "King" and bk:
                    while figure == "King":
                        figure = figures[randint(0, 5)]

                # generate a random color
                color = colors[randint(0, 1)]
                if figure == "King":
                    if color == "White":
                        wk = True
                    else:
                        bk = True
                test_list.append({"pos": pos, "figure": figure, "color": color})
            return test_list
        elif invalid_type == "Invalid color":
            for i in range(m):
                # generate a random position
                pos = [randint(1, n), randint(1, n)]
                while pos in taken_pos:
                    pos = [randint(1, n), randint(1, n)]
                taken_pos.append(pos)
                # generate a random figure
                figure = figures[randint(0, 5)]
                if figure == "King" and wk or figure == "King" and bk:
                    while figure == "King":
                        figure = figures[randint(0, 5)]

                # generate a random color
                color = invalid_colors[randint(0, 1)]
                if figure == "King":
                    if color == "White":
                        wk = True
                    else:
                        bk = True
                test_list.append({"pos": pos, "figure": figure, "color": color})
            return test_list
        elif invalid_type == "Invalid given Kings":
            for i in range(m):
                # generate a random position
                pos = [randint(1, n), randint(1, n)]
                while pos in taken_pos:
                    pos = [randint(1, n), randint(1, n)]
                taken_pos.append(pos)
                # generate a random figure
                figure = figures[randint(0, 5)]
                # generate a random color
                color = colors[randint(0, 1)]
                test_list.append({"pos": pos, "figure": figure, "color": color})
            return test_list
        else:
            return None
