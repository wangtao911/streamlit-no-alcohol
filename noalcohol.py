# streamlit run noalcohol.py

import streamlit as st
import sqlite3
import datetime

# create a database
conn = sqlite3.connect('no-alcohol.db')
cur =  conn.cursor()

if False:
    try:
        table_name = 'no_alcohol'
        cur.execute(f'DROP TABLE IF EXISTS {table_name}')
        table_name = 'trigger_reason'
        cur.execute(f'DROP TABLE IF EXISTS {table_name}')
        table_name = 'alcohol_harm'
        cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    except:
        pass

# create a table
# '2023-09-18 11:45:00'
sql_command = '''
    CREATE TABLE IF NOT EXISTS no_alcohol (
    id INTEGER PRIMARY KEY,
    创建时间 DATE,
    触发原因 TEXT,
    新的触发原因 TEXT,
    酒精对身体的危害 TEXT,
    酒精对大脑的危害 TEXT,
    酒精的危害 TEXT,
    成功的原因 TEXT,
    失败的原因 TEXT,
    惭愧地喝了多少毫升 INTEGER,
    少喝了多少毫升 INTEGER,
    酒精的热量 INTEGER,
    代替饮酒的方法 TEXT
    )'''
cur.execute(sql_command)

sql_command = '''
    CREATE TABLE IF NOT EXISTS trigger_reason(
    id INTEGER PRIMARY KEY,
    触发原因 TEXT,
    UNIQUE(触发原因)
    )'''
cur.execute(sql_command)
sql_text_2 = "INSERT OR IGNORE INTO trigger_reason (触发原因) VALUES('')"
cur.execute(sql_text_2)
sql_text_2 = "INSERT OR IGNORE INTO trigger_reason (触发原因) VALUES('独自一人')"
cur.execute(sql_text_2)
sql_text_2 = "INSERT OR IGNORE INTO trigger_reason (触发原因) VALUES('为了庆祝')"
cur.execute(sql_text_2)

sql_command = '''
    CREATE TABLE IF NOT EXISTS alcohol_harm(
    id INTEGER PRIMARY KEY,
    酒精的危害 TEXT,
    UNIQUE(酒精的危害)
    )'''
cur.execute(sql_command)
sql_text_2 = "INSERT OR IGNORE INTO alcohol_harm (酒精的危害) VALUES('高热量')"
cur.execute(sql_text_2)
sql_text_2 = "INSERT OR IGNORE INTO alcohol_harm (酒精的危害) VALUES('影响记忆力')"
cur.execute(sql_text_2)


# 检查表头 和 前5个数据
def check_table_info(table_name):
    st.text('检查表头 和 前5个数据')
    #table_name = 'no_alcohol'
    cur.execute(f'PRAGMA table_info({table_name})')
    headers = [header[1] for header in cur.fetchall()]
    st.text(headers)
    cur.execute(f'SELECT * FROM {table_name} LIMIT 5')
    rows = cur.fetchall()
    for row in rows:
        st.text(row)



# 检查表头 和 前5个数据
# check_table_info('no_alcohol')
# check_table_info('trigger_reason')
# check_table_info('alcohol_harm')



# snippet
today = datetime.datetime.now()
formatted_date = today.strftime('%Y-%m-%d')
date_obj = datetime.datetime.strptime(formatted_date, '%Y-%m-%d').date()
formatted_time = today.strftime('%H:%M:%S')
time_obj = datetime.datetime.strptime(formatted_time, '%H:%M:%S').time()

# 准备酒精危害的列表
#st.text('准备酒精危害的列表')
alcohol_harm_list = []
table_name = 'alcohol_harm'
cur.execute(f'PRAGMA table_info({table_name})')
cur.execute(f'SELECT * FROM {table_name} ' )
rows = cur.fetchall()
for row in rows:
    #st.text(row[1])
    alcohol_harm_list.append(row[1])

