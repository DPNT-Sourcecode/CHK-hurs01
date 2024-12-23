from lib.solutions.CHK.checkout_solution import checkout


class TestChk():
    def test_chk(self):
        assert checkout("ABCD") == 115
    def test_chk_offers(self):
        assert checkout("AAA") == 130
        assert checkout("AAAAA") == 200
        assert checkout("AAAAAAA") == 300
        assert checkout("BB") == 45
        assert checkout("EEB") == 80
        assert checkout("FFF") == 20
        assert checkout("XYZ") == 45
    def test_chk_offers_multi(self):
        assert checkout("EEBB") == 110
        assert checkout("RRRQQQ") == 210
        assert checkout("XXXZZ") == 79
    def test_chk_invalid(self):
        assert checkout("@") == -1