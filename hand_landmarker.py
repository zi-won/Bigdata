import cv2
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
import numpy as np

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)  # vibrant green

def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.multi_hand_landmarks
    handedness_list = detection_result.multi_handedness
    annotated_image = np.copy(rgb_image)

    if hand_landmarks_list is None:
        return annotated_image

    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx].landmark
        handedness = handedness_list[idx]

        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
        ])

        print(f"Hand {idx + 1} Landmarks:")
        for i, landmark in enumerate(hand_landmarks):
            print(f"Landmark {i + 1}: x={landmark.x}, y={landmark.y}, z={landmark.z}")

        mp.solutions.drawing_utils.draw_landmarks(
            annotated_image,
            hand_landmarks_proto,
            mp.solutions.hands.HAND_CONNECTIONS,
            mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
            mp.solutions.drawing_styles.get_default_hand_connections_style())

        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]
        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN

        if handedness is not None and handedness.classification:
            cv2.putText(annotated_image, f"{handedness.classification[0].label}",
                        (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                        FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    return annotated_image

cap = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    detection_result = hands.process(image)

    annotated_image = draw_landmarks_on_image(frame, detection_result)

    cv2.imshow("Hand Landmarks", annotated_image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
