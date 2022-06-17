import pymysql
import sys

host="1.1.1.1"
username="keystone"
password="keystone-password"
dbname="keystone"
try:
    conn = pymysql.connect(
        host,
        user=username,
        passwd=password,
        db=dbname,
        connect_timeout=5
    )
except pymysql.MySQLError as e:
	print('Got error {!r}, errno is {}'.format(e, e.args[0]))
	sys.exit()
finally:
	print('Connection opened successfully.')
