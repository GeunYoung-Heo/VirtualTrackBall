import pyautogui
import keyboard

# 커서 이동 단위 (픽셀)
move_distance = 20

# 콜백 함수 정의
def move_up():
    pyautogui.move(0, -move_distance)  # Y축 음수 방향으로 이동 (위로)
    
def move_down():
    pyautogui.move(0, move_distance)  # Y축 양수 방향으로 이동 (아래로)
    
def move_left():
    pyautogui.move(-move_distance, 0)  # X축 음수 방향으로 이동 (왼쪽으로)
    
def move_right():
    pyautogui.move(move_distance, 0)  # X축 양수 방향으로 이동 (오른쪽으로)

# 키보드 이벤트에 콜백 함수 연결
keyboard.add_hotkey('w', move_up)     # 'w'를 누르면 위로 이동
keyboard.add_hotkey('s', move_down)   # 's'를 누르면 아래로 이동
keyboard.add_hotkey('a', move_left)   # 'a'를 누르면 왼쪽으로 이동
keyboard.add_hotkey('d', move_right)  # 'd'를 누르면 오른쪽으로 이동

# 'q'를 누르면 프로그램 종료
keyboard.add_hotkey('q', lambda: print("프로그램 종료") or exit())

# 프로그램이 종료될 때까지 대기 (키보드 이벤트 콜백 처리)
keyboard.wait('q')  # 'q' 키를 누르면 프로그램이 종료됨