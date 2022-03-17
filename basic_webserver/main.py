import network
import time
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to phone network...')
    wlan.connect('rezmax', 'porshe45ccx')
    for i in range(8) :
        if (not wlan.isconnected()):
            time.sleep(1) 
            pass
        else :
            print ("connected")
        
if not wlan.isconnected():
    print('connecting to home network...')
    wlan.connect('ALHN-7003', '9776105615')
    for i in range(8) :
        if (not wlan.isconnected()):
            time.sleep(1) 
            pass
        else :
            print ("connected")
print('network config:', wlan.ifconfig())

import socket
from machine import Pin
led    = Pin(2, Pin.OUT)
buzzer = Pin(1, Pin.OUT)

def web_page(param):
  text_file = open("index.html", "r")
  html = text_file.read()
  text_file.close()
  send_resp(html)

def send_resp(text):
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(text)
  conn.close()

def light(param) :
  print("\nlight " + param + "\n")
  if param == "on" :
    led.value(1)
  elif param == "off" :
    led.value(0)
  else :
    print("light param not understood")
  send_resp("light "+param)
    
def sound(param) :
  print("\nsound " + param + "\n")
  if param == "1" :
    for i in range(20) :
      buzzer.value(1)
      time.sleep(0.05)
      buzzer.value(0)
      time.sleep(0.05)
  elif param == "2" :
    for i in range(10) :
      buzzer.value(1)
      time.sleep(0.1)
      buzzer.value(0)
      time.sleep(0.1) 
  elif param == "3" :
    for i in range(5) :
      buzzer.value(1)
      time.sleep(0.2) 
      buzzer.value(0)
      time.sleep(0.2) 
  else :
    print("sound param not understood")
  send_resp("sound "+param)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
      
  action = "web_page"
  param = ""
  try :
    if request.find("action=")>=0 :
      action = request[request.find("action=")+len("action="):request.find("&param")]
    if request.find("param=") >=0 :
      param = request[request.find("param=")+len("param="):request.find(" HTTP")]
    print("\n---------\nProceeding action '" + action + "' \n")
  except :
    print("\n---------\nBad URL syntax will send default page \n")

  action_func = globals()[action]
  if action_func != None :
    action_func(param)
  else :
    print("No action : " + action)
    