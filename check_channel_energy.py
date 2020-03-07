
import cv2

def U(input):
    input = cv2.cvtColor(input, cv2.COLOR_BGR2Luv)
    l, u, v = cv2.split(input)
    return u

def V(input):
    input = cv2.cvtColor(input, cv2.COLOR_BGR2Luv)
    l, u, v = cv2.split(input)
    return v

def check_channel_energy(img1,img2):
    image1_U = U(img1)
    image1_V = V(img1)

    image2_U = U(img2)
    image2_V = V(img2)

    # image1 为第一帧图片， img2为当前帧 由于有烟雾出现，所以当前帧的u,v 通道值会减小， 所以dis a-b >0 说明有烟雾
    a = sum(map(sum, image1_U))
    b = sum(map(sum, image2_U))

    c = sum(map(sum, image1_V))
    d = sum(map(sum, image2_V))

    if a-b>0 and c-d>0 :
        # print("1 there has smoke", a-b,c-d)
        return 1
    else:
        # print("0 there has no smoke", a-b, c-d)
        return 0
