from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

# 動画1の読み込み
clip1 = VideoFileClip('movie1.mp4')
# 20秒までの範囲を切り出す
clip1_20s = clip1.subclip(0, 20)

# 動画2の読み込み
clip2 = VideoFileClip('movie2.mp4')

# クロスディゾルブの時間設定
crossfade_duration = 2.0

# クロスディゾルブを適用した動画1の終了部分
clip1_end = clip1_20s.fadeout(crossfade_duration)

# クロスディゾルブを適用した動画2の開始部分
clip2_start = clip2.fadein(crossfade_duration)

# BGMの読み込み
bgm = AudioFileClip('bgm.mp3')
# BGMをトリミング
bgm_trimmed = bgm.subclip(0, 30)

# フェードインとフェードアウトの時間設定
fade_duration = 2.0
# BGMにフェードインとフェードアウトを適用させる
bgm_faded = bgm_trimmed.audio_fadein(fade_duration).audio_fadeout(fade_duration)

# 音量を50%にする
bgm_adjusted = bgm_faded.volumex(0.5)
# BGMを動画1に追加
clip1_end = clip1_end.set_audio(bgm_adjusted)

# 動画の連結
final_clip = concatenate_videoclips([clip1_end, clip2_start])

# フェードインとフェードアウトをいれる
final_clip = final_clip.fadein(fade_duration).fadeout(fade_duration)

# テキストの作成
text_clip = TextClip('MOVIE-SNS', fontsize=40, color='#ebebeb', bg_color='#2b2b2b', size=(final_clip.w, 120), font=font_family)
# フェードインを適用
text_clip = text_clip.set_position(('center', 'center')).set_start(10).set_duration(10)  # 10秒目から5秒間表示
text_clip = text_clip.fadein(fade_duration).fadeout(fade_duration)

# テキストを動画に追加
final_clip_with_text = CompositeVideoClip([final_clip, text_clip])

# 動画を保存
final_clip_with_text.write_videofile('output_video_with_text_and_transition.mp4', codec='libx264', audio_codec='aac')
