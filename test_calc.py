import pytest
from pythoncode.calculator import Calculator


class TestCalc():
    def setup_method(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @pytest.mark.parametrize(("a", "b", "expect"), [(1, 3, 4), (100, 101, 201), (3.9, 1.1, 5.0)],
                             ids=["int", "bigint", "float"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)
        print(f"\n{a}+{b}={expect}")


if __name__ == "__main__":
    pytest.main(["test_calc.py", "-v"])
