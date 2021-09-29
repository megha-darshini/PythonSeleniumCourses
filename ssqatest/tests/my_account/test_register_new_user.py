import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password

#pytest -m tcid13 -s --pdb --html=results/my_report.html --self-contained-html

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):

        my_account_o = MyAccountSignedOut(self.driver)
        my_account_o.go_to_my_account()

        rand_email = generate_random_email_and_password()
        my_account_o.input_register_email(rand_email['email'])
        my_account_o.input_register_password('seleniumpytest@12345')
        my_account_o.click_register_btn()

        my_account_in = MyAccountSignedIn(self.driver)
        my_account_in.verify_user_signed_in()