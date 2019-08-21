import unittest

from jsonpath_rw import parse

from com.tencent.utils import log
from com.tencent.utils.CommonUtils import CommonUtils


class TestCase_1906A(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAllFile(self):
        log.logger().info("===开始执行所有的用例文件===")
        commonUtils = CommonUtils()
        commonUtils.executeAllCaseFile("../data")
        commonUtils.export_report()

    # def testSingleFile(self):
    #     commonUtils = CommonUtils()
    #     commonUtils.executeSingleCaseFile("../data/case2.xls")
    #     commonUtils.export_report()


    def testJsonParse(self):
        dict = {
            "status": 200,
            "msg": "success",
            "data": {
                "code": "snMN"
            }
        }
        # 获取status的规则
        regex1 = "data.code"
        json_exe = parse(regex1)
        result = json_exe.find(dict)
        #抄过来，获取匹配中的第0个
        params = [match.value for match in result][0]
        print(params)


if __name__ == '__main__':
    unittest.main()
