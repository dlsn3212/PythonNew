num = 1
prev = 0
cur =  1

while num < 10:
    nexts = cur + prev
    print("%2d %d"%(num,nexts))
    prev = cur
    cur = nexts
    num += 1