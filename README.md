# Smart_buildings
This a a collection of codes to be used for smart things and smart home projects

## Architecture
![Architecture](http://www.mederp.net/projects/smart_buildings/sb_architecture.png)

## Central server
Python web microservice displays a complete control panel in single page design :
* Complete and rich web interface
* Can controle multiple devices
* Generates web requests that should be executed by device's basic web servers

## Area controller
Micropython web server that works on Nodemcu/ESP8266 or ESP32 microcontroller can control a given area (indoor or outdoor) with a few devices, consists on :
* Main script (executes after boot) : initializes microcontroller responses (actions) ton web requests and launches a listener for http requests
* Index page that displays anctions, the requests are sent by Ajax and actions are executed then response is displayed in the same page

## Universal bridge
A bridge consisting on a single board computer (raspberry) and a sniffer usb for zigbee and z-wave protocols, aims to collect data and control low consumption devices and sensors.
