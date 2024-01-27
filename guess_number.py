from dataclasses import dataclass, field
import random

@dataclass
class NumberGuess:
    range: list[int] = field(default_factory=list)
    target: int = 0
    range_beginning: int = None
    range_end: int = None

    def set_range(self):
        while self.range_beginning is None or self.range_end is None:
            try:
                self.range_beginning = int(input('Enter the first number in the range: '))
                self.range_end = int(input('Enter the last number in the range: '))                
            except ValueError:
                print('Please enter numbers only.')
                self.range_beginning = None
                self.range_end = None

        self.range.append(self.range_beginning)
        self.range.append(self.range_end)

    def randomize(self):
        if self.range_end > self.range_beginning:
            self.target = random.randint(self.range_beginning,self.range_end)
        else:
            self.target = random.randint(self.range_end,self.range_beginning)

    def number_guess(self) -> int:
        while True:
            try:
                return int(input(f'Guess a number between {self.range_beginning} and {self.range_end}: '))
            except ValueError:
                print('Please enter numbers ony.')
            break

@dataclass
class Game:
    winner: bool = False
    num: NumberGuess = NumberGuess()

    def is_correct(self, user_guess):
        if self.num.target == user_guess:
            print(f'You guessed the correct number: {self.num.target}!')
            self.winner = True
        else:
            if user_guess > self.num.target:
                print('Your guess is too high! Guess again!')
            else:
                print('Your guess is too low! Guess again!')

    def play(self):
        self.num.set_range()
        self.num.randomize()
        while self.winner is False:
            user_guess = self.num.number_guess()
            self.is_correct(user_guess)

def main() -> None:
    game = Game()
    game.play()

if __name__ == '__main__':
    main()
