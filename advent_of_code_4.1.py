#!/usr/bin/python3

import sys
import itertools


def take(n, iterable):
    return list(itertools.islice(iterable, n))

class Bingo_Card():

    def __init__(self, *rows):
        self.board = rows

    def _check_column(self, column_number, called_numbers):
        column_called = 1
        for row in self.board:
           column_called &= (row[column_number] in called_numbers)
        return column_called
        
    def _check_row(self, row_number, called_numbers):
        row_called = 1
        row = self.board[row_number]
        for number in row:
            row_called &= (number in called_numbers)
        return row_called

    def _sum_unmarked_row(self, row_number, called_numbers):
        row = self.board[row_number]
        return sum([number for number in row if not number in called_numbers])

    
    def check_table_against_calls(self, called_numbers):
        any_row_called = ([self._check_row(row_number, called_numbers) for row_number in range(len(self.board))])
        any_column_called = ([self._check_column(column_number, called_numbers) for column_number in range(len(self.board[0]))])

        print(any_row_called, any_column_called)
        
        return (max(any_row_called) | max(any_column_called))

    def total_unmarked_numbers(self, called_numbers):
        return sum([self._sum_unmarked_row(row_number, called_numbers) for row_number in range(len(self.board))])

    
def find_winning_bingo_card_score(bingo_cards, numbers_called):
    number_called_check_dict = dict()
    for index, number_called in enumerate(numbers_called):
        number_called_check_dict[number_called] = index
        for bingo_card in bingo_cards:
            if bingo_card.check_table_against_calls(number_called_check_dict):
                score = bingo_card.total_unmarked_numbers(number_called_check_dict) * number_called
                return score

    
if __name__ == '__main__':

    bingo_data = (line.rstrip() for line in sys.stdin)

    numbers_called = next(bingo_data)
    numbers_called = [int(number) for number in numbers_called.split(",")]
    

    number_called_check_dict = dict()
    bingo_cards = []
    
    try:
        i = 0 
        while True:
            next(bingo_data) # throw away blank lines
            bingo_rows = take(5, bingo_data)
            bingo_rows = [[int(number) for number in row.split()] for row in bingo_rows]
            bingo_cards.append(Bingo_Card(*bingo_rows))
    except StopIteration:
        pass

    winning_card_score = find_winning_bingo_card_score(bingo_cards, numbers_called)
    print(winning_card_score)
        
    

        
        
