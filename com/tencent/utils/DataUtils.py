import json

from com.tencent.utils.ExcelUtils import ExcelUtils
from com.tencent.utils.VarUtils import Var


class DataUtils:
    def __init__(self, file="../data/case1.xls"):
        self.file = file
        # 需要创建excelutils
        self.excelUtils = ExcelUtils(file=file)

    # 根据行获取对应的用例
    def getCaseNo(self, row):
        return self.excelUtils.getCellValue(row, Var.REQUEST_ID)

    # 获取用例名称
    def getCaseName(self, row):
        return self.excelUtils.getCellValue(row, Var.REQUEST_NAME)

    # 获取用例URL 参数是行
    def getCaseURL(self, row):
        return self.excelUtils.getCellValue(row, Var.REQUEST_URL)

    # 获取请求方法
    def getCaseMethod(self, row):
        return self.excelUtils.getCellValue(row, Var.REQUEST_METHOD)

    # 获取请求参数
    def getCaseParams(self, row):
        str = self.excelUtils.getCellValue(row, Var.REQUEST_PARAMS)
        try:
            # 将字符串转换成json
            return json.loads(str)
        except Exception as e:
            return {}
            # 获取请求头信息

    # 获取请求头
    def getCaseHeaders(self, row):
        try:
            str = self.excelUtils.getCellValue(row, Var.REQUEST_HEADERS)
            # 将字符串转换成字典类型
            return json.loads(str)
        except Exception as e:
            return {}

    # 获取用例是否有依赖参数是行
    def getCaseDependentNo(self, row):
        return self.excelUtils.getCellValue(row, Var.REQUEST_DEPENDENT_NO)

    # 获取依赖的字段
    def getCaseDependentField(self, row):
        return self.excelUtils.getCellValue(row, Var.REQUEST_DEPENDENT_FIELD)

    # 获取当前接口依赖的参数名称
    def getDependentParams(self, row):
        return self.excelUtils.getCellValue(row, Var.REQUEST_DEPENDENT_PARAMS)

    # 获取预期结果
    def getExpectResult(self, row):
        try:
            str = self.excelUtils.getCellValue(row, Var.REQUEST_EXPECT_RESULT)
            # 将字符串转换成字典类型
            return json.loads(str)
        except Exception as e:
            return None

            # 获取实际结果

    def getActualResult(self, row):
        try:
            str = self.excelUtils.getCellValue(row, Var.REQUEST_ACTUAL_RESULT)
            # 将字符串转换成字典类型
            return json.loads(str)
        except Exception as e:
            return None

    # 设置实际结果--如果外界获取到的实际结果是json类型-转换成字符串类型
    def writeActualResult(self, row, data):
        try:
            str = json.dumps(data, ensure_ascii=False, indent=4)
            self.excelUtils.writeCellValue(row, Var.REQUEST_ACTUAL_RESULT, str)
        except Exception as e:
            self.excelUtils.writeCellValue(row, Var.REQUEST_ACTUAL_RESULT, "")

    # 写出是否通过
    def writeIsPassed(self, row, flag):
        if flag:
            self.excelUtils.writeCellValue(row, Var.REQUEST_IS_PASSED, "是")
        else:
            self.excelUtils.writeCellValue(row, Var.REQUEST_IS_PASSED, "否")

    # 获取用例个数
    def getCaseCount(self):
        return self.excelUtils.getCaseCount()

    # 获取用例完整信息
    def getCaseInfo(self, row):
        # 定义一个用例
        case = {}
        case["no"] = self.getCaseNo(row)
        case["name"] = self.getCaseName(row)
        case["url"] = self.getCaseURL(row)
        case["method"] = self.getCaseMethod(row)
        case["params"] = self.getCaseParams(row)
        case["headers"] = self.getCaseHeaders(row)
        case["expect_result"] = self.getExpectResult(row)
        case["actual_result"]=self.getActualResult(row)
        # 获取接口依赖
        case["dept_no"] = self.getCaseDependentNo(row)
        # 存在接口依赖,取出依赖字段
        case["dept_field"] = self.getCaseDependentField(row)
        case["dept_params"] = self.getDependentParams(row)
        return case


if __name__ == '__main__':
    dataUtils = DataUtils()
    print(dataUtils.getCaseMethod(2))
    dataUtils.writeIsPassed(1, False)
    dataUtils.writeActualResult(1, "xxxxx")
    print(dataUtils.getCaseInfo(1))
