import cv2 as cv
import numpy as np
import itertools
from skimage import measure
import datetime
from check_channel_energy import check_channel_energy
from get_wavelet_energy import wavelet

from check_convexity_shape import get_line_continus_zero_number


es = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
cap = cv.VideoCapture('/Users/lijinxi/jinxi/code/opticalflow/video/train-2.avi')
fps = cap.get(cv.CAP_PROP_FPS)# 获取视频帧率
print('视频帧率：%d fps' %fps)
frame1 = cap.read()[1]
frame1 = cv.resize(frame1, (960, 540), interpolation=cv.INTER_CUBIC)
prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

# 视频文件输出参数设置
out_fps = 12.0  # 输出文件的帧率
fourcc = cv.VideoWriter_fourcc('M', 'P', '4', '2')
sizes = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
out1 = cv.VideoWriter('/Users/lijinxi/jinxi/code/opticalflow/video/train-2_6.avi', fourcc, out_fps, sizes)
out2 = cv.VideoWriter('/Users/lijinxi/jinxi/code/opticalflow/video/train-2_6.avi_v8.avi', fourcc, out_fps, sizes)


#获得第一帧图像
def get_first_frame():
	success,image = cap.read()
	n=1
	while n < 30:
		success, image = cap.read()
		n+=1

    # cv.imshow("dd.png",image)
	return image


original_image=get_first_frame()
original_image = cv.resize(original_image, (960, 540), interpolation=cv.INTER_CUBIC)

#### rbg 变 ycr-cb通道 求小波能量部分需要
img_o= cv.cvtColor(original_image, cv.COLOR_BGR2YCR_CB)
img_y_o = img_o[:, :, 0]
frame_data_y_o = np.array(img_y_o)

next = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
hsv[..., 0] = ang * 180 / np.pi / 2
hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)

bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)


draw = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
# opening operation
draw = cv.morphologyEx(draw, cv.MORPH_OPEN, kernel)
# threshold split
draw = cv.threshold(draw, 25, 255, cv.THRESH_BINARY)[1]
# cv.imshow("draw",draw)

contours, hierarchy = cv.findContours(draw.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# for one image

def for_one_image():
    i=0
    for c in contours:
        i=i+1
        if cv.contourArea(c) < 300:
            continue

        # 加入判断是否为凸状部分
        (x, y, w, h) = cv.boundingRect(c)

        circle=cv.rectangle(draw, (x, y), (x + w, y + h), (255, 255, 0), 1)

        face = draw[y:y+h, x:x+w]
        print(i, x, y, w, h )

        convexity=get_line_continus_zero_number(draw,x,y,w,h)
        print("ressult",convexity)

        # cv.imshow("a",face)
        cv.waitKey(0)

        # 黑色元素为0 白色为255


        # cv.imshow("threshold",circle)
        # cv.imshow("circle",v1)





i=0   #为第i 帧图像
first_area_pix=55941
dis_area_all=0
while True:
    (ret, frame2) = cap.read()
    frame2 = cv.resize(frame2, (960, 540), interpolation=cv.INTER_CUBIC)
    print(frame2.shape)
    starttime = datetime.datetime.now()

    # cv.imshow('original',frame2)
    next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

    imgYCR_CB = cv.cvtColor(frame2, cv.COLOR_BGR2YCR_CB)
    img_Y = imgYCR_CB[:, :, 0]
    frame_data = np.array(img_Y)

    flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)

    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)


    draw = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
    # opening operation
    draw = cv.morphologyEx(draw, cv.MORPH_OPEN, kernel)
    # threshold split
    draw = cv.threshold(draw, 25, 255, cv.THRESH_BINARY)[1]
    i=i+1
    print(i)
    #
    # # 1 计算烟雾的总面积， 经过运动检测后计算得到目标区域面积序列值，相邻两幅图像的烟雾面积变化量和前n帧图像变化量的平均值判断烟雾
    # smoke_area = sum(map(sum, draw))/255
    #
    # print("draw",smoke_area)
    #
    # dis=smoke_area-first_area_pix
    # first_area_pix=smoke_area
    # print("temp,dis",first_area_pix,dis)
    #
    # dis_area_all=(dis_area_all+dis)/i
    # print("i %d dis_area_all %f"%(i,dis_area_all))


    #接口中使用cv2.findContours()函数来查找检测物体的轮廓。
    # contours 寻找轮廓的图像
    # hierarchy  RETR_EXTERNAL 只检测外轮廓
    contours, hierarchy = cv.findContours(draw.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv.contourArea(c) < 300:
            continue

        (x, y, w, h) = cv.boundingRect(c)

        circle=cv.rectangle(draw, (x, y), (x + w, y + h), (255, 255, 0), 2)

        num=0
        box_data = frame_data [y:y+h, x:x+w]   #当前帧的ychannel

        # print(box_data.shape)
        cv.imshow("optical flow result", circle)

        # cv.imshow("box_uv_data region proposal", box_uv_data)

        # 加入判断是否为凸状部分
        convexity = get_line_continus_zero_number(draw, x, y, w, h)

        num=num+convexity

        # 判断小波能量是否减少部分   1

        wave_now = wavelet(box_data,w,h)   #当前帧

        orignal_data_y = frame_data_y_o[y:y + h, x:x + w]
        wave_background = wavelet(orignal_data_y, w, h)  #背景帧


        # T1wbn(x, y) > wn(x, y) > T2wbn(x, y) 参数可调
        T1 = 1
        T2 = 0.1
        # print("orignal_background" + str(wave_background) + "  wave_ now " + str(wave_now))

        if T1 * wave_background > wave_now and wave_now > T2 * wave_background:
            # print("1 there has smoke orignal_background" +str(wave_background)+"  wave_ now " +str(wave_now))
            # print("1 there has smoke wavelet channel")
            num=num+1
        else:
            # print("0 there has no smoke wavelet channel")
            num=num+0

        ##### 通过u,v channel进行判断

        orignal_data_uv = original_image[y:y + h, x:x + w]  #背景帧区域
        box_uv_data = frame2[y:y + h, x:x + w]  #当前帧的区域
        channel_result = check_channel_energy(orignal_data_uv, box_uv_data)

        num=num+channel_result
        # print("%d channel_check"%(channel_result))
        # print("num",num)
        # print(" ")



        if num>0:
            draw_rec = cv.rectangle(frame2, (x, y), (x + w, y + h), (255, 255, 0), 2)

        cv.imshow("detection result",draw_rec)
        # cv.imwrite("circle.png", circle)
    endtime = datetime.datetime.now()
    dis_time=(endtime-starttime).total_seconds()
    print(dis_time)
    # cv.imshow('frame1', frame2)

    out1.write(bgr)
    out2.write(frame2)

    k = cv.waitKey(200) & 0xff
    if k == 27 or k == ord('q'):
        break
    elif k == ord('s'):
        cv.imwrite('opticalfb.png', frame2)
        cv.imwrite('opticalhsv.png', bgr)
    prvs = next

out1.release()
out2.release()
cap.release()
cv.destroyAllWindows()
