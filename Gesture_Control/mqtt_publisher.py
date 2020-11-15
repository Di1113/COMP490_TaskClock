import paho.mqtt.publish as publish
 
MQTT_SERVER = "134.69.204.20"
MQTT_PATH = "test_channel"
 
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
