from lib.solutions.HLO import hello_solution


class TestHlo():
    def test_hlo(self):
        assert isinstance(hello_solution.hello("abc"),str)