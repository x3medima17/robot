import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)


class Robot(object):
  def __init__(self):
    self.p = [7,11,13,15]
    self.directions = dict(
      back = [7,13],
      forward = [11,15],
      left = [11,13],
      right = [7,15]
      )

    for port in self.p:
      GPIO.setup(port,GPIO.OUT)
      GPIO.output(port,False)


  def stop(self):
    p = self.p
    for port in p:
      GPIO.output(port,False)

  def set_move(self,direction):
    directions = self.directions
    self.stop()
    print "Move to                    " + direction
    for port in directions[direction]:
      GPIO.output(port,True)


if __name__ == "__main__":

  robot = Robot()
  #sys.exit()
  while True:
    try:
      robot.set_move("forward")
      time.sleep(2)
      robot.set_move("back")
      time.sleep(2)
    except KeyboardInterrupt:
      robot.stop()
      GPIO.cleanup()
      sys.exit()
