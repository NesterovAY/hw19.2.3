import pytest

from app.calculator import Calculator

class TestCalculcator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply(self):
        assert self.calculator.multiply(self, 2, 2) == 4

    def test_adding(self):
        assert self.calculator.adding(self, 2, 2) == 4

    def test_substraction(self):
        assert self.calculator.subtraction(self, 12, 10) == 2

    def test_division(self):
        assert self.calculator.division(self, 4, 4) == 1
