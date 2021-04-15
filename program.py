from tkinter import *
from tkinter import ttk
from gui_utilities import Empty_Error, Instance_Error, Range_Error, Confirmation_Message, Empty_Database_Error
import database_methods
from database_methods import Get_Mouse_Speed
import ctypes
import grid


class Program:

    def __init__(self, root):

        self.root = root

        self.templates_list = database_methods.Get_Templates_List()

        # Main grid widgets:

        self.drop_menu = ttk.Combobox(self.root, values=self.templates_list, justify='center')

        self.confirmation_button = ttk.Button(self.root, text="Confirm", width=21, cursor='hand2',
                                command=lambda: self.Change_Speed(Get_Mouse_Speed(self.drop_menu.get().split('  ')[0])))

        self.reset_button = ttk.Button(self.root, text="Reset to Default", command=lambda: self.Change_Speed(10),
                                       width=21, cursor='hand2')

        self.modify_button = ttk.Button(self.root, text="Modify Templates", width=21, cursor='hand2',
                                        command=self.Modification_Grid)

        self.current_speed_label = Label(self.root, text=f"Current Speed: {self.Get_Current_Speed()}",
                                             font='Impact', fg='#022b5d', bg='#dcdad5')

        grid.Main_Grid(self.templates_list, self.drop_menu, self.confirmation_button, self.reset_button,
                       self.modify_button, self.current_speed_label)

        # Modification grid widgets:

        self.new_template_button = ttk.Button(self.root, text="Add Weapon", command=self.Add_Weapon,
                                       width=21, cursor='hand2')

        self.weapon_name_entry = Entry(self.root, state='disabled', disabledbackground='#dcdad5', justify='center')

        self.weapon_speed_entry = Entry(self.root, state='disabled', disabledbackground='#dcdad5', justify='center')

        self.save_new_template_button = ttk.Button(self.root, text="Save", command=self.Save_Weapon, state='disabled',
                                            width=21, cursor='hand2')


        self.edit_speed_button = ttk.Button(self.root, text="Edit Template", command=self.Edit_Speed,
                                            width=21, cursor='hand2')

        self.edit_drop_menu = ttk.Combobox(self.root, values=self.templates_list, justify='center', state='disabled')

        self.weapon_speed_edit_entry = Entry(self.root, state='disabled', disabledbackground='#dcdad5',justify='center')

        self.save_new_edit_button = ttk.Button(self.root, text="Save", command=self.Save_Edit, state='disabled',
                                                 width=21, cursor='hand2')


        self.delete_template_button = ttk.Button(self.root, text="Delete Template", command=self.Delete_Template,
                                            width=21, cursor='hand2')

        self.delete_drop_menu = ttk.Combobox(self.root, values=self.templates_list, justify='center', state='disabled')

        self.save_delete_button = ttk.Button(self.root, text="Delete", command=self.Save_Delete, state='disabled',
                                               width=21, cursor='hand2')

        self.delete_all_templates_button = ttk.Button(self.root, text="Delete All Templates", command=self.Delete_All,
                                             width=21, cursor='hand2')

        self.return_button = ttk.Button(self.root, text="❮ Back ", command=self.Return_Main_Grid,
                                             width=21, cursor='hand2')


    def Add_Weapon(self):
        self.weapon_name_entry.configure(state='normal')
        self.weapon_speed_entry.configure(state='normal')
        self.save_new_template_button.configure(state='normal')

        self.weapon_name_entry.insert(0, "Weapon Name")
        self.weapon_speed_entry.insert(0, "Mouse Speed: 1-20")

        self.weapon_name_entry.bind("<FocusIn>", self.Unbind_Weapon_Entry)
        self.weapon_speed_entry.bind("<FocusIn>", self.Unbind_Speed_Entry)

    def Save_Weapon(self):
        if len(self.weapon_name_entry.get()) == 0 or self.weapon_name_entry.get() == "Weapon Name":
            Empty_Error()
            self.weapon_name_entry.focus_force()
            return

        elif len(self.weapon_speed_entry.get()) == 0:
            Empty_Error()
            self.weapon_speed_entry.focus_force()
            return

        try:
            if int(self.weapon_speed_entry.get()) < 1 or int(self.weapon_speed_entry.get()) > 20:
                Range_Error('1', '20')
                self.weapon_speed_entry.focus_force()
                return

        except:
            Instance_Error("whole number")
            self.weapon_speed_entry.focus_force()
            return

        database_methods.Add_Weapon(self.weapon_name_entry.get(), int(self.weapon_speed_entry.get()))
        self.weapon_name_entry.delete(0, "end")
        self.weapon_speed_entry.delete(0, "end")
        self.Disable_Widgets()
        self.Update_Dropmenus()

    def Edit_Speed(self):
        if (len(self.templates_list) == 0):
            Empty_Database_Error('edit')
            return
        self.edit_drop_menu.configure(state='normal')
        self.weapon_speed_edit_entry.configure(state='normal')
        self.save_new_edit_button.configure(state='normal')

        self.weapon_speed_edit_entry.insert(0, "Mouse Speed: 1-20")

        self.weapon_speed_edit_entry.bind("<FocusIn>", self.Unbind_Speed_Edit_Entry)

    def Save_Edit(self):
        if len(self.weapon_speed_edit_entry.get()) == 0:
            Empty_Error()
            self.weapon_speed_edit_entry.focus_force()
            return

        try:
            if int(self.weapon_speed_edit_entry.get()) < 1 or int(self.weapon_speed_edit_entry.get()) > 20:
                Range_Error('1', '20')
                self.weapon_speed_edit_entry.focus_force()
                return

        except:
            Instance_Error("whole number")
            self.weapon_speed_edit_entry.focus_force()
            return

        database_methods.Edit_Speed(self.edit_drop_menu.get().split('  ')[0], int(self.weapon_speed_edit_entry.get()))
        self.weapon_speed_edit_entry.delete(0, "end")
        self.Disable_Widgets()
        self.Update_Dropmenus()


    def Delete_Template(self):
        if (len(self.templates_list) == 0):
            Empty_Database_Error('delete')
            return
        self.delete_drop_menu.configure(state='normal')
        self.save_delete_button.configure(state='normal')

    def Save_Delete(self):
        confirmation = Confirmation_Message()
        if confirmation:
            database_methods.Delete_Weapon(self.delete_drop_menu.get().split('  ')[0])
            self.Disable_Widgets()
            self.Update_Dropmenus()


    def Delete_All(self):
        if (len(self.templates_list) == 0):
            Empty_Database_Error('delete')
            return
        confirmation = Confirmation_Message()
        if confirmation:
            database_methods.Delete_All_Weapons()
            self.Disable_Widgets()
            self.Update_Dropmenus()

    def Modification_Grid(self):
        grid.Hide_Main_Grid(self.drop_menu, self.confirmation_button, self.reset_button, self.modify_button,
                            self.current_speed_label)
        grid.Modification_Grid(self.templates_list, self.new_template_button, self.weapon_name_entry,
                               self.weapon_speed_entry, self.save_new_template_button, self.edit_speed_button,
                               self.edit_drop_menu, self.weapon_speed_edit_entry, self.save_new_edit_button,
                               self.delete_template_button, self.delete_drop_menu, self.save_delete_button,
                               self.delete_all_templates_button, self.return_button)

    def Return_Main_Grid(self):
        grid.Hide_Modification_Grid(self.new_template_button, self.weapon_name_entry, self.weapon_speed_entry,
                                    self.save_new_template_button, self.edit_speed_button, self.edit_drop_menu,
                                    self.weapon_speed_edit_entry, self.save_new_edit_button,
                                    self.delete_template_button, self.delete_drop_menu, self.save_delete_button,
                                    self.delete_all_templates_button, self.return_button)
        grid.Main_Grid(self.templates_list, self.drop_menu, self.confirmation_button, self.reset_button,
                       self.modify_button, self.current_speed_label)


    def Unbind_Weapon_Entry(self, event):
        self.weapon_name_entry.delete(0, "end")
        self.weapon_name_entry.unbind("<FocusIn>")
        return None

    def Unbind_Speed_Entry(self, event):
        self.weapon_speed_entry.delete(0, "end")
        self.weapon_speed_entry.unbind("<FocusIn>")
        return None

    def Unbind_Speed_Edit_Entry(self, event):
        self.weapon_speed_edit_entry.delete(0, "end")
        self.weapon_speed_edit_entry.unbind("<FocusIn>")
        return None


    def Change_Speed(self, speed):
        set_mouse_speed = 113
        ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)
        self.current_speed_label.configure(text=f"Current Speed: {self.Get_Current_Speed()}")

    def Get_Current_Speed(self):
        get_mouse_speed = 112
        speed = ctypes.c_int()
        ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)
        return speed.value

    def Disable_Widgets(self):
        self.weapon_name_entry.configure(state='disabled')
        self.weapon_speed_entry.configure(state='disabled')
        self.save_new_template_button.configure(state='disabled')

        self.edit_drop_menu.configure(state='disabled')
        self.weapon_speed_edit_entry.configure(state='disabled')
        self.save_new_edit_button.configure(state='disabled')

        self.delete_drop_menu.configure(state='disabled')
        self.save_delete_button.configure(state='disabled')

    def Update_Dropmenus(self):
        self.templates_list = database_methods.Get_Templates_List()
        self.drop_menu.configure(values=self.templates_list)
        self.delete_drop_menu.configure(values=self.templates_list)
        self.edit_drop_menu.configure(values=self.templates_list)
        if len(self.templates_list) != 0:
            self.drop_menu.current(0)
            self.delete_drop_menu.current(0)
            self.edit_drop_menu.current(0)
        else:
            self.drop_menu.set('')
            self.delete_drop_menu.set('')
            self.edit_drop_menu.set('')
