from lib.solutions.HLO import hello_solution


class TestHlo():
    def test_hlo_r1(self):
        assert isinstance(hello_solution.hello("abc"),str)

    def test_hlo_r2(self):
        assert hello_solution.hello("John") == "Hello, John!"