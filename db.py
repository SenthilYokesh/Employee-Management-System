import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        qry = """
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age TEXT,
            doj TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            address TEXT,
            dept TEXT,
            job_pos TEXT
            )
            """
        self.cur.execute(qry)
        self.con.commit()

    #  INSERT FUNCTION
    def insert(self, first_name, last_name, age, doj, email, gender, contact, address, dept, job_pos):
        self.cur.execute("INSERT INTO employees VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", (
            first_name, last_name, age, doj, email, gender, contact, address, dept, job_pos))
        self.con.commit()

    #  UPDATE FUNCTION
    def update(self, id, first_name, last_name, age, doj, email, gender, contact, address, dept, job_pos):
        self.cur.execute(
            "UPDATE employees SET first_name=?,last_name=?,age=?,doj=?,email=?,gender=?,contact=?,"
            "address=?,dept=?,job_pos=? WHERE id=?",
            (first_name, last_name, age, doj, email, gender, contact, address, dept, job_pos, id))
        self.con.commit()

    #  DISPLAY FUNCTION
    def display(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    #  DELETE FUNCTION
    def delete(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.con.commit()
