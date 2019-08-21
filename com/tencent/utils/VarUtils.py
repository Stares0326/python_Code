class Var:
    # 用例编号
    REQUEST_ID = 0
    # 用例名称
    REQUEST_NAME = 1
    # 请求地址
    REQUEST_URL = 2
    # 请求方法
    REQUEST_METHOD = 3
    # 请求参数
    REQUEST_PARAMS = 4
    # 请求头
    REQUEST_HEADERS = 5
    # 请求依赖接口编号
    REQUEST_DEPENDENT_NO = 6
    # 请求依赖字段
    REQUEST_DEPENDENT_FIELD = 7
    # 依赖参数字段
    REQUEST_DEPENDENT_PARAMS = 8
    # 预期结果 expect
    REQUEST_EXPECT_RESULT = 9
    # 实际结果 actual
    REQUEST_ACTUAL_RESULT = 10
    # 是否通过
    REQUEST_IS_PASSED = 11