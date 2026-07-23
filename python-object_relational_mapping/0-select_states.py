#!/usr/bin/python3
"""Module that lists all states from the database hbtn_0e_0_usa."""
import sys
import MySQLdb


def select_states(username, password, db_name):
    """Connect to MySQL and print all states ordered by id.

    Args:
        username (str): the MySQL username.
        password (str): the MySQL password.
        db_name (str): the database name.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    select_states(sys.argv[1], sys.argv[2], sys.argv[3])
