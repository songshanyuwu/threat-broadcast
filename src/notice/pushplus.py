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

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57",
        "Referer": "https://tv.cctv.com/lm/xwlb/",
        "Accept": "text/html, */*; q=0.01"
    }


def to_pushplus(cves):
    newstitle = "威胁情报播报"
    PushPlus = 'http://www.pushplus.plus/send'
    content = format_content(cves)
    print("#################################")
    print(len(content))
    content = content[0:6666]
    print(len(content))
    print(PUSHPLUSSCKEY)
    print("#################################")
    data = {
        "token":PUSHPLUSSCKEY,
        "title":newstitle,
        "content":content,
        "template":"html"
    }
    body=json.dumps(data).encode(encoding='utf-8')
    requests.post(url=PushPlus,data=body,headers=headers)
    return 'PushPlus推送成功'


def format_content(cves):
    src_tpl = '    <li><font color="red">%(cnt)d</font>条由 [<a href="%(url)s">%(src)s</a>] 提供</li>'
    mail_tpl =  '''
<h3>发现最新威胁情报<font color="red">%(total)d</font>条：</h3>
<ul>
%(src_infos)s
</ul>
<h3>详细漏洞清单如下：</h3>
<br/>
%(cve_infos)s

<br/><br/>
++++++++++++++++++++++++++++++++++++++++++++++
<br/>
<font color="red">【情报收集与播报支持】</font> https://lyy289065406.github.io/threat-broadcast/
'''
    src_infos = []
    cve_infos = []
    total = 0
    for src, _cves in cves.items():
        cnt = len(_cves)
        total += cnt
        src_infos.append(src_tpl % {
            'cnt': cnt,
            'url': src.HOME_PAGE(),
            'src': src.NAME_CH()
        })
        for cve in _cves:
            cve_infos.append(cve.to_html())

    content = mail_tpl % {
        'total': total,
        'src_infos': '\n'.join(src_infos),
        'cve_infos': '\n'.join(cve_infos)
    }
    return content
