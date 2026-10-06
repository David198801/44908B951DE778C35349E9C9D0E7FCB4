# ffmpeg生成粉红噪声、褐色噪声

## 单声道64k aac褐色噪声20h

ffmpeg -f lavfi -i "anoisesrc=sample_rate=44100:duration=72000:color=brown" -ac 1 -c:a aac -b:a 64k brown_20h.m4a

## 单声道64k aac粉红噪声20h
ffmpeg -f lavfi -i "anoisesrc=sample_rate=44100:duration=72000:color=pink" -ac 1 -c:a aac -b:a 64k pink_20h.m4a

## 单声道64k mp3褐色噪声20h
ffmpeg -f lavfi -i "anoisesrc=sample_rate=44100:duration=72000:color=brown" -ac 1 -c:a libmp3lame -b:a 64k brown_20h.mp3

## 单声道64k mp3粉红噪声20h
ffmpeg -f lavfi -i "anoisesrc=sample_rate=44100:duration=72000:color=pink" -ac 1 -c:a libmp3lame -b:a 64k pink_20h.mp3