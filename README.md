# color-captcha
Dynamically generated, AI-resistant captcha images. 

![captcha](https://raw.githubusercontent.com/stefs304/clockcaptcha/master/color-captcha.png)

*Can you tell what time it is? AI can't.*

Color-captcha uses higher-order shapes to hide the numbers from an AI. 
AI can recognize that the image is made up of triangles and circles. 
However, it cannot discern higher-order shapes (such as numbers) that appear in the image. 
Variable, randomized colors makes this task even more difficult for the machine
as it observes RGB layers separately. 
The human eye, on the other hand, can spot the numbers easily. 

Features:
* ClockCaptcha and DigitsCaptcha generators
* dynamically generated images
* rgb and grayscale color mode
* using custom colors

### Installation

```shellCan you tell what time it is
pip install color-captcha
```

### Usage

```python
from color_captcha import ClockCaptcha

captcha = ClockCaptcha()
print(captcha.value)

captcha.verify('0645') # True/False
captcha.save_image('image.png')

# generate new captcha
captcha.generate_new()

```
Choose between `color_mode='rgb'` ([color-captcha.png](color-captcha.png)) 
or `'grayscale'` ([grayscale-captcha.png](grayscale-captcha.png)). 

Pick between a 12-hour or a 24-hour `clock_mode`.
```python
from color_captcha import ClockCaptcha

captcha = ClockCaptcha(clock_mode=12)
```

Image size can be changed with relative `size` parameter. Here are corresponding pixel values. 

| size  | width   | height  |
|-------|---------|---------|
| 1     | 190     | 65      |
| 2     | 380     | 130     |
| **3** | **570** | **195** |
| 4 | 760 | 260 |
| ... | ... | ... | 

Change colors globally:
```python
from color_captcha import ClockCaptcha
ClockCaptcha.set_colors([
    '#FFFFFF',
    '#000000',
    '#999999'
])
```

