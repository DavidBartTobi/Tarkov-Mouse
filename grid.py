

def Main_Grid(templates_list, drop_menu, confirmation_button, reset_button, modify_button, current_speed_label):
    
    drop_menu.grid(row=0, column=0, columnspan=2, pady=(320, 0), ipady=5, padx=(180,0))
    drop_menu.configure(width=30)
    if len(templates_list) != 0:
        drop_menu.current(0)
    else:
        drop_menu.set('')

    confirmation_button.grid(row=0, column=2, columnspan=2, pady=(320, 0), padx=(0,180), ipadx=29)

    reset_button.grid(row=1, column=0, columnspan=2, pady=25, padx=(180,0), ipadx=29)

    modify_button.grid(row=1, column=2, columnspan=2, pady=25, padx=(0,180), ipadx=29)

    current_speed_label.grid(row=2, rowspan=2, columnspan=4, ipadx=12, ipady=2, pady=(0, 40))


def Modification_Grid(templates_list, new_template_button, weapon_name_entry, weapon_speed_entry, save_new_template_button
                      , edit_speed_button, edit_drop_menu, weapon_speed_edit_entry, save_new_edit_button,
                      delete_template_button, delete_drop_menu, save_delete_button, delete_all_templates_button,
                      return_button):
    new_template_button.grid(row=0, column=0, pady=(300, 0), ipadx=29, padx=(10, 0))
    weapon_name_entry.grid(row=0, column=1, pady=(300, 0), ipady=6, ipadx=38)
    weapon_speed_entry.grid(row=0, column=2, pady=(300, 0), ipady=6, ipadx=38)
    save_new_template_button.grid(row=0, column=3, pady=(300, 0), ipadx=29, padx=(0, 10))

    edit_speed_button.grid(row=1, column=0, ipadx=29, padx=(10, 0))
    edit_drop_menu.grid(row=1, column=1, ipady=5)
    edit_drop_menu.configure(width=30)
    if len(templates_list) != 0:
        edit_drop_menu.current(0)
    else:
        edit_drop_menu.set('')
    weapon_speed_edit_entry.grid(row=1, column=2, ipady=6, ipadx=38)
    save_new_edit_button.grid(row=1, column=3, ipadx=29, padx=(0, 10))

    delete_template_button.grid(row=2, column=0, ipadx=29, padx=(10, 0))
    delete_drop_menu.grid(row=2, column=1, ipady=5)
    delete_drop_menu.configure(width=30)
    if len(templates_list) != 0:
        delete_drop_menu.current(0)
    else:
        delete_drop_menu.set('')
    save_delete_button.grid(row=2, column=3, ipadx=29, padx=(0,10))

    return_button.grid(row=3, column=0, ipadx=29, padx=(10, 0))
    delete_all_templates_button.grid(row=3, column=3, ipadx=29, padx=(0, 10))


def Hide_Main_Grid(drop_menu, confirmation_button, reset_button, modify_button, current_speed_label):
    drop_menu.grid_forget()
    confirmation_button.grid_forget()
    reset_button.grid_forget()
    modify_button.grid_forget()
    current_speed_label.grid_forget()


def Hide_Modification_Grid(new_template_button, weapon_name_entry, weapon_speed_entry, save_new_template_button,
                      edit_speed_button, edit_drop_menu, weapon_speed_edit_entry, save_new_edit_button,
                      delete_template_button, delete_drop_menu, save_delete_button, delete_all_templates_button,
                      return_button):

    new_template_button.grid_forget()
    weapon_name_entry.grid_forget()
    weapon_speed_entry.grid_forget()
    save_new_template_button.grid_forget()
    edit_speed_button.grid_forget()
    edit_drop_menu.grid_forget()
    weapon_speed_edit_entry.grid_forget()
    save_new_edit_button.grid_forget()
    delete_template_button.grid_forget()
    delete_drop_menu.grid_forget()
    save_delete_button.grid_forget()
    delete_all_templates_button.grid_forget()
    return_button.grid_forget()