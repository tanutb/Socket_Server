import cv2
import mediapipe as mp
from SocketSever import Socket

webcam = cv2.VideoCapture(0)
img = webcam.read()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
)

mp_draw = mp.solutions.drawing_utils

Client = Socket()
Client.client_connect()
while True:
    success, img = webcam.read()    
    image_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    if results.multi_hand_landmarks:

        for hand_landmarks  in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks , mp_hands.HAND_CONNECTIONS)

            #Draw Circle
            height, width, channels = img.shape
            Wrist = hand_landmarks.landmark[8]
            center = tuple(map(int,(Wrist.x * width ,Wrist.y *height)))

            Client.client_send_data(list(center))

            img = cv2.circle(img,center , 20, (255,0,0), 5)

    cv2.imshow("Image Hand Tracking",img)
    if cv2.waitKey(5) & 0xFF == 27:
      break
webcam.release()