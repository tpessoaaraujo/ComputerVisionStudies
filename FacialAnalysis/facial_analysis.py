import cv2
import mediapipe as mp

mp_face = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

face = mp_face.FaceMesh()

cam = cv2.VideoCapture(0)
resolution_x, resolution_y = 1280, 720

cam.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution_y)

while True:
    success, frame = cam.read()
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face.process(frame_rgb)
    
    if result.multi_face_landmarks:
        try:
            for face_landmarks in result.multi_face_landmarks:
                mp_drawing.draw_landmarks(frame, face_landmarks, mp_face.FACEMESH_CONTOURS,
                    landmark_drawing_spec = mp_drawing.DrawingSpec(color=(0,0,255), thickness=1, circle_radius=1),
                    connection_drawing_spec = mp_drawing.DrawingSpec(thickness=1))
        except:
            pass
            
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(10) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()