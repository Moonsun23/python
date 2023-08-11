import sys
import mariadb

url = 'bigdata.c8hdgnwsefiu.ap-northeast-2.rds.amazonaws.com'
uid = 'admin'
pwd = 'Bigdata_2023'
db = 'bigdata'


sungjuks = {}

def showSungJukMenu():
    print(f'''
    -----------------------
      성적처리프로그램 v8
    -----------------------
      1. 성적데이터 입력
      2. 성적데이터 조회
      3. 성적데이터 상세조회
      4. 성적데이터 수정
      5. 성적데이터 삭제
      0. 성적 프로그램 종료
    -----------------------
    ''')
    return input('   작업을 선택하세요: ')

def addSungJuk():
    sungjuk = input('이름과 성적을 입력하세요 (예: 홍길동 99 88 77): ')
    sj = sungjuk.split()
    
    data = [sj[0], int(sj[1]), int(sj[2]), int(sj[3]), 0, 0.0, '가']
    computeSungJuk(data)
    insertSungJuk(data) #db에 저장하는 메서드?

def computeSungJuk(val):

    val[4]=val[1]+val[2]+val[3]
    val[5]=val[4] / 3
    val[6]='수' if (90 <= val[5] <= 100) else \
            ('우'if(80 <= val[5] <= 89) else \
            ('미'if(70 <= val[5] <= 79) else \
            ('양'if(60 <= val[5] <= 69) else '가')))


def readSungJuk():
    sql = 'select name, kor, eng, math from sungjuk '
    conn = None
    cur = None

    try:
        conn = mariadb.connect(host=url, user=uid, password=pwd, database=db)
        cur = conn.cursor()
        cur.execute(sql)

        for (name, kor, eng, math) in cur:
            print(f'{name} {kor} {eng} {math}')

    except mariadb.Error as e:
        print('read 시 오류 발생', e)

    finally:
        try: cur.close()
        except: pass
        try: conn.close()
        except: pass

def readOneSungJuk():
    name = input('조회할 학생이름은? ')

    sql = 'select * from sungjuk where name = ?'
    conn = None
    cur = None

    try:
        conn = mariadb.connect(host=url, user=uid, password=pwd, database=db)
        cur = conn.cursor()
        cur.execute(sql, [name])

        for (name, kor, eng, math, tot, avg, grd) in cur:
            print(f'{name} {kor} {eng} {math} {tot} {avg} {grd}')

    except mariadb.Error as e:
        print('read 시 오류 발생', e)

    finally:
        try: cur.close()
        except: pass
        try: conn.close()
        except: pass

def modifySungJuk():
    name = input('수정할 학생이름은? ')
    kor = int(input('수정할 국어점수는? '))
    eng = int(input('수정할 영어점수는? '))
    math = int(input('수정할 수학점수는? '))

    data = [name, kor, eng, math, 0, 0.0, '가']
    computeSungJuk(data)
    updateSungJuk(data)

def updateSungJuk(data):
    sql = ' update sungjuk set kor = ?, eng = ?, math = ?, tot = ?, avg = ?, grd = ? '\
            ' where name = ? '
    conn = None
    cur = None

    try:
        conn = mariadb.connect(host=url, user=uid, password=pwd, database=db)
        cur = conn.cursor()
        cur.execute(sql, [data[1], data[2], data[3], data[4], data[5], data[6],data[0]])
        conn.commit()

    except mariadb.Error as e:
        print('update 시 오류 발생', e)


    finally:
        try: cur.close()
        except: pass
        try: conn.close()
        except: pass

def removeSungJuk():
    name = input('삭제할 학생 이름은? ')

    sql = 'delete from sungjuk where name = ?'
    conn = None
    cur = None

    try:
        conn = mariadb.connect(host=url, user=uid, password=pwd, database=db)
        cur = conn.cursor()
        cur.execute(sql, [name])
        conn.commit()

    except mariadb.Error as e:
        print('remove 시 오류 발생', e)

    finally:
        try: cur.close()
        except: pass
        try: conn.close()
        except: pass

def insertSungJuk(data):
    sql = 'insert into sungjuk values (?,?,?,?,?,?,?)'
    conn = None
    cur = None

    try:
        conn = mariadb.connect(host=url, user=uid, password=pwd, database=db)
        cur = conn.cursor()

        params = data
        cur.execute(sql, params)
        conn.commit()

        print('데이터 입력 성고옹!')

    except mariadb.Error as e:
        print('insert 시 오류 발생', e)

    finally:
        try: cur.close()
        except: pass
        try: conn.close()
        except: pass

def mainSungJuk():
    while True:
        menu = showSungJukMenu()

        if menu == '1':
                addSungJuk()
        elif menu == '2':
                readSungJuk()
        elif menu == '3':
                readOneSungJuk()
        elif menu == '4':
                modifySungJuk()
        elif menu == '5':
                removeSungJuk()
        elif menu == '0':
                sys.exit(0)

                
# 프로그램 실행 진입점
if __name__ == "__main__":
    mainSungJuk()












