import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()


p=[]
while row:
    p.append(row)
    print(row[0]," " +row[4]+" "+ row[6])
    row = cursor.fetchone()

n=input("select your number")
cursor.execute('select * from Person.Person where firstname= \'' + p[n-1][4] + '\'')
