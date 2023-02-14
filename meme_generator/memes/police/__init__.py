from typing import List
from pathlib import Path
from pil_utils import BuildImage

from meme_generator import add_meme


img_dir = Path(__file__).parent / "images"


def police(images: List[BuildImage], texts, args):
    img = images[0].convert("RGBA").square().resize((245, 245))
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(img, (224, 46), below=True)
    return frame.save_jpg()


def police1(images: List[BuildImage], texts, args):
    img = (
        images[0]
        .convert("RGBA")
        .resize((60, 75), keep_ratio=True)
        .rotate(16, expand=True)
    )
    frame = BuildImage.open(img_dir / "1.png")
    frame.paste(img, (37, 291), below=True)
    return frame.save_jpg()


add_meme("police", ["出警"], police, min_images=1, max_images=1)
add_meme("police1", ["警察"], police1, min_images=1, max_images=1)