import ddt
import requests
import unittest

from Test123.readCsv2 import ReadCsv


@ddt.ddt
class Login(unittest.TestCase):
    testdata2 = ReadCsv("login.csv")

    def setUp(self):
        self.url = "http://localhost/index.php?m=user&c=public&a=login"

    def tearDown(self):
        print(2)
        print(self.result)

    @ddt.data(*testdata2)
    def test_Denglu(self,row):
        parameters = {"url_forward":row[0],"username":row[1],"password":row[2]}
        response = requests.post(self.url,data=parameters)
        response.encoding = response.apparent_encoding

        self.result = response.headers["Expires","Thu, 19 Nov 1981 08:52:00 GMT"]

        self.assertEqual(self.result,"Thu, 19 Nov 1981 08:52:00 GMT")


    if __name__ == '__main__':
        unittest.main()