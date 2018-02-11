#!/usr/bin/python

import os
import sqlite3
import string

SQL_COMPANY_DB = 'company.db'

# connect.
def get_conn_cur():
	conn = sqlite3.connect(SQL_COMPANY_DB)
	cur = conn.cursor()
	return conn, cur

# commit and close.
def close_conn_cur(conn, cur):
	cur.close()
	conn.commit()
	conn.close()

def execute(sql, data=''):
	''' execute sql and data '''
	if sql is not None and sql != '':
		conn, cur = get_conn_cur()
		cur.execute(sql,data)
		close_conn_cur(conn, cur)

def print_table():
	conn, cur = get_conn_cur()
	sql = '''SELECT * FROM COMPANY'''
	cur.execute(sql)
	data = cur.fetchall()
	if len(data):
		for item in range(len(data)):
			print(data[item])
	print('')
	close_conn_cur(conn, cur)


Func_list = [
	('INSERT', 'INSERT INTO COMPANY (ID, NAME, AGE) VALUES (?, ?, ?)', (1, 'Hu', 32)),
	('DELETE', 'DELETE COMPANY (ID, NAME) WHERE VALUES (?, ?)', (1, 'Li')),
	('UPDATE', 'UPDATE COMPANY SET NAME=?, AGE=? WHERE ID=?', ('Li', 29, 1)),
	('SELECT', 'SELECT * FROM COMPANY WHERE ID=?', (1)),
	('SHOW', None, None),
	('EXIT', None, None)]


def usage_menu():
	menu='------Menu------\n'
	for func in Func_list:
		menu += func[0] + '\n'
	menu +='-------------------\n'
	menu += 'Enter your option:'
	return menu

# loop for options.
def main():
	usage = usage_menu()
	while True: # loop to input
		ops = raw_input(usage).upper()
		if ops == 'EXIT':
			break
		elif ops == 'SHOW':
			print_table()

		# loop to get func.
		for func in Func_list:
			if ops == func[0]:
				execute(func[1], func[2])
				print(ops + ' done!')
				break


# main for enterance.
if __name__ == '__main__':
	main()
