# color-captcha
Dynamically generated, AI-resistant captcha images. 

![color-captcha](https://raw.githubusercontent.com/stefs304/clockcaptcha/master/color-captcha.png)

*Can you tell what time it is? AI can't.*

Color-captcha uses higher-order shapes to hide the information from an AI. 
AI can recognize that the image is made up of triangles, squares and circles.
However, it cannot recognize that these shapes form more complex higher-order shapes, in this case numbers. 
The numbers, therefore, remain hidden in plain sight.
The human eye, on the other hand, should be able to see the numbers with very little effort. 

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
Same usage as ClockCaptcha except it can generate arbitrary number of 
digits, and is not in the clock format, just plain digits. 

```python
from color_captcha import DigitsCaptcha

captcha = DigitsCaptcha(digits=5) # number of digits
captcha.save_image('digits.png')
captcha.verify('12345')
captcha.generate_new()
```

#### Size parameter
Both ClockCaptcha and DigitsCaptcha have the `size` parameter, which changes the size of the image.
Below relative values in pixels for the ClockCaptcha image. 
DigitsCaptcha images vary in width depending on the number of digits. 

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

\*Percent increase of non-dominant colors in a pixel.
To turn off color variation set these parameters to 0.

```python
from color_captcha.config import Config

Config.colors = ['#ec7063', '...']  # minimum 3 colors required
Config.base_variation_percent = 0.30
Config.content_variation_percent = 0.15
```

⚠️ **Important to consider:** 
Difference in color variation between background and numbers can make the numbers stand out more. 
If this difference is too great the AI may pick up on that and be able to detect numbers. 
The default values of 0.15 and 0.30 should be good for now, but may need to change in the future. 

