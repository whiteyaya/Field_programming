
cdict = {1: u'', 2: u'拾', 3: u'佰', 4: u'仟'}
xdict = {1: u'', 2: u'万', 3: u'亿', 4: u'兆'}  # 数字标识符
gdict = {0: u'零', 1: u'壹', 2: u'贰', 3: u'叁', 4: u'肆', 5: u'伍', 6: u'陆', 7: u'柒', 8: u'捌', 9: u'玖'}

def csplit(cdata):  # 拆分函数，将整数字符串拆分成[亿，万，仟]的list
    g = len(cdata) % 4
    csdata = []
    lx = len(cdata) - 1
    if g > 0:
        csdata.append(cdata[0:g])
    k = g
    while k <= lx:
        csdata.append(cdata[k:k + 4])
        k += 4
    return csdata

def cschange(cki):  # 对[亿，万，仟]的list中每个字符串分组进行大写化再合并
    lenki = len(cki)
    i = 0
    lk = lenki
    chk = u''
    for i in range(lenki):
        if int(cki[i]) == 0:
            if i < lenki - 1:
                if int(cki[i + 1]) != 0:
                    chk = chk + gdict[int(cki[i])]
        else:
            chk = chk + gdict[int(cki[i])] + cdict[lk]
        lk -= 1
    return chk

def mysmall2big(data):
    cdata = str(data).split('.')
    cki = cdata[0]
    if len(cdata) == 1:
        i = 0
        chk = u''
        cski = csplit(cki)  # 分解字符数组[亿，万，仟]三组List:['0000','0000','0000']
        ikl = len(cski)  # 获取拆分后的List长度
        # 大写合并
        for i in range(ikl):
            if cschange(cski[i]) == '':  # 有可能一个字符串全是0的情况
                chk = chk + cschange(cski[i])  # 此时不需要将数字标识符引入
            else:
                chk = chk + cschange(cski[i]) + xdict[ikl - i]  # 合并：前字符串大写+当前字符串大写+标识符
        chk = chk + u''
    else:
        i = 0
        chk = u''
        cski = csplit(cki)  # 分解字符数组[亿，万，仟]三组List:['0000','0000','0000']
        ikl = len(cski)  # 获取拆分后的List长度
        # 大写合并
        for i in range(ikl):
            if cschange(cski[i]) == '':  # 有可能一个字符串全是0的情况
                chk = chk +cschange(cski[i])  # 此时不需要将数字标识符引入
            else:
                chk = chk + cschange(cski[i]) +xdict[ikl - i]  # 合并：前字符串大写+当前字符串大写+标识符
    return chk
