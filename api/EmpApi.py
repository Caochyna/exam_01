import app


class EmpApi(object):
    # 增加员工请求业务
    def emp_add_api(self, session, username, mobile, workNumber):
        emp_data = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber
        }
        token = {"Authorization": "Bearer " + app.TOKEN}
        return session.post(app.BASE_URL + "user", json=emp_data, headers=token)

    # 修改员工请求业务
    def emp_update_api(self, session, username):
        emp_update_data = {username: username}
        token = {"Authorization": "Bearer " + app.TOKEN}
        return session.put(app.BASE_URL + "user/"  + app.EMP_ID, json=emp_update_data, headers=token)

    # 删除员工请求业务
    def emp_delete_api(self,session):
        token = {"Authorization": "Bearer " + app.TOKEN}
        return session.delete(app.BASE_URL + "user/" + app.EMP_ID, headers=token)

    # 查询员工请求业务
    def emp_search_api(self, session):
        token = {"Authorization": "Bearer " + app.TOKEN}
        return session.get(app.BASE_URL + "user/" + app.EMP_ID, headers=token)
