#!/usr/bin/python3
"""
0-nqueens:
Finds all possible solutions to N-Queens problem
"""
import sys


class Queen:
    """ A queen chess piece
    """
    file: int
    rank: int

    def __init__(self, file: int, rank: int):
        """Initialise the Queen instance"""
        self.rank = rank
        self.file = file

    def get_pos(self):
        """Returns the position of the Queen instance as a list [file, rank]"""
        return [self.file, self.rank]

    def __repr__(self) -> str:
        """Returns a print-friendly representation of the Queen instance"""
        return 'Queen[{}][{}]'.format(self.file, self.rank)


def main():
    N: int

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if N < 4:
        print('N must be at least 4')
        exit(1)

    queens = []
    for rank in range(N):
        row = []
        for file in range(N):
            row.append(Queen(file, rank))
        queens.append(row)

    solutions = []
    for file in range(N):
        s = findSolution(N, file, queens)
        if s not in solutions and len(s) == N:
            solutions.append(s)

    solutions_list = [[queen.get_pos() for queen in s] for s in solutions]

    for s in solutions_list:
        print(s)


def findSolution(N: int, row: int, queens: list) -> set:
    """ Finds and return a solution if the first queen is placed on the given
    position
    """
    solution = {queens[0][row]}
    for rank in range(N):
        for file in range(N):
            new_queen = queens[rank][file]
            if any(isAttacking(new_queen, queen) for queen in solution):
                continue
            solution.add(new_queen)

    return solution


def isAttacking(q1: Queen, q2: Queen) -> bool:
    """ Returns true if the two given Queens are attacking eachother
    """
    if any([sameFile(q1, q2), sameRank(q1, q2), sameDiagonalPath(q1, q2)]):
        return True
    return False


def sameFile(q1: Queen, q2: Queen) -> bool:
    """ Returns true if the two Queens have the same file and therefore are
    attacking eachother
    """
    if q1.file == q2.file:
        return True
    return False


def sameRank(q1: Queen, q2: Queen) -> bool:
    """ Returns true if the two Queens have the same rank and therefore are
    attacking eachother
    """
    if q1.rank == q2.rank:
        return True
    return False


def sameDiagonalPath(q1: Queen, q2: Queen) -> bool:
    """ Check if the two Queens are on the same diagonal path and therefore
    are attacking eachother
    """
    if abs(q1.file - q2.file) == abs(q1.rank - q2.rank):
        return True
    return False

if __name__ == '__main__':
    main()
