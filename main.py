from flask import Flask, request, jsonify
import pygame
import os

app = Flask(__name__)

# 初始化 pygame 混音器
pygame.mixer.init()

# 設置音檔路徑
SOUND_FILES = {
    'hey-michael': '/Users/criz.chien/extremedata/tmp/sound/add_money.mp3',
    'alert': '/Users/criz.chien/extremedata/tmp/sound/alert.mp3',
    'welcome': '/Users/criz.chien/extremedata/tmp/sound/welcome.mp3'
}

@app.route('/hey-michael', methods=['PUT'])
def webhook():
    try:
        # 獲取請求中的 JSON 數據
        data = request.json
        sound_key = data.get('sound_key')

        if sound_key and sound_key in SOUND_FILES:
            sound_path = SOUND_FILES[sound_key]

            # 播放音檔
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

            return jsonify({'status': 'success', 'message': f'Playing sound: {sound_key}'})
        else:
            return jsonify({'status': 'error', 'message': 'Invalid sound key'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000)

