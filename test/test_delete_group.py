import random
import datetime


def test_delete_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) <= 1:
        group_to_add = "Additional group " + str(datetime.datetime.now().strftime("%m_%d_%H:%M:%S"))
        app.groups.add_new_group(group_to_add)
        old_list = app.groups.get_group_list()
    group_to_del = random.choice(old_list)
    app.groups.delete_group(group_to_del)
    new_list = app.groups.get_group_list()
    new_list.append(group_to_del)
    assert sorted(old_list) == sorted(new_list)