import sqlite3

db = sqlite3.connect("DataLog.db")
cur = db.cursor()


def check_tables(num):
    for i in range(num):
        cur.execute(f"""CREATE TABLE IF NOT EXISTS 'PIR_{i}'(
                        dt STRING)""")
        db.commit()


def new_data(pir_id, dt):
    cur.execute(f"""INSERT INTO 'PIR_{pir_id}' (dt) VALUES ('{dt}')""")
    db.commit()


check_tables(4)
new_data(0, "10006300725")