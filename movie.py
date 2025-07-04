import json
from pathlib import Path

from moviepy import AudioFileClip, ColorClip, CompositeVideoClip, ImageClip, TextClip, VideoFileClip, clips_array, concatenate_videoclips

def generate_movie():
  posts = json.loads(Path('posts/data.json').read_text())['posts']

  for post_index, post in enumerate(posts):
    audio_clip = AudioFileClip(f'posts/{post_index}/title.wav')
    image_clip = ImageClip(f'posts/{post_index}/post_screenshot.png', duration=audio_clip.duration)
    image_clip = image_clip.with_audio(audio_clip)
    bg_clip = ColorClip(size=(1080, 1920), color=(0, 0, 0, 0))
    bg_clip = bg_clip.with_duration(image_clip.duration)
    image_clip = image_clip.resized(width=1000)
    image_clip = image_clip.with_position(('center', 'center'))
    image_with_bg_clip = CompositeVideoClip([bg_clip, image_clip])
    clips = [image_with_bg_clip]

    for comment_index, comment in enumerate(post['comments']):
      comment_audio_clip = AudioFileClip(f'posts/{post_index}/comments/{comment_index}.wav')
      comment_text_clip = TextClip(font = 'Roboto-Regular.ttf', text = comment, method='caption', color=(255, 255, 255, 255), duration=comment_audio_clip.duration, font_size=64, size=(1080, 1920), text_align='center', stroke_color=(0, 0, 0, 255), stroke_width=10)
      comment_text_clip = comment_text_clip.with_audio(comment_audio_clip)  
      clips.append(comment_text_clip)

    comments_clip = concatenate_videoclips(clips)
    parkour_clip = VideoFileClip('parkour.mp4')
    parkour_clip = parkour_clip.resized((1080, 1920))
    parkour_clip = parkour_clip.with_audio(comments_clip.audio)
    parkour_clip = parkour_clip.with_duration(comments_clip.duration)
    final_clip = CompositeVideoClip([parkour_clip, comments_clip])
    final_clip.write_videofile(f'videos/{post_index}.mp4', fps=60, threads=4)
