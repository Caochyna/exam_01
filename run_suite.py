import unittest
from tools.HTMLTestRunner import HTMLTestRunner
import time

import app
from case.TestLogin import TestLogin
from case.TestEmp import TestEmp

suite = unittest.TestSuite()
suite.addTest(TestLogin("test_login_success"))
suite.addTest(TestEmp("emp_add"))
suite.addTest(TestEmp("emp_search"))
suite.addTest(TestEmp("emp_update"))
suite.addTest(TestEmp("emp_delete"))

report_path = app.PRO_PATH + "/report/report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_path, "wb") as f:
    runner = HTMLTestRunner(f, title="人力资源测试报告", description="这是一份人力资源增删查改测试报告")
    # runner = unittest.TextTestRunner()
    runner.run(suite)
