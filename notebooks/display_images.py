import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread('assets/checkerboard_color.png')
if cb_img is None:
    print("failed to load checkerboard_color.png")


coke_img = cv2.imread('assets/coca-cola-logo.png')
if coke_img is None:
    print('failed to load coca-cola-logo.png')


# using matplotlib imshow()
plt.imshow(cb_img)
plt.title('matplotlib imshow')
plt.show()

# using openCv imshow, display for 8 sec
window1 = cv2.namedWindow('w1')
cv2.imshow(window1, cb_img)
cv2.waitKey(8000)
cv2.destroyWindow(window1)

# using openCv imshow, display for 8 sec
window2 = cv2.namedWindow('w2')
cv2.imshow(window1, coke_img)
cv2.waitKey(8000)
cv2.destroyWindow(window2)

# using openCv imshow, display until key is pressed
window3 = cv2.namedWindow('w3')
cv2.imshow(window3, cb_img)
cv2.waitKey(0)
cv2.destroyWindow(window3)

window4 = cv2.namedWindow('w4')

while True:
    cv2.imshow(window4, coke_img)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        break

cv2.destroyWindow(window4)

cv2.destroyAllWindows()
