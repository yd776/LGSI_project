video_path = '/content/laptop_-_61037 (540p).mp4'
output_dir = 'frames/'
os.makedirs(output_dir, exist_ok=True)
cap = cv2.VideoCapture(video_path)
frame_count = 0
while True:
    ret, frame = cap.read()
    if ret:
        frame_count += 1
        frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
    else:
        break

cap.release()
print(f'{frame_count} frames extracted and saved to {output_dir}')