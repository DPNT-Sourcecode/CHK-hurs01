from lib.solutions.CHK.checkout_solution import checkout


class TestChk():
    def test_chk(self):
        assert checkout("ABCD") == 115
    def test_chk_offers(self):
        assert checkout("AAA") == 130
        assert checkout("BB") == 45
