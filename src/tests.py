from unittest import TestCase

from src.engine import IntervalCalculator
from src.enums import Interval, Note


class TestIntervalCalculatorBuildingAbove(TestCase):
    def test_5th_above_d_should_equal_a(self):
        calc = IntervalCalculator()
        note = calc.add_interval_above(Note.D, Interval.PERFECT_5TH)
        self.assertEqual(note, Note.A)

    def test_minor_6th_above_g_should_equal_e_flat(self):
        calc = IntervalCalculator()
        note = calc.add_interval_above(Note.G, Interval.MINOR_6TH)
        self.assertEqual(note, Note.E_FLAT)

    def test_minor_7th_above_e_flat_should_equal_d_flat(self):
        calc = IntervalCalculator()
        note = calc.add_interval_above(Note.E_FLAT, Interval.MINOR_7TH)
        self.assertEqual(note, Note.D_FLAT)

    def test_major_3rd_above_b_flat_should_equal_d(self):
        calc = IntervalCalculator()
        note = calc.add_interval_above(Note.B_FLAT, Interval.MAJOR_3RD)
        self.assertEqual(note, Note.D)


class TestIntervalCalculatorBuildingBelow(TestCase):
    def test_major_3rd_below_c_should_equal_a_flat(self):
        calc = IntervalCalculator()
        note = calc.subtract_interval_below(Note.C, Interval.MAJOR_3RD)
        self.assertEqual(note, Note.A_FLAT)

    def test_minor_6th_below_a_should_equal_c_sharp(self):
        calc = IntervalCalculator()
        note = calc.subtract_interval_below(Note.A, Interval.MINOR_6TH)
        self.assertEqual(note, Note.C_SHARP)

    def test_tritone_below_g_flat_should_equal_d(self):
        calc = IntervalCalculator()
        note = calc.subtract_interval_below(Note.A_FLAT, Interval.TRITONE)
        self.assertEqual(note, Note.D)

    def test_major_7th_below_d_should_equal_c_sharp(self):
        calc = IntervalCalculator()
        note = calc.subtract_interval_below(Note.D, Interval.MAJOR_7TH)
        self.assertEqual(note, Note.E_FLAT)


class TestIntervalCalculatorFindingIntervalAscending(TestCase):
    def test_f_sharp_up_to_c_sharp_should_equal_perfect_4th(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_ascending(Note.C_SHARP, Note.F_SHARP)
        self.assertEqual(interval, Interval.PERFECT_4TH)

    def test_c_sharp_up_to_f_sharp_should_equal_perfect_5th(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_ascending(Note.F_SHARP, Note.C_SHARP)
        self.assertEqual(interval, Interval.PERFECT_5TH)

    def test_d_up_to_b_should_equal_major_6th(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_ascending(Note.D, Note.B)
        self.assertEqual(interval, Interval.MAJOR_6TH)

    def test_g_flat_up_to_c_should_equal_tritone(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_ascending(Note.G_FLAT, Note.C)
        self.assertEqual(interval, Interval.TRITONE)


class TestIntervalCalculatorFindingIntervalDescending(TestCase):
    def test_b_flat_down_to_g_should_equal_minor_3rd(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_descending(Note.B_FLAT, Note.G)
        self.assertEqual(interval, Interval.MINOR_3RD)

    def test_f_down_to_d_flat_should_equal_major_3rd(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_descending(Note.F, Note.D_FLAT)
        self.assertEqual(interval, Interval.MAJOR_3RD)

    def test_d_down_to_a_flat_should_equal_tritone(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_descending(Note.D, Note.A_FLAT)
        self.assertEqual(interval, Interval.TRITONE)

    def test_f_sharp_down_to_b_flat_should_equal_minor_6th(self):
        calc = IntervalCalculator()
        interval = calc.find_interval_descending(Note.F_SHARP, Note.B_FLAT)
        self.assertEqual(interval, Interval.MINOR_6TH)
