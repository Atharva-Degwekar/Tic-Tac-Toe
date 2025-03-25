def printboard(xstate, ostate):
    zero = "X" if xstate[0]==1 else "O" if ostate[0]==1 else " "
    one = "X" if xstate[1]==1 else "O" if ostate[1]==1 else " "
    two = "X" if xstate[2]==1 else "O" if ostate[2]==1 else " "
    three = "X" if xstate[3]==1 else "O" if ostate[3]==1 else " "
    four = "X" if xstate[4]==1 else "O" if ostate[4]==1 else " "
    five = "X" if xstate[5]==1 else "O" if ostate[5]==1 else " "
    six = "X" if xstate[6]==1 else "O" if ostate[6]==1 else " "
    seven = "X" if xstate[7]==1 else "O" if ostate[7]==1 else " "
    eight = "X" if xstate[8]==1 else "O" if ostate[8]==1 else " "

    print(f"   |   |   |   |")
    print(f"---|---|---|---|---")
    print(f"   | {zero} | {one} | {two} |")
    print(f"---|---|---|---|---")
    print(f"   | {three} | {four} | {five} |")
    print(f"---|---|---|---|---")
    print(f"   | {six} | {seven} | {eight} |")
    print(f"---|---|---|---|---")
    print(f"   |   |   |   |")

def sum(a, b, c):
    return a + b + c

def checkwin(xstate, ostate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("Player 1 wins")
            return 1

        elif sum(ostate[win[0]], ostate[win[1]], ostate[win[2]]) == 3:
            print("Player 2 wins")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    ostate = [0,0,0,0,0,0,0,0,0]

    # 1 for X and 0 for O
    turn = 1
    print("Welcome to Tic Tac Toe")
    print("Player 1 is X and Player 2 is O")
    print("Player 1 will go first")

    while True:
        if turn == 1:
            print("Player 1's turn")
            value = int(input("Enter the value: "))
            xstate[value] = 1

        else:
            print("Player 2's turn")
            value = int(input("Enter the value: "))
            ostate[value] = 1

        cwin = checkwin(xstate, ostate)
        if cwin != -1:
            printboard(xstate, ostate)
            break
        turn = 1 - turn