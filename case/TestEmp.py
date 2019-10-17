import unittest

import requests

import app
from api.EmpApi import EmpApi


class TestEmp(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.empApi = EmpApi()

    def tearDown(self):
        self.session.close()

    # 增
    def emp_add(self):
        response = self.empApi.emp_add_api(self.session, "chyna101617", "138000000116","chyna001")
        print(response.json())
        #断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        id = response.json().get("data").get("id")
        app.EMP_ID = id

    # 查询
    def emp_search(self):
        response = self.empApi.emp_search_api(self.session)
        print(response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        # 修改
    def emp_update(self):
        response = self.empApi.emp_update_api(self.session,"chyna101618")
        print(response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 删除
    def emp_delete(self):
        response = self.empApi.emp_delete_api(self.session)
        print(response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

