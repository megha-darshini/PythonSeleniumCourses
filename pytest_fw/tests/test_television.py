from pytest import mark

@mark.skip
@mark.parametrize('tv_brand',[
    ('Samsung'),
    ('Sony'),
    ('LG')
])
def test_television_tunrs_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.skip
def test_television_tunrs_on_1(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.skip
def test_browser_navigate_training_ground(browser):
    browser.get('http://techstepacademy.com/traning-ground')