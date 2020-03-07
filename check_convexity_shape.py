
import itertools
import cv2 as cv

def get_line_continus_zero_number(draw,x,y,w,h):
    sum=0
    ######################   平行   ######################################

    a1 = [len(list(v)) for k, v in itertools.groupby(draw[y + h // 6][x:x + w]) if k == 0]
    # if len(a1):
    #     print("平行的第1条线：%d" % (y + h // 6)+' 0连续出现的最大次数为：%d' % max(a1))
    # else:
    #     print("平行的第1条线 0连续出现的最大次数为0 ")
    cv.line(draw, (x, y + h // 6), (x + w, y + h // 6), (0, 255, 54), 1, 4)
    if len(a1):
        if max(a1)>3:
            sum=sum+1

    a2 = [len(list(v)) for k, v in itertools.groupby(draw[y + 2*h // 6][x:x + w]) if k == 0]
    # if len(a2):
    #     print("平行的第2条线：%d" % (y + 2*h // 6)+' 0连续出现的最大次数为：%d' % max(a2))
    # else:
    #     print("平行的第2条线 0连续出现的最大次数为0 ")
    cv.line(draw, (x, y + 2*h // 6), (x + w, y + 2*h // 6), (0, 255, 54), 1, 4)
    if len(a2):
        if max(a2)>3:
            sum=sum+1


    a3 = [len(list(v)) for k, v in itertools.groupby(draw[y + 3*h // 6][x:x + w]) if k == 0]
    # if len(a3):
    #     print("平行的第3条线：%d" % (y + 3*h // 6)+'  0连续出现的最大次数为：%d' % max(a3))
    # else:
    #     print("平行的第3条线 0连续出现的最大次数为0 ")
    cv.line(draw, (x, y + 3*h // 6), (x + w, y + 3 * h // 6), (0, 255, 54), 1, 4)
    if len(a3):
        if max(a3)>3:
            sum=sum+1

    a4 = [len(list(v)) for k, v in itertools.groupby(draw[y + 4*h // 6][x:x + w]) if k == 0]
    # if len(a4):
    #     print("平行的第4条线：%d" % (y + 4*h // 6)+'  0连续出现的最大次数为：%d' % max(a4))
    # else:
    #     print("平行的第3条线 0连续出现的最大次数为0 ")
    cv.line(draw, (x, y + 4 * h // 6), (x + w, y + 4 * h // 6), (0, 255, 54), 1, 4)
    if len(a4):
        if max(a4)>3:
            sum=sum+1


    a5 = [len(list(v)) for k, v in itertools.groupby(draw[y + 5*h // 6,x:x + w]) if k == 0]
    # if len(a5):
    #     print("平行的第5条线：%d" % (y + 5*h // 6)+'  0连续出现的最大次数为：%d' % max(a5))
    # else:
    #     print("平行的第5条线 0连续出现的最大次数为0 ")
    cv.line(draw, (x, y + 5 * h // 6), (x + w, y + 5* h // 6), (0, 255, 54), 1, 4)
    if len(a5):
        if max(a5)>3:
            sum=sum+1



    ######################   垂直    ######################################
    b1=[len(list(v)) for k, v in itertools.groupby(draw[y:y+h,x+w//6]) if k == 0]
    # print("垂直的第1条线：%d" % (x+w//6)+' 0连续出现的最大次数为：%d' % max(b1))
    cv.line(draw, (x+w//6, y ), (x+w//6, y + h), (0, 255, 54), 1, 4)
    if max(b1)>3:
        sum=sum+1

    b2=[len(list(v)) for k, v in itertools.groupby(draw[y:y+h,x+2*w//6]) if k == 0]
    # print("垂直的第2条线：%d" % (x+2*w//6)+' 0连续出现的最大次数为：%d' % max(b2))
    cv.line(draw, (x+ 2*w//6, y ), (x+ 2*w//6, y + h), (0, 255, 54), 1, 4)
    if max(b2)>3:
        sum=sum+1

    b3=[len(list(v)) for k, v in itertools.groupby(draw[y:y+h,x+3*w//6]) if k == 0]
    # print("垂直的第3条线：%d" % (x+3*w//6)+' 0连续出现的最大次数为：%d' % max(b3))
    cv.line(draw, (x+3*w//6, y ), (x+3*w//6, y + h), (0, 255, 54), 1, 4)
    if max(b3)>3:
        sum=sum+1

    b4=[len(list(v)) for k, v in itertools.groupby(draw[y:y+h,x+4*w//6]) if k == 0]
    # print("垂直的第4条线：%d" % (x+4*w//6)+' 0连续出现的最大次数为：%d' % max(b4))
    cv.line(draw, (x+4*w//6, y ), (x+4*w//6, y + h), (0, 255, 54), 1, 4)
    if max(b4)>3:
        sum=sum+1

    b5=[len(list(v)) for k, v in itertools.groupby(draw[y:y+h,x+5*w//6]) if k == 0]
    # print("垂直的第5条线：%d" % (x+w//6)+' 0连续出现的最大次数为：%d' % max(b5))
    cv.line(draw, (x+5*w//6, y ), (x+5*w//6, y + h), (0, 255, 54), 1, 4)
    if max(b5)>3:
        sum=sum+1

    # print("line sum",sum)
    # 参数可调节
    if sum>3:
        # print("1 , convexity  line sum %d" %(sum))
        return 1
    else:
        # print("0 , convexity  line sum %d" % (sum))
        return 0
