#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14, RPi.GPIO.OUT)
RPi.GPIO.setup(15, RPi.GPIO.OUT)


# 呼吸灯的效果
# 创建一个 PWM 实例，需要两个参数，第一个是GPIO端口号，这里我们用14号
# 第二个是频率（Hz），频率越高LED看上去越不会闪烁，相应对CPU要求就越高，设置合适的值就可以
pwm = RPi.GPIO.PWM(14, 80)
pwm2 = RPi.GPIO.PWM(15, 80)

# 启用 PWM，参数是占空比，范围：0.0 <= 占空比 >= 100.0
pwm.start(0)
pwm2.start(0)

try:
    while True:
        # 电流从小到大，LED由暗到亮
        for i in xrange(0, 101, 1):
            # 更改占空比，
            pwm.ChangeDutyCycle(i)
            pwm2.ChangeDutyCycle(i)
            time.sleep(.02)

        # 再让电流从大到小，LED由亮变暗
        for i in xrange(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            pwm2.ChangeDutyCycle(i)
            time.sleep(.02)

# 最后一段是一个小技巧。这个程序如果不强制停止会不停地执行下去。
# 而Ctrl+C强制终端程序的话，GPIO口又没有机会清理。
# 加上一个try except 可以捕捉到Ctrl+C强制中断的动作，
# 试图强制中断时，程序不会马上停止而是会先跳到这里来做一些你想做完的事情，比如清理GPIO口。
except KeyboardInterrupt:
    pass

# 停用 PWM
pwm.stop()
pwm2.stop()

# 清理GPIO口
RPi.GPIO.cleanup()
