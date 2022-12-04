import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_pass(self):
        assert self.calc.multiply(self, 4, 5) == 20

    def test_multiply_division_pass(self):
        assert self.calc.division(self, 20, 5) == 4

    def test_multiply_subtraction_pass(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_multiply_adding_pass(self):
        assert self.calc.adding(self, 5, 5) == 10