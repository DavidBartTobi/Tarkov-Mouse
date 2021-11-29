from tkinter import *
from tkinter import ttk
from gui_utilities import empty_error, instance_error, range_error, confirmation_message, empty_database_error
import database_methods
from ctypes import windll, c_int, byref
import grid


class Program:

    def __init__(self, root):

        self.root = root

        self.templates_list = database_methods.get_templates_list()

        # Main grid widgets:

        self.drop_menu = ttk.Combobox(self.root, values=self.templates_list, justify='center')

        self.confirmation_button = ttk.Button(self.root, text="Confirm", width=21, cursor='hand2',
                                command=lambda: self.change_speed(database_methods.get_mouse_speed(self.drop_menu.get().split('  ')[0])))

        self.reset_button = ttk.Button(self.root, text="Reset to Default", command=lambda: self.change_speed(10),
                                       width=21, cursor='hand2')

        self.modify_button = ttk.Button(self.root, text="Modify Templates", width=21, cursor='hand2',
                                        command=self.modification_grid)

        self.current_speed_label = Label(self.root, text=f"Current Speed: {self.get_current_speed()}",
                                             font='Impact', fg='#022b5d', bg='#dcdad5')

        grid.main_grid(self.templates_list, self.drop_menu, self.confirmation_button, self.reset_button,
                       self.modify_button, self.current_speed_label)

        # Modification grid widgets:

        self.new_template_button = ttk.Button(self.root, text="Add Weapon", command=self.add_weapon,
                                       width=21, cursor='hand2')

        self.weapon_name_entry = Entry(self.root, state='disabled', disabledbackground='#dcdad5', justify='center')

        self.weapon_speed_entry = Entry(self.root, state='disabled', disabledbackground='#dcdad5', justify='center')

        self.save_new_template_button = ttk.Button(self.root, text="Save", command=self.save_weapon, state='disabled',
                                            width=21, cursor='hand2')


        self.edit_speed_button = ttk.Button(self.root, text="Edit Template", command=self.edit_speed,
                                            width=21, cursor='hand2')

        self.edit_drop_menu = ttk.Combobox(self.root, values=self.templates_list, justify='center', state='disabled')

        self.weapon_speed_edit_entry = Entry(self.root, state='disabled', disabledbackground='#dcdad5',justify='center')

        self.save_new_edit_button = ttk.Button(self.root, text="Save", command=self.save_edit, state='disabled',
                                                 width=21, cursor='hand2')


        self.delete_template_button = ttk.Button(self.root, text="Delete Template", command=self.delete_template,
                                            width=21, cursor='hand2')

        self.delete_drop_menu = ttk.Combobox(self.root, values=self.templates_list, justify='center', state='disabled')

        self.save_delete_button = ttk.Button(self.root, text="Delete", command=self.save_delete, state='disabled',
                                               width=21, cursor='hand2')

        self.delete_all_templates_button = ttk.Button(self.root, text="Delete All Templates", command=self.delete_all,
                                             width=21, cursor='hand2')

        self.return_button = ttk.Button(self.root, text="❮ Back ", command=self.return_main_grid,
                                             width=21, cursor='hand2')


    def add_weapon(self):
        self.weapon_name_entry.configure(state='normal')
        self.weapon_speed_entry.configure(state='normal')
        self.save_new_template_button.configure(state='normal')

        if len(self.weapon_name_entry.get()) == 0 and len(self.weapon_speed_entry.get()) == 0 :
            self.weapon_name_entry.insert(0, "Weapon Name")
            self.weapon_speed_entry.insert(0, "Mouse Speed: 1-20")

        self.weapon_name_entry.bind("<FocusIn>", self.unbind_weapon_entry)
        self.weapon_speed_entry.bind("<FocusIn>", self.unbind_speed_entry)

    def save_weapon(self):
        if len(self.weapon_name_entry.get()) == 0 or self.weapon_name_entry.get() == "Weapon Name":
            empty_error()
            self.weapon_name_entry.focus_force()
            return

        elif len(self.weapon_speed_entry.get()) == 0:
            empty_error()
            self.weapon_speed_entry.focus_force()
            return

        try:
            if int(self.weapon_speed_entry.get()) < 1 or int(self.weapon_speed_entry.get()) > 20:
                range_error('1', '20')
                self.weapon_speed_entry.focus_force()
                return

        except:
            instance_error("whole number")
            self.weapon_speed_entry.focus_force()
            return

        database_methods.add_weapon(self.weapon_name_entry.get(), int(self.weapon_speed_entry.get()))
        self.weapon_name_entry.delete(0, "end")
        self.weapon_speed_entry.delete(0, "end")
        self.disable_widgets()
        self.update_dropmenus()

    def edit_speed(self):
        if (len(self.templates_list) == 0):
            empty_database_error('edit')
            return
        self.edit_drop_menu.configure(state='normal')

        self.weapon_speed_edit_entry.configure(state='normal')
        self.save_new_edit_button.configure(state='normal')
        if len(self.weapon_speed_edit_entry.get()) == 0 :
            self.weapon_speed_edit_entry.insert(0, "Mouse Speed: 1-20")

        self.weapon_speed_edit_entry.bind("<FocusIn>", self.unbind_speed_edit_entry)

    def save_edit(self):
        if len(self.weapon_speed_edit_entry.get()) == 0:
            empty_error()
            self.weapon_speed_edit_entry.focus_force()
            return

        try:
            if int(self.weapon_speed_edit_entry.get()) < 1 or int(self.weapon_speed_edit_entry.get()) > 20:
                range_error('1', '20')
                self.weapon_speed_edit_entry.focus_force()
                return

        except:
            instance_error("whole number")
            self.weapon_speed_edit_entry.focus_force()
            return

        database_methods.edit_speed(self.edit_drop_menu.get().split('  ')[0], int(self.weapon_speed_edit_entry.get()))
        self.weapon_speed_edit_entry.delete(0, "end")
        self.disable_widgets()
        self.update_dropmenus()


    def delete_template(self):
        if (len(self.templates_list) == 0):
            empty_database_error('delete')
            return
        self.delete_drop_menu.configure(state='normal')
        self.save_delete_button.configure(state='normal')

    def save_delete(self):
        confirmation = confirmation_message()
        if confirmation:
            database_methods.delete_weapon(self.delete_drop_menu.get().split('  ')[0])
            self.disable_widgets()
            self.update_dropmenus()


    def delete_all(self):
        if (len(self.templates_list) == 0):
            empty_database_error('delete')
            return
        confirmation = confirmation_message()
        if confirmation:
            database_methods.delete_all_weapons()
            self.disable_widgets()
            self.update_dropmenus()

    def modification_grid(self):
        grid.hide_main_grid(self.drop_menu, self.confirmation_button, self.reset_button, self.modify_button,
                            self.current_speed_label)
        grid.modification_grid(self.templates_list, self.new_template_button, self.weapon_name_entry,
                               self.weapon_speed_entry, self.save_new_template_button, self.edit_speed_button,
                               self.edit_drop_menu, self.weapon_speed_edit_entry, self.save_new_edit_button,
                               self.delete_template_button, self.delete_drop_menu, self.save_delete_button,
                               self.delete_all_templates_button, self.return_button)

    def return_main_grid(self):
        grid.hide_modification_grid(self.new_template_button, self.weapon_name_entry, self.weapon_speed_entry,
                                    self.save_new_template_button, self.edit_speed_button, self.edit_drop_menu,
                                    self.weapon_speed_edit_entry, self.save_new_edit_button,
                                    self.delete_template_button, self.delete_drop_menu, self.save_delete_button,
                                    self.delete_all_templates_button, self.return_button)
        grid.main_grid(self.templates_list, self.drop_menu, self.confirmation_button, self.reset_button,
                       self.modify_button, self.current_speed_label)


    def unbind_weapon_entry(self, event):
        self.weapon_name_entry.delete(0, "end")
        self.weapon_name_entry.unbind("<FocusIn>")
        return None

    def unbind_speed_entry(self, event):
        self.weapon_speed_entry.delete(0, "end")
        self.weapon_speed_entry.unbind("<FocusIn>")
        return None

    def unbind_speed_edit_entry(self, event):
        self.weapon_speed_edit_entry.delete(0, "end")
        self.weapon_speed_edit_entry.unbind("<FocusIn>")
        return None


    def change_speed(self, speed):
        if speed == -1:
            empty_database_error('use')
            return
        set_mouse_speed = 113
        windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)
        self.current_speed_label.configure(text=f"Current Speed: {self.get_current_speed()}")

    def get_current_speed(self):
        get_mouse_speed = 112
        speed = c_int()
        windll.user32.SystemParametersInfoA(get_mouse_speed, 0, byref(speed), 0)
        return speed.value

    def disable_widgets(self):
        self.weapon_name_entry.configure(state='disabled')
        self.weapon_speed_entry.configure(state='disabled')
        self.save_new_template_button.configure(state='disabled')

        self.edit_drop_menu.configure(state='disabled')
        self.weapon_speed_edit_entry.configure(state='disabled')
        self.save_new_edit_button.configure(state='disabled')

        self.delete_drop_menu.configure(state='disabled')
        self.save_delete_button.configure(state='disabled')

    def update_dropmenus(self):
        self.templates_list = database_methods.get_templates_list()
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
