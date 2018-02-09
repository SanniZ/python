#!/usr/bin/python

import os
import sqlite3
import string

SQL_COMPANY_DB = 'company.db'

USAGE_MENU='''0: Exit
1: Create TABLE
2: Insert
3: Update
4: Delete
5: Show
Enter your option(0/1/2.3?):'''

# connect.
def get_conn():
	return 	sqlite3.connect(SQL_COMPANY_DB)

# commit and close.
def exit_conn(conn):
	conn.comit()
	conn.close()

# create table.
def create_table():
	conn = get_conn()
	cur = conn.cursor()

	sql_create_table = '''CREATE TABLE COMPANY
		(ID    INT PRIMARY KEY NOT NULL,
		NAME      TEXT    NOT NULL,
		AGE       INT     NOT NULL,
		PID       INT,
		ADDRESS   TEXT,
		DEPT      TEXT,
		SALARY    INT)'''

	cur.execute(sql_create_table)

	exit_conn(conn)

# insert into table
def insert_table():
	conn = get_conn()
	cur = conn.cursor()

	id, name,age=input('(ID, NAME,AGE):')
	sql_insert = 'INSERT INTO COMPANY (ID, NAME, AGE) VALUES (%s,\'%s\',%s)' %(id,name,age)
	cur.execute(sql_insert)

	exit_conn(conn)


# loop for options.
def main():
	while True:
		ops = input(USAGE_MENU)

		if ops == 0:
			break
		elif ops == 1:
			create_table()
		elif ops == 2:
			insert_table()
		elif ops == 3:
			pass
		else:
			print('Not supported, please try again!')
			continue

# main for enterance.
if __name__ == '__main__':
	main()
