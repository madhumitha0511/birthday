from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/memorywall')
def abt():
    # List of image filenames
    photos = [f"{i}.jpg" for i in range(1,10)]  # 1.jpg to 27.jpg
    return render_template('memory-vault.html', photos=photos)

@app.route('/wishwall')
def wish_wall():
    video_wishes = [
        {"name": "AMMA", "video": "amma.mp4"},
        {"name": "Appa", "video": "appa.mp4"},
        {"name": "Thata & Patti", "video": "thata.mp4"},
        {"name": "Chithi", "video": "chithi.mp4"},
        {"name": "Papa", "video": "papa.mp4"},
       
    ]
    return render_template('wish-wall.html', video_wishes=video_wishes)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
