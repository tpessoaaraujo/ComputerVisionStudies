import cv2
import matplotlib.pyplot as plt

cb_img = cv2.imread("assets/checkerboard_color.png")
coke_img = cv2.imread("assets/coca-cola-logo.png")

# Usando o método imshow() do Matplotlib
plt.imshow(cb_img)
plt.title("Imagem exibida usando Matplotlib")
plt.show()

# Usando o método imshow() do OpenCV por 8seg
window1 = cv2.namedWindow("Window 1")
cv2.imshow("Window 1", cb_img)
cv2.waitKey(8000)
cv2.destroyWindow("Window 1")

# Usando o método imshow() do OpenCV por 8seg
window2 = cv2.namedWindow("Window 2")
cv2.imshow("Window 2", coke_img)
cv2.waitKey(8000)
cv2.destroyWindow("Window 2")

# Usando o método imshow() do OpenCV enquanto nenhuma tecla é pressionada
window3 = cv2.namedWindow("Window 3")
cv2.imshow("Window 3", cb_img)
cv2.waitKey(0)
cv2.destroyWindow("Window 3")

window4 = cv2.namedWindow("Window 4")

Alive = True
while Alive:
    # Usando o método imshow() do OpenCV enquanto a tecla "q" não é pressionada
    cv2.imshow("Window 4", coke_img)
    keypress = cv2.waitKey(1)
    if keypress == ord("q"):
        Alive = False
cv2.destroyWindow("Window 4")

cv2.destroyAllWindows()
stop = 1