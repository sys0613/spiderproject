# -*- coding:utf-8 -*-
import requests,random
from tools import constant


# 定义HTTP 请求前的头信息
def get_random_header():
    headers = {'User-Agent': random.choice(constant.user_agent_list),
               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               }
    return headers

def sendmessage(uid):
    print('uid:',uid)
    tagurl='https://www.incnjp.com/home.php?mod=spacecp&ac=pm&op=send&touid='+uid+'&inajax=1'
    payload = {'pmsubmit': 'true', 'touid': uid, 'formhash': '734325bc', 'handlekey': 'showMsgBox', 'message': '打开支付宝首页搜索“7211781”，即可领红包','messageappend':''}
    str_cookie='__cfduid=d1c0a20800d0ae326f2c3ed5c0396bce41533187654; yjs_id=e6b176328020c4300e2eef5e5af5591b; ctrl_time=1; _pk_ref.1.3141=%5B%22%22%2C%22%22%2C1533187656%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DtnUYQDjMaJQBOGEYhfDmpBs6qafwlI-acJdOfW7B1JHjNaG-_5nAfJi439Jkc0Qh%26wd%3D%26eqid%3Def7aa99a0006bdfa000000035b629644%22%5D; _pk_ses.1.3141=*; Z8CI_2132_sid=Caal66; Z8CI_2132_saltkey=M2YL2RRT; Z8CI_2132_lastvisit=1533184702; Z8CI_2132_ulastactivity=c790dd4e%2BT%2FKbvc9r6QVskybFiVzNnk2W2G7CKsd8Ya7DfFcfQAM; Z8CI_2132_auth=06437WpajrUijWZSmyhAeBBvgWQs6o5pxNNO27STOmabwxfHXfSUwJwqnBADjU%2BBPZOFICQZ6R82MIE%2B%2BAwoIf2d4xsV; Z8CI_2132_lip=42.103.52.102%2C1533188180; Z8CI_2132_myrepeat_rr=R0; Z8CI_2132_smile=23D1; Z8CI_2132_nofavfid=1; Z8CI_2132_st_p=1033949%7C1533189340%7Ca1091edfa40128a699e6039217dbc95e; Z8CI_2132_visitedfid=591; Z8CI_2132_viewid=tid_4532898; Z8CI_2132_lastcheckfeed=1033949%7C1533189787; _pk_id.1.3141=d106570284423812.1533187656.1.1533190371.1533187656.; Z8CI_2132_lastact=1533190370%09misc.php%09patch'
    cookies = dict(cookies_are=str_cookie)
    proxies = {'http': '125.45.87.12 :9999'}
    res=requests.post(url=tagurl,data=payload,headers=get_random_header(),proxies=proxies,cookies=cookies)

    print(res.text)




if __name__=='__main__':
    sendmessage(str(1033948))
    # n=1033948
    # while n>1030000:
    #     sendmessage(str(1033948))
    #     n=n-1
