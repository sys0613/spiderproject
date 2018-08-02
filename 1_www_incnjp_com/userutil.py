# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import commOBJ
import mysql.connector

# 准备数据库
conn = mysql.connector.connect(user='root', password='root', database='incnjp')
cursor = conn.cursor()

def getUserInfoByUid(uid):
    str_cookie='__cfduid=d1c0a20800d0ae326f2c3ed5c0396bce41533187654; yjs_id=e6b176328020c4300e2eef5e5af5591b; ctrl_time=1; _pk_ref.1.3141=%5B%22%22%2C%22%22%2C1533187656%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DtnUYQDjMaJQBOGEYhfDmpBs6qafwlI-acJdOfW7B1JHjNaG-_5nAfJi439Jkc0Qh%26wd%3D%26eqid%3Def7aa99a0006bdfa000000035b629644%22%5D; _pk_ses.1.3141=*; Z8CI_2132_sid=Caal66; Z8CI_2132_saltkey=M2YL2RRT; Z8CI_2132_lastvisit=1533184702; Z8CI_2132_ulastactivity=c790dd4e%2BT%2FKbvc9r6QVskybFiVzNnk2W2G7CKsd8Ya7DfFcfQAM; Z8CI_2132_auth=06437WpajrUijWZSmyhAeBBvgWQs6o5pxNNO27STOmabwxfHXfSUwJwqnBADjU%2BBPZOFICQZ6R82MIE%2B%2BAwoIf2d4xsV; Z8CI_2132_lip=42.103.52.102%2C1533188180; Z8CI_2132_myrepeat_rr=R0; Z8CI_2132_smile=23D1; Z8CI_2132_nofavfid=1; Z8CI_2132_st_p=1033949%7C1533189340%7Ca1091edfa40128a699e6039217dbc95e; Z8CI_2132_visitedfid=591; Z8CI_2132_viewid=tid_4532898; Z8CI_2132_lastcheckfeed=1033949%7C1533189787; _pk_id.1.3141=d106570284423812.1533187656.1.1533190371.1533187656.; Z8CI_2132_lastact=1533190370%09misc.php%09patch'
    cookies = dict(cookies_are=str_cookie)
    proxies = {'http': '125.45.87.12 :9999'}
    req=requests.get('https://www.incnjp.com/space-uid-'+uid+'.html',proxies=proxies,cookies=cookies)
    soup=BeautifulSoup(req.text,'html5lib')
    class_sd_div=soup.find('div',class_='sd')
    if class_sd_div==None:
        print('uid:',uid,'不存在')
        return None
    class_xs2_h2=class_sd_div.find('h2',class_='xs2')
    # print(class_xs2_h2.prettify())
    username=class_xs2_h2.get_text()
    print('uid:',uid,'username:',username)
    return commOBJ.UserInfo(username,uid)



if __name__ == "__main__" :
    n=1033948
    #每次启动前，先查询数据库中最小uid，n从这个最小的，继续查询并入库，这样每次启动时候，就不需要看数据库上次查询多少了
    cursor.execute('SELECT MIN(uid) FROM userinfo ORDER BY uid')
    n=cursor.fetchone()[0]-1
    while n>0:
        userInfo=getUserInfoByUid(str(n))
        if not userInfo is None:
            cursor.execute('insert into userinfo (uid,username) values (%s,%s)', [userInfo.useruid, userInfo.username])
            if (n % 15 == 0 or n == 1):
                conn.commit()
            # print('receive:',userInfo.username,userInfo.useruid)
        n=n-1
    cursor.close()
    conn.close()



