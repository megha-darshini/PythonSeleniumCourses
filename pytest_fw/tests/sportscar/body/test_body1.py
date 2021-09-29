from pytest import mark

@mark.smoke
@mark.body
class BodyTests:
    @mark.door
    def test_body_functions_as_expected(self):
        assert True

    def test_bumper(self):
        assert True

    def test_windsheild(self):
        assert True