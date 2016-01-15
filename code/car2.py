import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 0.5)
p.start(1)
input('点击回车停止：')   # 在 Python 2 中需要使用 raw_input
p.stop()
GPIO.cleanup()