from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 创建保存视频的文件夹
if not os.path.exists("videos"):
    os.makedirs("videos")
# 确保 text 文件夹存在
if not os.path.exists("text"):
    os.makedirs("text")

@app.route('/api/video', methods=['POST'])
def stream_video():
    video = request.files.get('video')
    if video:
        video_path = os.path.join("videos", "streamed_video.mp4")
        with open(video_path, "ab") as f:
            f.write(video.read())  # 追加写入，保持流式存储
        return "Video chunk received", 200
    return "No video received", 400

@app.route('/api/text', methods=['GET'])
def get_text():
    """
    读取 text/streamed_text.txt 文件内容并返回
    """
    file_path = os.path.join("text", "streamed_text.txt")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content, 200, {"Content-Type": "text/plain; charset=utf-8"}
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
