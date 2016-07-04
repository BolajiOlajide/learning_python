import random


class Number:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def random_number(self):
        return random.randint(self.start, self.stop)


class Message:
    def __init__(self):
        pass

    @staticmethod
    def intro(start, stop):
        print('I am thinking of a number between %i and %i, can you guess what that number is?' % (start, stop))
        print("-" * 77)

    @staticmethod
    def win(computer_number, times):
        print('You are a genius, you guessed my number it was %i!' % computer_number)
        print('Number of guess(es): %i' % times + 1)
        print("-" * 37)

    @staticmethod
    def try_again(computer_number, chances):
        print("Sorry but the number was %i!" % computer_number)
        print("You have a total of %i guess(es) left" % chances)
        print("-" * 37)

    @staticmethod
    def game_over(count, computer_number):
        print("Game ended with a total guess(es) of %i" % count)
        print("The number was %i!" % computer_number)
        print("-" * 37)


class BeginnersGuessIt:
    count = 0

    def __init__(self):
        self.start = 1
        self.stop = 10
        self.chances = 10
        self.number_range = Number(self.start, self.stop)

    def start_game(self):
        computer_number = self.number_range.random_number()
        Message.intro(self.start, self.stop)
        your_guess = input('Take a guess: ')

        if your_guess == quit:
            Message.game_over(self.count, computer_number)
            return
    
        if your_guess == computer_number:
            self.count = 1
            Message.win(computer_number, self.count)
            return

        while your_guess != computer_number:
            self.count += 1
            self.chances -= 1

            if self.chances == 0 or your_guess == quit:
                Message.game_over(self.count, computer_number)
                return

            Message.try_again(computer_number, self.chances)
            computer_number = self.number_range.random_number()
            your_guess = input('Take a guess: ')

            if your_guess == computer_number:
                Message.win(computer_number, self.count)
                return


class AdvanceGuessIt(BeginnersGuessIt):
    def __init__(self):
        self.start = 1
        self.stop = 50
        self.chances = 15
        self.number_range = Number(self.start, self.stop)


class ProGuessIt(BeginnersGuessIt):
    def __init__(self):
        self.start = 1
        self.stop = 100
        self.chances = 20
        self.number_range = Number(self.start, self.stop)

#BeginnersGuessIt().start_game()

#AdvanceGuessIt().start_game()

#ProGuessIt().start_game()

