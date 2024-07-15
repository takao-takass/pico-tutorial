from machine import Pin, I2C
import ssd1306

# I2C接続の設定
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)  # scl: GP17, sda: GP16

# OLEDディスプレイの初期化
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# ディスプレイをクリア
oled.fill(0)

# "Hello World"を描画
oled.text("Hello World", 0, 0)

# 描画をディスプレイに表示
oled.show()
