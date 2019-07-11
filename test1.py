from functools import reduce

def str2num(s):
    # if '.' in s:
    #     return float(s)
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    try:                                        #对怀疑的代码进行用try进行测试
       r = calc('99 + 88 + 7.6')
       print('99 + 88 + 7.6 =', r)
    except Exception as e:
       print("Error:",e)

main()
