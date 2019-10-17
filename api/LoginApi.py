import app


class LoginApi(object):
    def login(self, session, mobile, password):
        loginData = {"mobile": mobile, "password": password}
        return session.post(app.BASE_URL + "login", json=loginData)
