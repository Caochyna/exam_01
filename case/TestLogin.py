import unittest

import requests
import json

from parameterized import parameterized

import app
from api.LoginApi import LoginApi


def read_json():
    result = []
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        for value in json.load(f).values():
            username = value.get("username")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            ele = (username, password, success, code, message)
            result.append(ele)
    return result


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.session = requests.Session()
        self.loginApi = LoginApi()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(read_json())
    def test_login(self, username, password, success, code, message):
        print("-" * 100)
        print(
            "username={},password={},success={},code={},message={}".format(username, password, success, code, message))
        # 请求业务
        response = self.loginApi.login(self.session, username, password)
        print(response.json())
        # 断言
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

    def test_login_success(self):
        print("-" * 100)
        # 请求业务
        response = self.loginApi.login(self.session, "13800000002", "123456")
        print(response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        token = response.json().get("data")
        app.TOKEN = token


if __name__ == '__main__':
    unittest.main()
