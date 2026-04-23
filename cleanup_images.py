import os
import re
from PIL import Image

def cleanup_images():
    html_path = 'index.html'
    css_path = 'css/style.css'
    images_dir = 'images'
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
        
    used_images = set(re.findall(r'images/([^\"\'\s\)]+)', html + css))
    all_images = set(os.listdir(images_dir))
    
    unused_images = all_images - used_images
    print("Unused images:", unused_images)
    
    for img in unused_images:
        path = os.path.join(images_dir, img)
        os.remove(path)
        print(f"Deleted {img}")
        
    used_images_paths = [os.path.join(images_dir, img) for img in used_images if os.path.exists(os.path.join(images_dir, img))]
    
    for img_path in used_images_paths:
        file_size = os.path.getsize(img_path)
        filename = os.path.basename(img_path)
        name, ext = os.path.splitext(filename)
        
        if ext.lower() not in ['.webp'] or file_size > 300 * 1024:
            print(f"Processing {filename} (Size: {file_size/1024:.1f} KB)")
            with Image.open(img_path) as img:
                webp_path = os.path.join(images_dir, f"{name}.webp")
                max_dim = 1200
                if img.width > max_dim or img.height > max_dim:
                    img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
                img.save(webp_path, "WEBP", quality=80)
                
            print(f"Saved {name}.webp")
            
            if ext.lower() != '.webp':
                html = html.replace(f"images/{filename}", f"images/{name}.webp")
                css = css.replace(f"images/{filename}", f"images/{name}.webp")
                os.remove(img_path)
                print(f"Removed old file {filename}")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

if __name__ == '__main__':
    cleanup_images()
