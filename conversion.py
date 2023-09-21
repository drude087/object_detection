from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_avi_to_mp4(input_path, output_path):
    video = VideoFileClip(input_path)
    video.write_videofile(output_path, codec="libx264", audio=False)

# Provide the absolute path for the input AVI file and the desired output MP4 file
input_path = r'D:\yoloproject\demo.avi'
output_path = r'C:\Users\warzo\OneDrive\Desktop\demo\photos\video.mp4'  # Provide a complete file path

# Convert AVI to MP4
convert_avi_to_mp4(input_path, output_path)
