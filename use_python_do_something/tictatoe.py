#!/usr/bin/env python

def drawBoard(board):
    """drawBoard"""
    blank_board = '|     '*3 + '|'
    edge_board = '+-----'*3+'+'
    def drawLine(board_line):
        insert_sym = '|'
        print blank_board
        print "|%3s%3s%3s%3s%3s  |"%(board_line[0], insert_sym, board_line[1], insert_sym, board_line[2])
        print blank_board
        print edge_board
    print edge_board
    drawLine(board[7:10])
    drawLine(board[4:7])
    drawLine(board[1:4])

def inputPlayerLetter():
    lettor = ''
    while not (lettor == 'X' or lettor == 'O'):           
        # code...   
        print 'you want X or O?'
        lettor = raw_input().upper()
    if lettor == 'X':
        return ['X','O']
    else:
        return ['O', 'X']
def playerMove(board, lettor):
    """let the player type in his move"""
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        move=raw_input()
        try:
            if not isSpaceFree(board, int(move)):
                print 'the board has already had the stone!'
                move = ''
                continue
        except:
            print u' input now in the rule,please input valid num(1-9)'
            continue
    board[int(move)] = lettor
    return isWiner(board, lettor)

def playAgain():
    """this function returns true if the player wants to play again"""
    print 'do want to play again(yes or no)'
    return raw_input().lower().startswith('y')

def isWiner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

def isSpaceFree(board, move):
    """return true if the passed moveed"""
    return board[move] == ' ' or board[move] in '1 2 3 4 5 6 7 8 9'.split()

def isBoardFull(board):
    """return True if every space on the board"""
    for i in range(1, 10):
        if  isSpaceFree(board, i):
            return False
    return True

if __name__ == '__main__':
    print u'welcome to play Tic Tac Toe!'
    while True:
        theBoard = '0 1 2 3 4 5 6 7 8 9'.split()
        player1Letter, player2Letter = inputPlayerLetter();
        Lettor = (player1Letter, player2Letter)
        print u' ' + Lettor[0] + u'first'

        turn = 0
        gameIsPlaying = True

        while gameIsPlaying:
            drawBoard(theBoard)
            current_letter = Lettor[turn];

            print u'turn on ' + current_letter + u' go'

            if playerMove(theBoard, current_letter):
                    drawBoard(theBoard)
                    print u'wa ' + current_letter + u' win'
                    gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print u'Game over, you are all winner'
                    break
                else:
                    turn = (turn+1)%2
        if not playAgain():
            break
                    
                    


