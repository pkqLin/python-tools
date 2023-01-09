import quopri       #quoted-printable编解码
with open("d:\contacts.vcf", 'r',encoding='utf-8') as rf, open('d:\contacts.txt', 'w',encoding='utf-8') as wf:
    content = ['', '', '', '']
    tel = 0
    not_1_line=0
    fn=''               #多行姓名
    for line in rf.readlines():
        if line.startswith('FN') or not_1_line:      #姓名   此处存在多行的情况
            if len(line)>1:
                if line[-2]=='=': #说明不止1行
                    not_1_line=1
                    fn+=line[:-2]       #删除最后两位——'=\n'
                    continue
                else:               #到底了
                    not_1_line=0
            fn+=line.strip('\n')
            line=fn
            fn=''       #清空
            pos=line.find(':')
            qp_origin= line[pos+1:].strip().encode()      #b'=E5=95=8A=6C'
            content[0]=quopri.decodestring(qp_origin).decode('utf-8')

        elif line.startswith('TEL'):
            if tel > 2:                 #最多三个电话
                continue
            pos = line.find(':')
            content[tel + 1] = line[pos + 1:].strip()
            tel = tel + 1
        elif line.startswith('END'):
            str = '\t'.join(content) + '\n'      #'gbk' codec can't encode character '\u270c' in position 5: illegal multibyte sequence，存在特殊字符
                                                #将编码方式修改为UTF-8——open默认编解码非utf-8
            print(str)
            wf.write(str)
            # if 'a妹' in str:                #此处添加筛选条件
            #     wf.write(str)
            content = ['', '', '', '']
            tel = 0
