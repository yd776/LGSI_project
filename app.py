from flask import Flask, render_template, request
import os
import cv2


app = Flask(__name__)



@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    videofile= request.files['videofile']
    image_path = "./images/" + videofile.filename
    videofile.save(image_path)
    print(image_path)
    video_path = image_path
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



    

    return render_template('index.html')



if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
