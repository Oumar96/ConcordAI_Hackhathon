import cv2

img = cv2.imread ("C:\\Users\\oumar\\OneDrive\\Documents\\ConUhack AI\\Arthur\\venv\\Test\\ronaldo.jpg")

resized = cv2.resize(img, (600, 600) )

cv2.imshow("Legend", resized)
cv2.waitKey(0)

cv2.destroyAllWindows()