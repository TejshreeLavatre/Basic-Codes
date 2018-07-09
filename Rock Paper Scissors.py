#Basic game of Rock, Paper, Scissors using elif statements

P1 = input("Player 1, plays. rock, paper or scissors? : ")
P2 = input("Player 2, plays. rock, paper or scissors? : ")

if P1 == P2:
    print("That's a tie!")
elif P1 == 'rock' and P2 == 'scissors':
    print("P1 wins")
elif P1 == 'scissors' and P2 == 'paper':
    print("P1 wins")
elif P1 == 'paper' and P2 == 'rock':
    print("P1 wins")
elif P1 == 'scissors' and P2 == 'rock':
    print("P2 wins")
elif P1 == 'paper' and P2 == 'scissors':
    print("P2 wins")
elif P1 == 'rock' and P2 == 'paper':
    print("P2 wins")
