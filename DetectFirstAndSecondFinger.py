import cv2
import mediapipe as mp
import time

# MediaPipe의 손 인식 모듈 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 웹캠 초기화
cap = cv2.VideoCapture(0)

# FPS 계산을 위한 초기 시간 설정
prev_time = 0

# Hands 모듈 설정
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # BGR 이미지를 RGB로 변환
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # 손 인식
        results = hands.process(image)

        # 이미지를 다시 쓰기 가능 상태로 설정
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 인식된 손이 있다면 프레임에 그리기
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 모든 손 랜드마크 그리기
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # 검지 끝의 좌표 얻기 (랜드마크 인덱스 8)
                index_finger_tip = hand_landmarks.landmark[8]
                h, w, c = image.shape  # 이미지의 높이, 너비 가져오기
                cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)  # 좌표를 픽셀 값으로 변환

                # 좌표를 이미지에 그리기
                cv2.circle(image, (cx, cy), 10, (0, 255, 0), -1)
                cv2.putText(image, f'Index Tip: ({cx}, {cy})', (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)

                # 엄지 끝의 좌표 얻기 (랜드마크 인덱스 4)
                thumb_tip = hand_landmarks.landmark[4]
                h, w, c = image.shape  # 이미지의 높이, 너비 가져오기
                cx, cy = int(thumb_tip.x * w), int(thumb_tip.y * h)  # 좌표를 픽셀 값으로 변환

                # 좌표를 이미지에 그리기
                cv2.circle(image, (cx, cy), 10, (0, 255, 0), -1)
                cv2.putText(image, f'Thumb Tip: ({cx}, {cy})', (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)



        # FPS 계산
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        # FPS를 프레임에 표시
        cv2.putText(image, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # 프레임 출력
        cv2.imshow('Hand Detection', image)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
