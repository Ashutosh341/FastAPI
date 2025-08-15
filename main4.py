import pyodbc

server = 'ASHUTOSH\MSSQLSERVER03'       # e.g., 'DESKTOP-12345\\SQLEXPRESS'
database = 'NamasteSQl'
username = 'Ashutosh/ashut'
#password = 'YOUR_DB_PASSWORD'
driver = '{ODBC Driver 17 for SQL Server}'

# try:
#     conn = pyodbc.connect(
#         f'DRIVER={driver};'
#         f'SERVER={server};'
#         f'DATABASE={database};'
#         f'UID={username};'
#         f'PWD={password}'
#     )
#     print("✅ Connected to SQL Server")
#     conn.close()
# except Exception as e:
#     print("❌ Connection failed:", e)

try:
    conn = pyodbc.connect(
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'Trusted_Connection=yes;'
        
    )
    print("✅ Connected to SQL Server")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)