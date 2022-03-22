# Smart_buildings
This a a collection of codes to be used for smart things and smart home projects

## Flask home server
Python web microservice displays a complete control panel in single page design :
* Complete and rich web interface
* Can controle multiple devices
* Generates web requests that should be executed by device's basic web servers

## Basic web server
Micropython web server that works on Nodemcu/ESP8266 microcontroller can control a single device, consists on :
* Main script (executes after boot) : initializes microcontroller responses (actions) ton web requests and launches a listener for http requests
* Index page that displays anctions, the requests are sent by Ajax and actions are executed then response is displayed in the same page

