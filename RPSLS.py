Alice Rodriguez Cepeda
Joshua Rodriguez Santana

rounds_counter=0
# kept 'while True' because 'isPlaying = True' was not ending the program.
while True:
    rounds_counter+=1
    print('Rock Paper Scissors Lizard Spock!')
    print()
    player1 = input('Who is player 1? : ')
    print()
    player2 = input('Who is player 2? : ')
    print()
    P1Move = input(f'{player1}, make your move (R, P, S, SP, L ) : ')
    print()
    P2Move = input(f'{player1}, move (R, P, S, SP, L ) : ')
    if P1Move == 'R' and P2Move == 'P':
        print(f"{player2}'s paper beat {player1}'s rock!")
    elif P1Move == 'P' and P2Move == 'R':
        print(f"{player1}'s paper beat {player2}'s rock!")
    elif P1Move == 'S' and P2Move == 'P':
        print(f"{player1}'s scissors beat {player2}'s paper!")
    elif P1Move == 'P' and P2Move == 'S':
        print(f"{player1}'s paper was cut by {player2}'s scissors!")
    elif P1Move == 'S' and P2Move == 'R':
        print(f"{player1}'s scissors were broken by {player2}'s rock!")
    elif P1Move == 'L' and P2Move == 'P':
        print(f"{player1}'s lizard ate {player2}'s paper!")
    elif P1Move == 'L' and P2Move == 'S':
        print(f"{player1}'s lizard was decapitated by {player2}'s scissors!")
    elif P1Move == 'L' and P2Move == 'R':
        print(f"{player1}'s lizard was crushed by {player2}'s rock!")
    elif P1Move == 'L' and P2Move == 'SP':
        print(f"{player1}'s lizard poisoned {player2}'s Spock!")
    elif P1Move == 'SP' and P2Move == 'R':
        print(f"{player1}'s Spock dissolved {player2}'s Rock!")
    elif P1Move == 'SP' and P2Move == 'P':
        print(f"{player1}'s Spock was disproved by {player2}'s Paper!")
    elif P1Move == 'SP' and P2Move == 'S':
        print(f"{player1}'s Spock smashed {player2}'s Scissors!")
    elif P1Move == 'SP' and P2Move == 'L':
        print(f"{player1}'s Spock was poisoned by {player2}'s lizard!")
    elif P1Move == 'P' and P2Move == 'L':
        print(f"{player1}'s paper was eaten by {player2}'s lizard!")
    elif P1Move == 'S' and P2Move == 'L':
        print(f"{player1}'s scissors decapitated {player2}'s lizard!")
    elif P1Move == 'R' and P2Move == 'L':
        print(f"{player1}'s rock crushed {player2}'s lizard!")
    elif P1Move == 'R' and P2Move == 'S':
        print(f"{player1}'s rock broke {player1}'s scissors!")
    elif P1Move == 'R' and P2Move == 'R':
        print(f"{player1}'s rock collided with {player2}'s rock in confusion.. 🤨")
    elif P1Move == 'P' and P2Move == 'P':
        print(f"{player1}'s paper collided with{player2}'s paper in confusion.. 🤨")
    elif P1Move == 'S' and P2Move == 'S':
        print(F"{player1}'s scissors collided with {player2}'s scissors in confusion.. 🤨")
    elif P1Move == 'P' and P2Move == 'P':
        print(f"{player1}'s paper collided with {player2}'s paper in confusion.. 🤨")
    elif P1Move == 'P' and P2Move == 'P':
        print(f"{player1}'s paper collided with {player2}'s paper in confusion.. 🤨")

    exit=input('Want to play another round ? : ')
    if exit=='no':
        if rounds_counter==1:
            print(f'{player1} and {player2} played {rounds_counter} round.')
        elif rounds_counter>=2:
            print(f'{player1} and {player2} played {rounds_counter} rounds.')
        break
# End of While loop
