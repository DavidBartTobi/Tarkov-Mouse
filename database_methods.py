import sqlite3


def add_weapon(name, speed):

    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    insert = "INSERT INTO Weapons (weapon_name, speed) VALUES (?,?);"
    entries = (name, speed)
    c.execute(insert, entries)

    conn.commit()
    conn.close()

def edit_speed(name, speed):

    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    c.execute(("UPDATE Weapons SET speed=? WHERE weapon_name =?"), (speed, name))

    conn.commit()
    conn.close()

def delete_weapon(name):

    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    c.execute(("DELETE FROM Weapons WHERE weapon_name =?"), (name,))

    conn.commit()
    conn.close()

def delete_all_weapons():

    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    c.execute("DELETE FROM Weapons")

    conn.commit()
    conn.close()

def get_weapon_names():

    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    list = []
    weapons = c.execute('SELECT weapon_name FROM Weapons')
    for weapon in weapons.fetchall():
        list.append(weapon[0])      # Keep it as weapon[0]. It's a list of tuples.

    conn.commit()
    conn.close()
    return list

def get_templates_list():
    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    list = []
    templates = c.execute('SELECT Weapons.weapon_name, Weapons.speed FROM Weapons')
    for template in templates.fetchall():
        list.append(template[0]+f"  [{template[1]}]")

    conn.commit()
    conn.close()
    return list

def get_weapon_id(weapon):

    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    get_id = c.execute(("SELECT weapon_id FROM Weapons WHERE weapon=?"), (weapon, ))
    id = get_id.fetchone()[0]

    conn.commit()
    conn.close()
    return id

def get_mouse_speed(weapon):

    if len(weapon) == 0:
        return -1

    conn = sqlite3.connect('MouseSpeedsDB.db')
    c = conn.cursor()

    get_speed = c.execute(("SELECT speed FROM Weapons WHERE weapon_name=?"), (weapon, ))
    speed = get_speed.fetchone()[0]

    conn.commit()
    conn.close()
    return speed
