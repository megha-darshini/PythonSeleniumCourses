import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

#pytest -m tcid12 -s --pdb --html=results/my_report.html --self-contained-html

@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        #assert 1 == 2
        #return
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('abcqwe')
        my_account.input_login_password('asdsad')
        my_account.click_login_btn()

        expected_error="Error: The username abcqwe is not registered on this site. If you are unsure of your username, try your email address instead."
        my_account.wait_until_error_is_displayed(expected_error)