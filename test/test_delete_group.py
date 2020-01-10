import random


def test_delete_group(app):
    old_list = app.groups.get_group_list()
    group_to_del = random.choice(old_list)
    app.groups.delete_group(group_to_del)
    new_list = app.groups.get_group_list()
    new_list.append(group_to_del)
    assert sorted(old_list) == sorted(new_list)