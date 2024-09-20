# color-captcha
Dynamically generated, AI-resistant captcha images. 

![color-captcha](https://raw.githubusercontent.com/stefs304/clockcaptcha/master/color-captcha.png)

*Can you tell what time it is? AI can't.*

Color-captcha uses high-order shapes to hide meaningful content from an AI. 
AI can recognize that the image is made up of triangles, squares and circles. 
However, it cannot distinguish higher-order shapes that appear in the image. 
Variable, randomized colors make this task even more difficult for the machine
as it observes RGB layers separately. 
To the human eye, however, the numbers are clearly visible. 

Features:
* `ClockCaptcha` and `DigitsCaptcha` generators.
* Decently performant: can generate 100 images in ~0.8 seconds.
* Configurable (base colors, color variation).

### Installation

```shell
pip install color-captcha
```

### Usage

#### ClockCaptcha

```python
from color_captcha import ClockCaptcha

captcha = ClockCaptcha(clock_mode=12, color_mode='rgb') 
# 12 or 24-hour mode
# rgb or grayscale color_mode

# current captcha value
print(captcha.value)

captcha.save_image('my_captcha.png') 
# if no extension, set format explicitly
captcha.save_image('my_captcha', format='png')

# verify the guessed value
captcha.verify('0645') 
# returns True/False

# create new captcha
captcha.generate_new()
captcha.save_image('new_captcha.png')
```

#### DigitsCaptcha
Follows the same usage as ClockCaptcha except it can generate arbitrary number of 
digits, and is not in the clock format.

```python
from color_captcha import DigitsCaptcha

captcha = DigitsCaptcha(digits=5) # number of digits
captcha.save_image('digits.png')
captcha.verify('12345')
captcha.generate_new()
```

#### Size parameter
Both ClockCaptcha and DigitsCaptcha have a `size` parameter. 
This parameter changes the size of the image.
Below are size parameter values and corresponding pixel values of the ClockCaptcha image.
DigitsCaptcha varies in pixel size. 

ClockCaptcha sizes:

| size            | width (pixels) | height (pixels) |
|-----------------|----------------|-----------------|
| 1               | 190            | 65              |
| 2               | 380            | 130             |
| **3 (default)** | **570**        | **195**         |
| 4               | 760            | 260             |
| ...             | ...            | ...             | 

### Changing configuration
Configuration changes are applied globally.
* `colors`: list of base colors in hex format (full 6 characters required).
* `base_variation_percent`: max \*variation of the color in the background.  
* `content_variation_percent`: max \*variation of colors of the numbers.
be
\* Variation percent means the color will be modified by percentage of the original color value.
Setting the variation percent to 0 means the base colors will remain unchanged.

```python
from color_captcha.config import Config

Config.colors = ['#ec7063', '...']  # minimum 3 colors required
Config.base_variation_percent = 0.30
Config.content_variation_percent = 0.15

```

⚠️ **Important to consider:** 
Increased difference in color variation between background and number can make numbers stand out more. 
If this difference is too great the AI may pick up on that and be able to detect numbers. 
The default values of 0.15 and 0.30 should be good for now, but may need to change in the future. 

<hr>

If you have ideas for improvements or notice a deficiency of this captcha please consider 
joining the discussion [here](https://github.com/stefs304/color-captcha/discussions/3).