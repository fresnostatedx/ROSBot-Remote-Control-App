#!/usr/bin/env python

"""
   Project Name: Bulldog Bot - Remote Control
   By: Fresno State DX
   Email: dx@mail.fresnostate.edu
   Project Site: https://medium.com/fresnostatedx/bulldog-autonomous-bot-2cf4badf3c1
   Last Updated: 10/21/2019
   Copyright 2019 Fresno State / Digital Transformation
"""

# noinspection PyUnresolvedReferences
import rospy
import ast
# noinspection PyUnresolvedReferences
from std_msgs.msg import String
# noinspection PyUnresolvedReferences
from geometry_msgs.msg import Twist
# noinspection PyUnresolvedReferences
from websocket_server import WebsocketServer

PORT = 8000
pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)


# Called for every client connecting (after handshake)
def new_client(client, server):
    msg = "Client (join), id: " + str(client['id'])
    rospy.loginfo(msg)
    server.send_message_to_all('Welcome!')


# Called for every client disconnecting
def client_left(client, server):
    msg = "Client (left), id: " + str(client['id'])
    rospy.loginfo(msg)


# Called when a client sends a message
def message_received(client, server, message):
    msg = "Message client (id: " + str(client['id']) + "): " + message
    rospy.loginfo(msg)
    message = ast.literal_eval(message)
    if 'speed' in message:
        twist.linear.x = message['speed']; twist.linear.y = 0; twist.linear.z = 0;
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = message['angle']
        pub.publish(twist)


def run_node():
    rospy.init_node('rcontrol', anonymous=True, disable_signals=True)
    rate = rospy.Rate(10)  # 10hz
    socket.set_fn_new_client(new_client)
    socket.set_fn_client_left(client_left)
    socket.set_fn_message_received(message_received)
    socket.run_forever()


if __name__ == '__main__':
    try:
        twist = Twist()
        socket = WebsocketServer(port=PORT, host="0.0.0.0")
        run_node()
    except rospy.ROSInterruptException:
        pass
    # pip install websocket_server

