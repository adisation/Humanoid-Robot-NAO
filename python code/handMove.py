import time
import motion
import argparse
from naoqi import ALProxy

def main(robotIP =127.0.0.1, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Example showing how to set LArm Position, using a fraction of max speed
    chainName = "LArm"
    frame     = motion.FRAME_TORSO
    useSensor = False

    # Get the current position of the chainName in the same frame
    current = motionProxy.getPosition(chainName, frame, useSensor)

    target = [
        current[0] + 0.05,
        current[1] + 0.05,
        current[2] + 0.05,
        current[3] + 0.0,
        current[4] + 0.0,
        current[5] + 0.0]

    fractionMaxSpeed = 0.5
    axisMask         = 7 # just control position

    motionProxy.setPositions(chainName, frame, target, fractionMaxSpeed, axisMask)

    time.sleep(1.0)
    postureProxy.goToPosture("StandInit", 0.5)

    # Example showing how to set Torso Position, using a fraction of max speed
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
