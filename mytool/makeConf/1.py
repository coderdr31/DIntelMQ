# python3 运行要更改moudle路径
start = 46
end = 57
with open('/opt/intelmq/etc/pipeline.conf', 'wt') as f2:
    f2.write('{'+'\n')
with open('/opt/intelmq/etc/runtime.conf', 'wt') as f2:
    f2.write('{'+'\n')

with open('/home/dr/Desktop/tmp/moudle/pipeline.conf', 'r') as f:
    tem = f.read()
    for i in range(start, end):
        t = tem.replace('-1-', '-%d-'%(i)).replace('"file-output-1": {', '"file-output-%d": {'%(i))
        with open('/opt/intelmq/etc/pipeline.conf', 'at') as f2:
            f2.write(t)

with open('/home/dr/Desktop/tmp/moudle/runtime.conf', 'r') as f:
    tem = f.read()
    for i in range(start, end):
        t = tem.replace('-1-', '-%d-'%(i)).replace('"file-output-1": {', '"file-output-%d": {'%(i))
        with open('/opt/intelmq/etc/runtime.conf', 'at') as f2:
            f2.write(t)

with open('/opt/intelmq/etc/pipeline.conf', 'at') as f2:
    f2.write('}')
with open('/opt/intelmq/etc/runtime.conf', 'at') as f2:
    f2.write('}')
print("make ok")
