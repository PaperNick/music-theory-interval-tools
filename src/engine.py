from typing import List, Optional

from src.enums import Interval, Note


class IntervalCalculator:
    def _take_note_with_same_accidental(self, note: Note, target_note: List[Note]) -> Optional[Note]:
        """
        Given a reference note, return a target note with the same accidental.

        note - reference note used to determine which target note to return
        target_note - the result from Note.from_number() method

        Example:
        Having: note = C# and target_note = [G#, Ab]
        The method should return G#
        """
        for t_note in target_note:
            if note.is_sharp() and t_note.is_sharp():
                return t_note
            if note.is_flat() and t_note.is_flat():
                return t_note

        return target_note[0] if target_note else None


    def add_interval_above(self, note: Note, interval: Interval) -> Note:
        if interval == Interval.OCTAVE:
            return note

        interval_note_num = (note.number + interval.half_steps) % 12
        if interval_note_num == 0:
            interval_note_num += 12

        interval_note: List[Note] = Note.from_number(interval_note_num)
        if len(interval_note) == 1:
            return interval_note[0]

        if interval.is_perfect():
            return self._take_note_with_same_accidental(note, interval_note) or interval_note[0]

        # Example: Minor 6th above C should return Ab, not G#
        # Note.from_number() will always return in this order - [G#, Ab]
        # Details: Count up a 5th from C and add a half-step = C -> G -> Ab
        if interval.is_minor():
            return interval_note[1]

        return interval_note[0]


    def subtract_interval_below(self, note: Note, interval: Interval) -> Note:
        if interval == Interval.OCTAVE:
            return note

        interval_note_num = note.number - interval.half_steps
        if interval_note_num <= 0:
            interval_note_num += 12

        interval_note: List[Note] = Note.from_number(interval_note_num)
        if len(interval_note) == 1:
            return interval_note[0]

        if interval.is_perfect():
            return self._take_note_with_same_accidental(note, interval_note) or interval_note[0]

        # Example: Minor 6th below A should return C#, not Db
        # Note.from_number() will always return in this order - [C#, Db]
        # Details: Count down a 5th from A and subtract a half-step = A -> D -> C#
        if interval.is_minor():
            return interval_note[0]

        return interval_note[1]

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
