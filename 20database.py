# aws mariadb 접속정보
url = 'bigdata.c8hdgnwsefiu.ap-northeast-2.rds.amazonaws.com'
uid = 'admin'
pwd = 'Bigdata_2023'
db = 'bigdata'

import mariadb

conn = None
cur = None

try:
    conn = mariadb.connect(host=url, user=uid, password=pwd, database=db)
    cur = conn.cursor()
    sql = 'select * from zipcode2013 where dong like ?'
    params = ('망원1%',)
    cur.execute(sql, params)

    for (zipcode, sido, gugun, dong, ri, bunji, seq) in cur:
        print(f'{zipcode} {sido} {gugun} {dong} {ri} {bunji}')

except mariadb.Error as e:
    print('5류발생', e)
finally:
    cur.close()
    conn.close()
