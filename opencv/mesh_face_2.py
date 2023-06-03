import cv2
import mediapipe as mp

# Initialize MediaPipe FaceMesh
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

video = cv2.VideoCapture('output_2.mp4')

while cv2.waitKey(1) != 27:
    ret, frame = video.read()

    if not ret:
        break

    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run face detection
    results = mp_face_mesh.process(frame_rgb)

    # Detect faces and apply mosaic effect
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get face landmarks coordinates
            landmarks = face_landmarks.landmark

            # Calculate face bounding box
            x_min, x_max, y_min, y_max = float('inf'), float('-inf'), float('inf'), float('-inf')
            for landmark in landmarks:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y

            # Apply mosaic effect to the face region
            face_area = frame[y_min:y_max, x_min:x_max]
            mosaic = cv2.resize(face_area, (8, 8), interpolation=cv2.INTER_LINEAR)
            mosaic = cv2.resize(mosaic, (x_max - x_min, y_max - y_min), interpolation=cv2.INTER_NEAREST)
            frame[y_min:y_max, x_min:x_max] = mosaic

            # Draw face landmarks
            mp_drawing.draw_landmarks(frame, face_landmarks)

    cv2.imshow("frame", frame)

video.release()
cv2.destroyAllWindows()