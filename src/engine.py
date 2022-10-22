from src.enums import Interval, Note, NoteValue


class IntervalCalculator:
    def add_interval_above(self, note: Note, interval: Interval) -> Note:
        if interval == Interval.OCTAVE:
            return note

        interval_note_num = (note.number + interval.half_steps) % 12
        if interval_note_num == 0:
            interval_note_num += 12

        interval_note: NoteValue = Note.from_number(interval_note_num)

        if interval.is_perfect():
            return interval_note.sharp_value() if note.is_sharp() else interval_note.flat_value()

        # Example: Minor 6th above C should return Ab, not G#
        # Details: Count up a 5th from C and add a half-step = C -> G -> Ab
        if interval.is_minor():
            return interval_note.flat_value()

        # Given Gb, count up a major 3rd. Should return Bb, not A#
        if note.is_flat() and interval.is_major():
            return interval_note.flat_value()

        return interval_note.value()


    def subtract_interval_below(self, note: Note, interval: Interval) -> Note:
        if interval == Interval.OCTAVE:
            return note

        interval_note_num = note.number - interval.half_steps
        if interval_note_num <= 0:
            interval_note_num += 12

        interval_note: NoteValue = Note.from_number(interval_note_num)

        if interval.is_perfect():
            return interval_note.sharp_value() if note.is_sharp() else interval_note.flat_value()

        # Example: Minor 6th below A should return C#, not Db
        # Details: Count down a 5th from A and subtract a half-step = A -> D -> C#
        if interval.is_minor():
            return interval_note.sharp_value()

        # Given A#, count down a major 3rd. Should return F#, not Gb
        if note.is_sharp() and interval.is_major():
            return interval_note.sharp_value()

        return interval_note.flat_value()

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
