# importing dependencies
import cv2
import face_recognition
# from simple_facerec import SimpleFacerec

img1 = cv2.imread("imgs/duterte.jpg")
rgb_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]


img2 = cv2.imread("imgs/duterte2.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]
# compare the two images
result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)

# Display image that you want to compare
cv2.imshow("Image", img1)
cv2.imshow("Image 2", img2)
# prevents terminating the program from running after initializing it
cv2.waitKey(0)
