import cv2
import sys

woman = cv2.VideoCapture("woman.mp4")
raining = cv2.VideoCapture("raining.mp4")

if not woman.isOpened() or not raining.isOpened():
    print("영상이 열리지 않습니다")
    sys.exit()

while True:
    # 여자 영상 읽기
    ret, woman_frame = woman.read()
    if not ret:
        print("woman 프레임 종료")
        break

    # 비 영상 읽기
    ret2, raining_frame = raining.read()
    if not ret2:
        print("raining 다시 시작")
        raining.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # 크기 맞추기
    raining_frame = cv2.resize(
        raining_frame,
        (woman_frame.shape[1], woman_frame.shape[0])
    )

    # HSV 변환
    hsv = cv2.cvtColor(woman_frame, cv2.COLOR_BGR2HSV)

    # 초록색 마스크
    mask = cv2.inRange(hsv, (50,150,0), (80,255,255))

    # 결과 복사본 만들기
    dst = woman_frame.copy()

    # 합성
    cv2.copyTo(raining_frame, mask, dst)

    # 출력
    cv2.imshow("woman", woman_frame)
    cv2.imshow("mask",mask)
    cv2.imshow("chroma", dst)

    if cv2.waitKey(30) == 27:
        break

woman.release()
raining.release()
cv2.destroyAllWindows()