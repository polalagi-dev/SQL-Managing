import hashlib
import mysql.connector
import time
from time import *
from hashlib import *
from Crypto.Cipher import AES

def console_sql :
    input_sql = input(host_sql,"/",database_sql,"/~$ ")


file = open("password.sha512", "w")
password_sql = input("Password >>>")
print('Encoding Password...')
sleep(1)
encode_pass = password_sql.encode('utf-8')
print('Done')
sleep(1)
print('Generating Hash From Encoded Password...')
sleep(1)
pass_hash = hashlib.sha512(encode_pass).hexdigest()
if pass_hash != "" and password_sql != "":
    print('Done')
    account_sql = input('Account/User >>>')
    host_sql = input('Host/Domain >>>')
    database_sql = input('Database >>>')
    file.write(pass_hash)
    file.close()
    database = mysql.connector.connect(
    host = host_sql,
    user = account_sql,
    password = password_sql,
    database = database_sql
    )
    provider = database.cursor()
    console_sql()
    while input != "":
        console_sql
    
else:
    print('Error While Generating Hash From Password Or Password Is Empty\nKillng Task...')
    sleep(1)
    quit()
    print('Task killed!')
    exit()

