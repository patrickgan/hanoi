# Towers of Hanoi

class Hanoi:
    def __init__(self, pieces=3, **kwargs):
        self.pieces = pieces
        piece_stack = [i+1 for i in range(self.pieces)]
        piece_stack.reverse()
        self.board = [piece_stack,[],[]]
        self.crane_position = 0
        self.crane_weight = 0
        self.moves = []
        # self.crane_string = '[]'
        # self.base_string = '+-+'
        
    def __repr__(self):
        crane = [[],[],[]]
        crane[self.crane_position] = [self.crane_weight]
        return str(self.board) + '; ' + str(crane)
        
    def __str__(self):
        return self.fancy_str()

    def fancy_str(self):
        def piece_string(size):
            if size > 0:
                return "  %s<%s%s%s>%s  " % (' '*(self.pieces-size),' '*(size-1), size, ' '*(size-1),' '*(self.pieces-size))
            else:
                return ' ' * (2*self.pieces+5)
        base_string = (" +%s+ " % ('-'*(2*self.pieces+1))) * 3
        crane_string = (' ' * self.pieces + '  *  ' + ' ' * self.pieces)
        space_string = ' ' * (2*self.pieces+5)
        selected_string = piece_string(self.crane_weight) if self.crane_weight else space_string
        hanoi_string = ''
        for peg in range(3):
            if peg == self.crane_position:
                hanoi_string += crane_string
            else:
                hanoi_string += space_string
        hanoi_string += '\n'  
        for peg in range(3):
            if peg == self.crane_position:
                hanoi_string += selected_string
            else:
                hanoi_string += space_string
        hanoi_string += '\n'
        for row in range(self.pieces):
            row_string = ''
            for peg in range(3):
                if len(self.board[peg]) >= self.pieces - row:
                    row_string += piece_string(self.board[peg][self.pieces - row - 1])
                else:
                    row_string += piece_string(0)
            hanoi_string += row_string + '\n'
        hanoi_string += base_string
        return hanoi_string

    def plain_str(self):
        hanoi_string = ''
        for row in self.hanoi_board():
            for column in row:
                hanoi_string += str(column)
            hanoi_string += '\n'
        return hanoi_string

    def hanoi_board(self):
        hanoi_board = [[' ' * 7] * 3]
        hanoi_board[0][self.crane_position] = '  [ ]  ' if self.crane_weight == 0 else '  [%s]  ' % self.crane_weight
        for row in range(1,self.pieces+1):
            hanoi_row = [' ' * 7] * 3
            for peg in range(0,3):
                if len(self.board[peg]) >= self.pieces+1 - row:
                    hanoi_row[peg] = '   %s   ' % self.board[peg][self.pieces - row]
            hanoi_board.append(hanoi_row)
        hanoi_board.append([' +---+ '] * 3)
        return hanoi_board
        
    def left(self):
        """ To be called when 'left' is pressed. Moves crane left.
            Does not wrap around, i.e. 0 <= crane position <= 2
        """
        if self.crane_position > 0:
            self.crane_position -= 1
        else:
            return 1
        
    def right(self):
        """ To be called when 'right' is pressed. Moves crane right.
            Does not wrap around, i.e. 0 <= crane position <= 2
        """
        if self.crane_position < 2:
            self.crane_position += 1
        else:
            return 1
        
    def pop(self):
        """ To be called when 'up' is pressed.
            Picks up the piece at crane position, if crane is empty.
        """
        if self.crane_weight == 0:
            if len(self.board[self.crane_position]) > 0:
                self.crane_weight += self.board[self.crane_position].pop()
    
    def drop(self):
        """ To be called when 'down' is pressed.
            Drops the piece at crane position, if crane is not empty,
            and if is a valid drop. (weight not greater than last element)
        """
        if self.crane_weight > 0:
            if len(self.board[self.crane_position]) == 0 or self.board[self.crane_position][-1] > self.crane_weight:
                self.board[self.crane_position].append(self.crane_weight)
                self.crane_weight = 0
                # self.moves.append("drop")
            else:
                return "Illegal move."
        else:
            self.pop() # return None
                    
    def win(self):
        piece_stack = [i for i in range(1,self.pieces+1)]
        piece_stack.reverse()
        return self.board == [[],[],piece_stack]

    def move_to(self, peg_num):
        # moves the crane from current to specified peg
        diff = peg_num - self.crane_position
        if diff >= 0:
            while diff > 0:
                self.right()
                diff -= 1
        else:
            while diff < 0:
                self.left()
                diff += 1

    def move_piece(self, src_peg, dst_peg):
        if len(self.board[dst_peg]) == 0 or self.board[dst_peg][-1] > self.board[src_peg][-1]:
            self.move_to(src_peg)
            self.pop()
            self.move_to(dst_peg)
            self.drop()

    ####
    # def undo(self):
    #     if len(self.moves) > 0:
    #         undo_action = self.moves.pop()
    #         undo_action(self)
