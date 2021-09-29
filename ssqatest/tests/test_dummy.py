
import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy():
    def test_dummy_func(self):
        print("Hi im dummy test1")
        print("Hi im dummy test2")
        #self.driver.get("https://supersqa.com")
        self.driver.get("http://localhost:8888/demotestsite/")
