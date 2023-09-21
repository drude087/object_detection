import cv2
from ultralytics import YOLO
import os

model = YOLO('yolov8n.pt')

video_path = r'D:\yoloproject\demo.avi'
output_dir = r'C:\Users\warzo\OneDrive\Desktop\demo\photos'
max_frames = 100


cap = cv2.VideoCapture(video_path)

frame_count = 0

while frame_count < max_frames:
   
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

   
    annotated_frame_filename = os.path.join(output_dir, f'annotated_frame_{frame_count:04d}.jpg')
    cv2.imwrite(annotated_frame_filename, annotated_frame)

    frame_count += 1


cap.release()
print("completed")
