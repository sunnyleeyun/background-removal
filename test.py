from pathlib import Path
from rembg import remove, new_session
from PIL import UnidentifiedImageError

session = new_session()

img_dir = Path('/Users/sunny/Desktop/Computer Vision 30 Projects/Project 16/images')
exts = ('*.jpg', '*.jpeg', '*.png')

for pattern in exts:
    for file in img_dir.glob(pattern):

        # ⛔ skip rembg outputs
        if '.out.' in file.name:
            continue

        output_path = file.parent / f"{file.stem}.out.png"

        try:
            with open(file, 'rb') as i, open(output_path, 'wb') as o:
                o.write(remove(i.read(), session=session))
        except UnidentifiedImageError:
            print(f"Skipping invalid image: {file}")
