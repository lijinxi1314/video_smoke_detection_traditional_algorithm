
from pywt import dwt2, idwt2
import matplotlib.pyplot as plt

def wavelet(img,w,h):
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    # img_y = img[:, :, 0]

    coeffs2 = dwt2(img, 'bior1.3')
    LL, (LH, HL, HH) = coeffs2

    fig = plt.figure(figsize=(12, 3))
    c=0
    for i, a in enumerate([LH, HL, HH]):
        ax = fig.add_subplot(1, 3, i + 1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)

        b = abs(sum(map(sum, a)))
        # print("b", b)
        c= b*b+c
    # print("c",c)
    c=c/(w*h)
    return c

