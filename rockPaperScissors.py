from random import randint


def play_game():
    rand_num = randint(0, 2)
    players_score = 0
    computers_score = 0
    winning_score = 5

    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'
    while players_score < winning_score and computers_score < winning_score:
        print(f'Players score: {players_score}  Computers score: {computers_score}')
        player = input('Rock, Paper or Scissors? \n').lower()
        print(f'Computer plays {computer}')
        if player == 'quit' or player == 'q':
            break
        if player == computer:
            print(f'It\'s a tie')
        elif player == 'rock':
            if computer == 'paper':
                print('Computer wins')
                computers_score += 1
            else:
                print('You win')
                players_score += 1
        elif player == 'paper':
            if computer == 'rock':
                print('You win')
                players_score += 1
            else:
                print('Computer wins')
                computers_score += 1
        elif player == 'scissors':
            if computer == 'rock':
                print('Computer wins')
                computers_score += 1
            else:
                print('You win')
                players_score += 1
        else:
            print('Enter a valid input!')
    if players_score > computers_score:
        print(f'YOU WON!!!')
    elif players_score == computers_score:
        print(f'It is a tie')
    else:
        print(f'The computer won.')
    print(f"FINAL SCORES... Player Score: {players_score}  Computer Score: {computers_score}")


play_game()
play_again = input('Do you want to play again?  Y/N ').upper()
if play_again == 'N':
    print('Game Over')
else:
    play_game()