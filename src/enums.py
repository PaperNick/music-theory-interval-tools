from enum import auto, Enum
from typing import List


class Interval(Enum):
    """
    This enum describes the interval name
    and the number of half steps it contains
    """
    MINOR_2ND = (1, 'm2', 'minor 2nd')
    MAJOR_2ND = (2, 'M2', 'major 2nd')
    MINOR_3RD = (3, 'm3', 'minor 3rd')
    MAJOR_3RD = (4, 'M3', 'major 3rd')
    PERFECT_4TH = (5, 'P4', '4th')
    TRITONE = (6, 'TT', 'tritone')
    PERFECT_5TH = (7, 'P5', '5th')
    MINOR_6TH = (8, 'm6', 'minor 6th')
    MAJOR_6TH = (9, 'M6', 'major 6th')
    MINOR_7TH = (10, 'm7', 'minor 7th')
    MAJOR_7TH = (11, 'M7', 'major 7th')
    OCTAVE = (12, 'P8', 'octave')

    def __init__(self, half_steps: int, short_name: str, full_name: str):
        self.half_steps = half_steps
        self.short_name = short_name
        self.full_name = full_name

    def is_minor(self) -> bool:
        return self in (
            self.MINOR_2ND,
            self.MINOR_3RD,
            self.MINOR_6TH,
            self.MINOR_7TH,
        )

    def is_perfect(self) -> bool:
        return self in (
            self.PERFECT_4TH,
            self.PERFECT_5TH,
            self.OCTAVE,
        )

    @classmethod
    def from_half_steps(cls, half_steps: int) -> 'Interval':
        for interval in Interval:
            if interval.half_steps == half_steps:
                return interval

        raise ValueError(f'Interval with {half_steps} is not valid.')


class Note(Enum):
    """
    In music, two note names can represent the same pitch.
    This concept cannot be described using python enums, since enums have unique values.
    To work-around this issue, we create a tuple with 2 values.
    We only care about the second value which represents the actual note number.
    """
    C = (auto(), 1)
    C_SHARP = (auto(), 2)
    D_FLAT = (auto(), 2)
    D = (auto(), 3)
    D_SHARP = (auto(), 4)
    E_FLAT = (auto(), 4)
    E = (auto(), 5)
    F = (auto(), 6)
    F_SHARP = (auto(), 7)
    G_FLAT = (auto(), 7)
    G = (auto(), 8)
    G_SHARP = (auto(), 9)
    A_FLAT = (auto(), 9)
    A = (auto(), 10)
    A_SHARP = (auto(), 11)
    B_FLAT = (auto(), 11)
    B = (auto(), 12)

    def __init__(self, _, number) -> None:
        self.display_name = self.name.replace('_SHARP', '#').replace('_FLAT', 'b')
        self.number = number

    def is_sharp(self) -> bool:
        return '#' in self.display_name

    def is_flat(self) -> bool:
        return 'b' in self.display_name

    @classmethod
    def from_name(cls, note_name: str) -> 'Note':
        note_name = note_name.capitalize()
        for note in Note:
            if note_name == note.display_name:
                return note

        raise ValueError(f'Cannot find note with name: {note_name}')

    @classmethod
    def from_number(cls, note_number: int) -> List['Note']:
        """
        If a "note_number" resolves to 2 note names,
        it will always return them in this order:
        [G#, Ab], [D#, Eb], etc...
        """
        return [note for note in Note if note.number == note_number]