#sss

# 准备触发原因列表
#st.text('准备触发原因列表')
trigger_reason_list = []
table_name = 'trigger_reason'
cur.execute(f'PRAGMA table_info({table_name})')
cur.execute(f'SELECT * FROM {table_name} ' )
rows = cur.fetchall()
for row in rows:
    #st.text(row[1])
    trigger_reason_list.append(row[1])



#st.write('now date is:', date_obj)
#st.write('now time is:', time_obj)
col1, col2 = st.columns(2)
with col1:
    shenti_harm = st.text_input('酒精对身体的危害',"身体")

with col2:
    danao_harm = st.text_input('酒精对大脑的危害',"大脑")


col1, col2 = st.columns(2)
with col1:
    st.text('酒精的危害')
    harm=''
    for n in alcohol_harm_list:
        harm= harm+n+'!  '
    #st.write(harm)
    st.error(harm,icon="🚨")
with col2:
    st.write('酒精的热量')
    st.error('42卡/100ml，2杯=5公里',icon="🚨")
    jiujing_reliang = 42

col1, col2 = st.columns(2)
with col1:
    chufa_yuanyin = st.selectbox('触发原因',trigger_reason_list)
with col2:    
    xin_chufa_yuanyin = st.text_input('新的触发原因','新原因？')

st.text('代替饮酒的方法')
st.error('''
告诉对方自己身体不好，不希望喝酒\n
喝杯冰镇的苏打水\n
运动一下，或者换算两杯酒=5公里\n
玩游戏\n
''',icon="🚨")
col1, col2 = st.columns(2)
with col1:
    chenggong_yuanyin= st.text_input('成功的原因',)
with col2:
    shibai_yuanyin = st.text_input('失败的原因',)

col1, col2 = st.columns(2)
with col1:
    duo_he_le_duoshao = int(st.text_input('多喝了多少毫升?',"0"))
    shao_he_le_duoshao = 300
    shao_he_le_duoshao = shao_he_le_duoshao - duo_he_le_duoshao
with col2:
    shao_he_le_duoshao = int(st.text_input('少喝了多少毫升?',str(shao_he_le_duoshao)))

col1, col2 = st.columns(2)
with col1:
    if st.button('提交',type="primary"):
        # 更新酒精伤害
        if len(danao_harm) > 0:
            sql_text_3 = "INSERT OR IGNORE INTO alcohol_harm (酒精的危害) VALUES('"+danao_harm+"')"
            st.text(sql_text_3)
            cur.execute(sql_text_3)
        if len(shenti_harm) > 0:
            sql_text_3 = "INSERT OR IGNORE INTO alcohol_harm (酒精的危害) VALUES('"+shenti_harm+"')"
            st.text(sql_text_3)
            cur.execute(sql_text_3)
        
        # 更新触发原因
        if len(xin_chufa_yuanyin) >0:
            sql_text_3 = "INSERT OR IGNORE INTO trigger_reason (触发原因) VALUES('"+xin_chufa_yuanyin+"')"
            st.text(sql_text_3)
            cur.execute(sql_text_3)
        
        # 新增记录
        sql_text_4 = '''
        INSERT INTO no_alcohol 
        (创建时间,触发原因,新的触发原因,酒精对身体的危害,酒精对大脑的危害,成功的原因,失败的原因,惭愧地喝了多少毫升,少喝了多少毫升) VALUES(?,?,?,?,?,?,?,?,?)'''
        st.text(sql_text_4)
        cur.execute(sql_text_4,(today,chufa_yuanyin,xin_chufa_yuanyin,shenti_harm,danao_harm,chenggong_yuanyin,shibai_yuanyin,duo_he_le_duoshao,shao_he_le_duoshao))

    else:
        st.write('少喝一口是一口')

with col2:
    #st.button("Reset")
    pass




# 提交更改并关闭连接
conn.commit()
conn.close()