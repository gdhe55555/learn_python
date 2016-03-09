#!/usr/bin/env python

import re   
text= 'aaa@163.com chu-tian-shu_1932@heafaefa.com'

print re.findall(r'(\w+[-\w]*)@([a-zA-Z0-9]+).(com|org|cn)', text)
