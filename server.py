from flask import Flask, request
import os

app = Flask(__name__)

# 创建保存视频的文件夹
if not os.path.exists("videos"):
    os.makedirs("videos")

@app.route('/api/stream', methods=['POST'])
def stream():
    video = request.files.get('video')
    if video:
        video_path = os.path.join("videos", "streamed_video.mp4")
        with open(video_path, "ab") as f:
            f.write(video.read())  # 追加写入，保持流式存储
        return "Video chunk received", 200
    return "No video received", 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)