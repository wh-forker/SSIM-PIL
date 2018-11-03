# SSIM-PIL
Structural similarity algorithm with compatibility to PIL.

## Installation
`python3 -m pip install SSIM-PIL`

## Usage Example
Usage:
```python

from SSIM_PIL import compare_ssim
from PIL import Image

image1 = Image.open(path)
image2 = Image.open(path)
value = compare_ssim(image1, image2)
print(value)

```