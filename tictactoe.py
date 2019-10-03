print("Tic Tac Toe")
player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
board = []
for num in range(3):
	board.append(["[ ]"] *3)
def print_board(board):
	for row in board:
		print (" ".join(row))
victory = "none"
print_board(board)
p1r = 0
p1c = 0
p2r = 0
p2c = 0
while victory != "one win" and victory != "tie" and victory != "two win":

#Player one moves
	while (p1r > 3 or p1c > 3) or (p1r < 1 or p1c < 1)  or board[p1r - 1][p1c - 1] != "[ ]":
		p1r = eval(input("%s, please select the row of your move. " % (player1)))
		p1c = eval(input("%s, please select the column of your move. " % (player1)))
		
	else:
		board[p1r - 1][p1c - 1] = "[x]"
		print_board(board)
		
	if (board[0][0] == "[x]" and board[0][1] == "[x]" and board[0][2] == "[x]") or (board[1][0] == '[x]' and board[1][1] == '[x]' and board[1][2] == '[x]') or (board[2][0] == '[x]' and board[2][1] == '[x]' and board[2][2] == '[x]') or (board[0][0] == '[x]' and board[1][0] == '[x]' and board[2][0] == '[x]') or (board[0][1] == '[x]' and board[1][1] == '[x]' and board[2][1] == '[x]') or (board[0][2] == '[x]' and board[1][2] == '[x]' and board[2][2] == '[x]') or (board[0][0] == '[x]' and board[1][1] == '[x]' and board[2][2] == '[x]') or (board[0][2] == '[x]' and board[1][1] == '[x]' and board[2][0] == '[x]'):
		victory = "one win"
		break 
	elif board[0][0] != '[ ]' and board[0][1] != '[ ]' and board[0][2] != '[ ]' and board[1][0] != '[ ]' and board[1][1] != '[ ]' and board[1][2] != '[ ]' and board[2][0] != '[ ]' and board[2][1] != '[ ]' and board[2][2] != '[ ]':
		victory = "tie"
		break 
#Player 2 moves
	while (p2r > 3 or p2c > 3) or (p2r < 1 or p2c < 1)  or board[p2r - 1][p2c - 1] != "[ ]":
		p2r = eval(input("%s, please select the row of your move. " % (player2)))
		p2c = eval(input("%s, please select the column of your move. " % (player2)))
		
	else:
		board[p2r - 1][p2c - 1] = "[o]"
		print_board(board)

	
	if (board[0][0] == "[o]" and board[0][1] == "[o]" and board[0][2] == "[o]") or (board[1][0] == '[o]' and board[1][1] == '[o]' and board[1][2] == '[o]') or (board[2][0] == '[o]' and board[2][1] == '[o]' and board[2][2] == '[o]') or (board[0][0] == '[o]' and board[1][0] == '[o]' and board[2][0] == '[o]') or (board[0][1] == '[o]' and board[1][1] == '[o]' and board[2][1] == '[o]') or (board[0][2] == '[o]' and board[1][2] == '[o]' and board[2][2] == '[o]') or (board[0][0] == '[o]' and board[1][1] == '[o]' and board[2][2] == '[o]') or (board[0][2] == '[o]' and board[1][1] == '[o]' and board[2][0] == '[o]'):
		victory = "two win"
		break





#end states
if victory == "one win":
	print("Congratulations %s, you have cleverly outsmarted and outplayed %s. You win!" % (player1, player2))
	print(""" 
	          ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `=======` 
""")
elif victory == "two win":
	print("Congratulations are in order %s, you have triumphed over %s. You are clearly more intelligent and skilled than %s. You win!" % (player2, player1, player1))
	print("""
    	        .-=========-.
              \\'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\\
              
""")
elif victory == "tie":
	print("It's a tie! Neither %s nor %s could prove their superiority." % (player1, player2))


	
	

