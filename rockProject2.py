import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        result = random.choice(moves).lower()
        return result

    def learn(self, my_move, their_move):
        pass


class RepeatPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    count = 0

    def move(self):
        if self.count == 0:
            self.count += 1
            return random.choice(moves)

        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = my_move


class CyclerPlayer(Player):  # for having the choices sequenceed
    counter = 0

    def move(self):
        self.counter += 1
        return moves[self.counter % 3]

    def learn(self, my_move, their_move):
        pass


class HumanPlayer:
    def move(self):
        answer = input("Rock, paper, scissors? ")
        while answer not in moves:
            answer = input("Invalid input.\nTry again.")

        return answer

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p2.learn(move1, move2)
        if (move1 == move2):
            print("\n\t\t***IT'S A TIE!***\n")
        elif beats(move1, move2) is True:
            print("\n\t\t***PLAYER 1 WINS!***\n")
            self.p1_score += 1
        elif beats(move2, move1) is True:
            print("\n\t\t***PLAYER 2 WINS!***\n")
            self.p2_score += 1
        print(f"Score: Player One {self.p1_score}, Player Two {self.p2_score}")

    def play_game(self):
        print("\t\t\t\t-----Game start!-----\n")
        games = input("How many rounds would you like to play? ")
        while not games.isnumeric():
            print("Invalid input!!!")
            games = input("How many rounds would you like to play? ")

        for round in range(int(games)):
            print(f"\n\t___Round {round}___\n")
            self.play_round()
        print("\t\t\t\t-----Game over!-----")

if __name__ == '__main__':

    gameChoice = ['random', 'repeat', 'reflect', 'cycle', 'end']
    print("Enter your choice for the game:\n")
    print("Enter 'random' for having a random choices in the game ")
    print("Enter 'repeat' for having repeated choices in the game")
    print("Enter 'reflect' for copying the user's answer in the next round")
    print("Enter 'cycle' for having the choices sequenced in the game")
    print("Enter 'end' for exiting the game\n")
    choice = input().lower()

    while choice not in gameChoice:
        choice = input("WRONG CHOICE!!!\nTry Again.\n")

    if choice == 'random':
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()

    elif choice == 'repeat':
        game = Game(HumanPlayer(), RepeatPlayer())
        game.play_game()

    elif choice == 'reflect':
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game()

    elif choice == 'cycle':
        game = Game(HumanPlayer(), CyclerPlayer())
        game.play_game()

    elif choice == 'end':
        exit(0)
