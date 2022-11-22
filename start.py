from tests import Tester
import numpy as np
from matplotlib import pyplot as plt


def main(n_bound: int, m_bound: int, inv_type: str = "invalid"):
    test_cases = Tester
    n = n_bound
    m = m_bound
    file = open("../test.txt", "w")
    test = test_cases.generate_valid_test(n, m)
    file.write(str(n) + "\n" + str(m) + "\n")
    for c in test:
        file.write(f"{c['figure']} {c['color']} {c['pos'][0]} {c['pos'][1]}\n")

    file.close()

    file = open("../test_i.txt", "w")
    test_i = test_cases.generate_invalid_test(n, m, invalid_type=inv_type)
    file.write(str(n) + "\n" + str(m) + "\n")
    for c in test_i:
        file.write(f"{c['figure']} {c['color']} {c['pos'][0]} {c['pos'][1]}\n")
    file.close()

    plt.figure(figsize=(n, n))
    ax = plt.gca()
    ax.set_xticks(np.arange(n) + 1)
    ax.set_yticks(np.arange(n) + 1)
    ax.set_xticklabels(np.arange(1, n + 1))
    ax.set_yticklabels(np.arange(1, n + 1))
    ax.grid()

    for c in test:
        if c['color'] == "White":
            color = "r"
        else:
            color = "k"
        if c['figure'] == "King":
            plt.text(c['pos'][0] - 0.5, c['pos'][1] - 0.5, "♔", color=color, fontsize=30, horizontalalignment='center',
                     verticalalignment='center')
        elif c['figure'] == "Queen":
            plt.text(c['pos'][0] - 0.5, c['pos'][1] - 0.5, "♕", color=color, fontsize=30, horizontalalignment='center',
                     verticalalignment='center')
        elif c['figure'] == "Rook":
            plt.text(c['pos'][0] - 0.5, c['pos'][1] - 0.5, "♖", color=color, fontsize=30, horizontalalignment='center',
                     verticalalignment='center')
        elif c['figure'] == "Bishop":
            plt.text(c['pos'][0] - 0.5, c['pos'][1] - 0.5, "♗", color=color, fontsize=30, horizontalalignment='center',
                     verticalalignment='center')
        elif c['figure'] == "Knight":
            plt.text(c['pos'][0] - 0.5, c['pos'][1] - 0.5, "♘", color=color, fontsize=30, horizontalalignment='center',
                     verticalalignment='center')
        elif c['figure'] == "Pawn":
            plt.text(c['pos'][0] - 0.5, c['pos'][1] - 0.5, "♙", color=color, fontsize=30, horizontalalignment='center',
                     verticalalignment='center')

    plt.show()


if __name__ == "__main__":
    print("Enter n:")
    n = int(input())
    print("Enter m:")
    m = int(input())
    print("Enter invalid type:")
    inv_type = input()
    if not inv_type:
        inv_type = "invalid"
    main(n, m, inv_type=inv_type)
