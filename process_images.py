import os
from PIL import Image

src_dir = r"C:\Users\TM-PC\.gemini\antigravity\brain\119afb7b-0d20-4fbf-8d54-53eeb5cfdff3"
dest_dir = r"d:\antigravity\business_application\ビギナー講座\beginner3\images"

files = [
    ("media__1776941897197.jpg", "instructor_profile_new.webp", 600),
    ("media__1776941948463.jpg", "gallery_cake1.webp", 800),
    ("media__1776941977419.jpg", "gallery_cake2.webp", 800),
    ("media__1776942009540.jpg", "gallery_instructor.webp", 800),
    ("media__1776942032025.jpg", "gallery_cake3.webp", 800)
]

os.makedirs(dest_dir, exist_ok=True)

for src_name, dest_name, max_size in files:
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    
    if os.path.exists(src_path):
        with Image.open(src_path) as img:
            img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            img.save(dest_path, "WEBP", quality=85)
        print(f"Saved: {dest_path}")
    else:
        print(f"File not found: {src_path}")
