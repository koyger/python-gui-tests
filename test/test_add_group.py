import datetime

def test_add_group(app):
    old_list = app.groups.get_group_list()
    group_to_add = "New group "+str(datetime.datetime.now().strftime("%m_%d_%H:%M:%S"))
    app.groups.add_new_group(group_to_add)
    new_list = app.groups.get_group_list()
    old_list.append(group_to_add)
    assert sorted(old_list) == sorted(new_list)