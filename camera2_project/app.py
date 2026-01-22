from flask import Flask, render_template, request
import base64, time, os

app = Flask(__name__)

if not os.path.exists("photos"):
    os.mkdir("photos")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.form['image']
    image_data = data.split(",")[1]

    filename = f"photos/photo_{int(time.time()*1000)}.png"
    with open(filename, "wb") as f:
        f.write(base64.b64decode(image_data))

    return "ok"

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

