import cv2

# 웹캠 초기화 (0은 기본 웹캠 장치를 의미)
cap = cv2.VideoCapture(0)

while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 제대로 읽혔는지 확인
    if not ret:
        print("Failed to grab frame")
        break

    # 프레임을 윈도우에 출력
    cv2.imshow('Webcam Feed', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제 및 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
