def test_add_group(app):
    old_list = app.groups.get_group_list()
    groups_from_excel = app.groups.\
        get_groups_from_excel("C:\\Users\\AleksandrKoygerov\\PycharmProjects\\python-gui-tests\\groups.xlsx")
    if len(groups_from_excel) == 0:
        print("NO GROUPS LIST, CHECK EXCEL FILE")
        assert False
    for group_to_add in groups_from_excel:
        app.groups.add_new_group(group_to_add)
        old_list.append(group_to_add)
    new_list = app.groups.get_group_list()
    assert sorted(old_list) == sorted(new_list)
