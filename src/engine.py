from typing import List

from src.enums import Interval, Note


class IntervalCalculator:
    def add_interval_above(self, note: Note, interval: Interval) -> Note:
        if interval == Interval.OCTAVE:
            return note

        interval_note_num = (note.number + interval.half_steps) % 12
        if interval_note_num == 0:
            interval_note_num += 12

        interval_note: List[Note] = Note.from_number(interval_note_num)
        if len(interval_note) == 1:
            return interval_note[0]

        # Example: Minor 6th above C should return Ab, not G#
        # Note.from_number() will always return in this order - [G#, Ab]
        # Details: Count up a 5th from C and add a half-step = C -> G -> Ab
        return interval_note[1] if interval.is_minor_interval() else interval_note[0]


    def subtract_interval_below(self, note: Note, interval: Interval) -> Note:
        if interval == Interval.OCTAVE:
            return note

        interval_note_num = note.number - interval.half_steps
        if interval_note_num <= 0:
            interval_note_num += 12

        interval_note: List[Note] = Note.from_number(interval_note_num)
        if len(interval_note) == 1:
            return interval_note[0]

        # Example: Minor 6th below A should return C#, not Db
        # Note.from_number() will always return in this order - [C#, Db]
        # Details: Count down a 5th from A and subtract a half-step = A -> D -> C#
        return interval_note[0] if interval.is_minor_interval() else interval_note[1]

    def find_interval_ascending(self, first: Note, second: Note) -> Interval:
        second_note_num = second.number
        if second_note_num <= first.number:
            second_note_num += 12

        interval = second_note_num - first.number
        return Interval.from_half_steps(interval)

    def find_interval_descending(self, first: Note, second: Note) -> Interval:
        first_note_num = first.number
        if first_note_num <= second.number:
            first_note_num += 12

        interval = first_note_num - second.number
        return Interval.from_half_steps(interval)
