import argparse
import random
from signal import signal, SIGINT

from src.enums import Interval, Note
from src.engine import IntervalCalculator


class ColorText:
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END_COLOR = '\033[0m'

    @classmethod
    def blue(cls, msg: str) -> str:
        return f'{cls.BLUE}{msg}{cls.END_COLOR}'

    @classmethod
    def yellow(cls, msg: str) -> str:
        return f'{cls.YELLOW}{msg}{cls.END_COLOR}'

    @classmethod
    def green(cls, msg: str) -> str:
        return f'{cls.GREEN}{msg}{cls.END_COLOR}'

    @classmethod
    def red(cls, msg: str) -> str:
        return f'{cls.RED}{msg}{cls.END_COLOR}'


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='A CLI trainer to practice interval building',
    )
    parser.add_argument(
        '-a',
        '--auto-answer',
        action='store_true',
        help=(
            'Show the correct answer regardless of the given input. '
            'Press "Enter" to reveal the answer'
        ),
    )

    return parser.parse_args()


def prompt_answer() -> Note:
    while True:
        try:
            guess = input().strip().replace('3', '#')
            guessed_note = Note.from_name(guess)
            return guessed_note
        except ValueError:
            print('Invalid note name. Please try again: ', end='')


def main() -> None:
    args = parse_arguments()
    calc = IntervalCalculator()

    directions = [
        ('above', ColorText.yellow('ascending'), calc.add_interval_above),
        ('below', ColorText.blue('descending'), calc.subtract_interval_below),
    ]

    next_note = random.choice(tuple(Note))
    while True:
        interval = random.choice(tuple(Interval))
        note = next_note
        direction, clarification, answer_func = random.choice(directions)

        print(f'Which note is a {interval.full_name} {direction} {note.display_name}? ({clarification}) ', end='')
        actual_note: Note = answer_func(note, interval)

        if args.auto_answer:
            input()
            print(f'The correct answer is: {actual_note.display_name}')
        else:
            guessed_note = prompt_answer()
            if guessed_note == actual_note:
                print(ColorText.green('Correct!'))
            else:
                print(f'{ColorText.red("Incorrect.")} The correct answer is: {actual_note.display_name}')

        next_note = actual_note


if __name__ == '__main__':
    signal(SIGINT, lambda *args, **kwargs: exit())

    try:
        main()
    except EOFError:
        # Ctrl + D has been pressed
        exit()
