#使用方法：
#new_database,old_database添加数据库
#连接：db = select_connect('Ehai')
#查询sql:  reslut = exect_select(db,sql)
#更新和删除sql: exect_update_delete(db,sql)
#关闭连接：close_connect(db)

import pymssql

#数据库连接:
def connect_database(database,server):
    db = pymssql.connect(server,'AppUser','TY5s2x9f4iK1lpYV',database,charset='cp936')
    if db:
        print(database,"数据库链接成功",'\n')
    
    return db

#根据数据库，不区分大小写，选择新老服务器
def select_connect(database):
    new_database = ['Promotion','EhaiHangFire','OrderSharding0','OrderSharding1','OrderSharding2','OrderSharding3','OrderSharding4',
                    'OrderSharding5','OrderSharding6','OrderSharding7','OrderSharding8','OrderSharding9','OrderSharding10','OrderSharding11'
                    ,'OrderSharding12','OrderSharding13','OrderSharding14','OrderSharding15','OrderCurrent','OrderBak','EhaiStock',
                    'AvailabilityManager','OrderMessageHangfire','GpsData','ApiGateway','DataX','EhiSpiderPricing']
    old_database = ['Ehai','EhiCommon','EhaiVehicle','EhiUser']

    database_lower = database.lower()

    if database_lower in [db.lower() for db in old_database]:
        db = connect_database(database,'192.168.9.52')
        
    elif database_lower in [db.lower() for db in new_database]:
        db = connect_database(database,'192.168.9.62')
    else:
        raise ValueError(f"Database '{database}' not found in either old or new database lists.")

    return db

#查询exect_select
def exect_select(db,sql):
    cursor = db.cursor()
    cursor.execute(sql)   
    result = cursor.fetchall()
    cursor.close()
    return result

#执行更新删除exect_update_delete
def exect_update_delete(db,sql):
    cursor = db.cursor()
    cursor.execute(sql) 
    db.commit()
    cursor.close()

#关闭数据库
def close_connect(db):
    db.close()

