#练习unittest测试框架

import unittest

class UnittestDemo(unittest.TestCase):  #继承unittest里的Testcase测试用例类
    chrom = "谷歌浏览器"  #创建了一个对象
    def setUp(self):
        print(1)
        print(self.chrom)   #调用了对象

    def tearDown(self):
        print(2)
        print(self.chrom)

    def test_url(self):
        print(3)
if __name__ == '__main__':
    unittest.main()