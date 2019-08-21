# 公共
import os

from jsonpath_rw import parse

from com.tencent.utils.DataUtils import DataUtils
from com.tencent.utils.RequestUtils import RequestUtils
from com.tencent.utils.reportutils import ReportUtils


class CommonUtils:
    def __init__(self):
        self.caseList = []

    # 获取所有的用例文件
    def getCaseFile(self, dir="../data"):
        list = os.listdir(path=dir)
        mList = []
        for file in list:
            if file.endswith(".xls") or file.endswith(".xlsx"):
                mList.append(dir + "/" + file)
        return mList

    # 执行单个用例文件：
    def executeSingleCaseFile(self, file):
        dataUtils = DataUtils(file)
        requestUtils = RequestUtils()
        # 获取用例的个数
        count = dataUtils.getCaseCount()
        for row in range(1, count):
            # 获取用例信息
            case = dataUtils.getCaseInfo(row)
            # 判断当前case是否有依赖
            if case["dept_no"] != None and case["dept_no"] != "":
                dept_no = int(case["dept_no"])
                # 根据dept_no获取所依赖接口的实际结果
                dept_case = dataUtils.getCaseInfo(dept_no)
                # 获取所依赖case的实际结果
                actual_result = dept_case["actual_result"]
                # 根据匹配规则，提取出参数来..
                regex = case["dept_field"]
                dept_params_value = self.getDeptParmas(actual_result, regex)
                # 获取依赖的参数名称
                dept_params = case["dept_params"]
                case["params"][dept_params] = dept_params_value
                print(case["params"])
            # 执行请求
            actual_result = requestUtils.doRequest(url=case["url"], method=case["method"], params=case["params"],
                                                   headers=case["headers"])
            expect_result = case["expect_result"]
            # 和预期结果进行比较
            is_passed = self.compareResult(actual_result, expect_result)
            # 设置实际结果，设置是否通过
            dataUtils.writeActualResult(row, actual_result)
            dataUtils.writeIsPassed(row, is_passed)
            # 往集合中添加用例信息  声明用例是否通过
            case["is_pass"] = is_passed
            self.caseList.append(case)

    # warn 警告 error 错误
    # 执行所有的用例文件  dir 用例所在的文件夹
    def executeAllCaseFile(self, dir):
        fileList = self.getCaseFile(dir)
        for file in fileList:
            self.executeSingleCaseFile(file)

    # 比较结果
    def compareResult(self, actual_result, expect_result):
        if actual_result != None and actual_result != {} and expect_result != None and expect_result != {}:
            # 比较什么东西...自动化，共性的东西..status msg
            if actual_result["status"] == expect_result["status"] and actual_result["msg"] == expect_result["msg"]:
                # 认为通过
                return True
                # 设置实际结果，设置是否通过
            else:
                return False
        else:
            return False

    # 声明函数，导出报告
    def export_report(self):
        reportUtils = ReportUtils()
        reportUtils.export_report(self.caseList)

    # 根据规则，到字典中提取参数
    def getDeptParmas(self, dict, regex):
        json_exe = parse(regex)
        result = json_exe.find(dict)
        params = [match.value for match in result][0]
        return params


if __name__ == '__main__':
    commonUtils = CommonUtils()
    print(commonUtils.getCaseFile())
    # commonUtils.executeSingleCaseFile("../data/case1.xls")
    commonUtils.executeAllCaseFile("../data")
    commonUtils.export_report()
