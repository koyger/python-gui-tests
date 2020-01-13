import openpyxl


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, gr_to_add):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(gr_to_add)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def delete_group(self, group_to_del):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for node in root.children():
            if node.text() == group_to_del:
                node.click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.del_win = self.app.application.window(title="Delete group")
        self.del_win.window(auto_id="uxDeleteAllRadioButton").click()
        self.del_win.window(auto_id="uxOKAddressButton").click()

    def get_groups_from_excel(self, excel_path):
        list = []
        excel_file = openpyxl.load_workbook(excel_path)
        current_sheet = excel_file['Лист1']
        # 1000 is maximum reasonable size of groups list
        for n in range(1000):
            group_name = current_sheet['A%s' % (n+1)].value  # "Group %s" % (i+1)
            if group_name is None:
                break  # let's take empty line as end of names list
            list.append(group_name)
        return list
