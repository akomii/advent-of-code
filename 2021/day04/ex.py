class Bingoboard:

    def __init__(self, board: list[list]):
        self.BOARD = board.copy()
        self.BOARD_TRANSPOSED = list(map(list, zip(*self.BOARD)))
        self.DICT_MARKED = self.__create_board_dict()

    def __create_board_dict(self) -> dict:
        return {number: False for number in [number for row in self.BOARD for number in row]}

    def mark_and_check(self, number: int) -> bool:
        self.__mark_number(number)
        return self.__check_bingo()

    def __mark_number(self, number: int):
        self.DICT_MARKED[number] = True

    def __check_bingo(self) -> bool:
        return self.__check_board_for_bingo(self.BOARD) or self.__check_board_for_bingo(self.BOARD_TRANSPOSED)

    def __check_board_for_bingo(self, board: list[list]) -> bool:
        return any([sum([self.DICT_MARKED[number] for number in row]) == len(row) for row in board])

    def count_board_sum(self):
        return sum([number if self.DICT_MARKED[number] is False else 0 for row in self.BOARD for number in row])


class BingoBoardMaster:

    def __init__(self, file: str):
        self.BOARDS: list[Bingoboard] = []
        self.__create_bingo_boards_from_text(file)

    def __create_bingo_boards_from_text(self, file: str):
        with open(file, 'r') as f:
            data = f.read().splitlines()
        indeces_empty_lines = [i for i, val in enumerate(data) if val == '']
        for index in indeces_empty_lines:
            rows = data[index + 1:index + 6]
            board = self.__convert_text_rows_to_board(rows)
            self.BOARDS.append(board)

    @staticmethod
    def __convert_text_rows_to_board(rows_text: list) -> Bingoboard:
        converted_rows = []
        for row in rows_text:
            row = row.split(' ')
            row = list(filter(None, row))
            row = list(map(int, row))
            converted_rows.append(row)
        return Bingoboard(converted_rows)


class BingoSequencer:

    def __init__(self, file: str):
        self.SEQUENCE: list[int] = []
        self.__get_bingo_sequence_from_text(file)

    def __get_bingo_sequence_from_text(self, file: str):
        with open(file, 'r') as f:
            data = f.read().splitlines()
        sequence_str = data[0].split(',')
        self.SEQUENCE = list(map(int, sequence_str))


if __name__ == "__main__":
    master = BingoBoardMaster('input.txt')
    sequencer = BingoSequencer('input.txt')

    for n in sequencer.SEQUENCE:
        for b in master.BOARDS.copy():
            if b.mark_and_check(n):
                if len(master.BOARDS) == 100:
                    print('FIRST WIN: %s' % (n * b.count_board_sum()))
                if len(master.BOARDS) == 1:
                    print('LAST WIN: %s' % (n * b.count_board_sum()))
                master.BOARDS.remove(b)
