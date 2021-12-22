#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : songshanyuwu
# @Time   : 2021/12/21 16:29
# -----------------------------------------------
# 通过pushplus推送威胁情报
# -----------------------------------------------

import os
import json
import requests

PUSHPLUSSCKEY = os.environ.get('PUSHPLUSSCKEY') ##PUSHPLUS推送KEY

def to_pushplus(cves):
    newstitle = "威胁情报播报"
    PushPlus = 'http://www.pushplus.plus/send'
    data = {
        "token":PUSHPLUSSCKEY,
        "title":newstitle,
        "content":cves,
        "template":"txt"
    }
    # body=json.dumps(data).encode(encoding='utf-8')
    body=json.dumps(data)
    requests.post(url=PushPlus,data=body,headers=headers)
    return 'PushPlus推送成功'
