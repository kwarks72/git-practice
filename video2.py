import cv2

cap=cv2.VideoCapture("video1.mp4")
if not cap.isOpened():
    print("비디오 파일이 열리지 않았습니다")

fps=cap.get(cv2.CAP_PROP_FPS)
delay=round(1000/fps)

while True:
    ret, frame= cap.read()
    if not ret:
        break
    inversed= ~frame
    cv2.imshow("frame", frame)
    cv2.imshow("inversed",inversed)

    if cv2.waitKey(delay)==27:
        break
cap.release()
cv2.destroyAllWindows()
