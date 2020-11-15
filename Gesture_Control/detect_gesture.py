################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################
import os, sys, inspect, thread, time
sys.path.insert(0,'/Users/xh/Library/Mobile Documents/com~apple~CloudDocs/Documents/Oxy/COMP490/Code/Gesture_Control/LeapSDK/lib')
# print(sys.path)

# import Leap, sys, thread, time
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import paho.mqtt.publish as publish
 
MQTT_SERVER = "134.69.204.20"
MQTT_PATH = "test_channel"

class SampleListener(Leap.Listener):

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        right_swipe = False 
        left_swipe = False 

        # Get gestures
        for gesture in frame.gestures():

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                curr_gesture = gesture
                swipe = SwipeGesture(gesture)

                d = swipe.direction

                if curr_gesture.state is Leap.Gesture.STATE_STOP:
                    if d.x > 0:
                        right_swipe = True 
                    elif d.x < 0:
                        left_swipe = True 

        if right_swipe:
            print "right swipe"
            publish.single(MQTT_PATH, "right swipe", hostname=MQTT_SERVER)
            time.sleep(1)
        elif left_swipe:
            print "left swipe" 
            publish.single(MQTT_PATH, "left swipe", hostname=MQTT_SERVER)
            time.sleep(1)

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
