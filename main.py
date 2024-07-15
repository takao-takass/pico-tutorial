from machine import Pin
import network
import time

# Wi-FiのSSIDとパスワードを設定
ssid = ''
password = ''

# WLANオブジェクトの作成
wlan = network.WLAN(network.STA_IF)

# Wi-Fiを有効にする
wlan.active(True)
print('Connecting to network...')
wlan.connect(ssid, password)


led = Pin('LED', Pin.OUT)

# 接続が確立されるまで待機
while not wlan.isconnected():
    print('Waiting for connection...')
    led.toggle()
    time.sleep(0.5)

# 接続が確立された場合、IPアドレスを表示
print('Connected to network:', wlan.ifconfig())
led.on()


# while True:
#     led.toggle()
#     time.sleep(1)


