from model.group1_16 import Group


# Метод принимает в качестве параметра фикстуру.
def test_testaddgroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Name_group01", header="group_header01", footer="group_footer01"))
    app.session.logout()


# Метод принимает в качестве параметра фикстуру.
def test_testaddemptygroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
