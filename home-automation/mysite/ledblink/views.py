
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse

import time
import serial
import datetime
#import Adafruit_DHT
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
#sensor=Adafruit_DHT.DHT22

# Set GPIO sensor is connected to
#dhtsensor=17
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)


#arduinoserialdata=serial.Serial('/dev/ttyACM2',9600)#arduino for dc motor
#arduino=serial.Serial('/dev/ttyACM1',9600) #arduino for relay board        
res1="closed"
@login_required(login_url="login/")
def home(request):
         # Use read_retry method. This will retry up to 15 times to
         # get a sensor reading (waiting 2 seconds between each retry).
         humidity, temperature = Adafruit_DHT.read_retry(sensor, dhtsensor)
         time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate
         if 'door-open' in request.POST: 
                arduinoserialdata.write('1')#door  open
                res1="OPEN"
         	#arduinoserialdata.write('1')#water pump on
         	#arduinoserialdata.write('3')#air pump on                
                #return render(request,'blog/controlling.html',{'result':result,'temp1':temp1,'humidity':humidity,'res':res})
        	return render(request,'blog/index.html',{'res1':res1,'temperature':temperature,'humidity':humidity})
         elif 'door-close' in request.POST:
                
                #arduinoserialdata.write('6')#fan off
         	arduinoserialdata.write('2')#door closed
         	res1="CLOSED"
         	#arduinoserialdata.write('4')#air pump off          
	 	return render(request,'blog/index.html',{'res1':res1,'temperature':temperature,'humidity':humidity})
	 elif 'light-on' in request.POST: 
                arduinoserialdata.write('4')#light on
                res2="ON"
         	return render(request,'blog/index.html',{'res2':res2,'temperature':temperature,'humidity':humidity})
         elif 'light-off' in request.POST:
         	arduinoserialdata.write('5')#Light off
         	res2="OFF"          
	 	return render(request,'blog/index.html',{'res2':res2,'temperature':temperature,'humidity':humidity})
	 elif 'fan-on' in request.POST: 
                arduinoserialdata.write('8')#light on
                res3="ON"
         	return render(request,'blog/index.html',{'res3':res3,'temperature':temperature,'humidity':humidity})
         elif 'fan-off' in request.POST:
                
         	arduinoserialdata.write('7')#Light off
         	res3="OFF"          
	 	return render(request,'blog/index.html',{'res3':res3,'temperature':temperature,'humidity':humidity})
	 elif 'pc-on' in request.POST: 
                arduinoserialdata.write('6')#light on
                res4="ON"
         	return render(request,'blog/index.html',{'res4':res4,'temperature':temperature,'humidity':humidity})
         elif 'pc-off' in request.POST:
                
         	arduinoserialdata.write('5')#Light off
         	res4="OFF"          
	 	return render(request,'blog/index.html',{'res4':res4,'temperature':temperature,'humidity':humidity})
	 else:
                res1="CLOSED"
                return render(request,'blog/index.html',{'res1':res1,'temperature':temperature,'humidity':humidity})

'''
def monitor(request):
	res=0
	led_res="LED Light"
	fan_res="FAN "
        [temp1,humidity]=grovepi.dht(sensor,0 )
        th=Temp_humi(temp=temp1,humi=humidity,date_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        th.save()
        data1=Temp_humi.objects.all().order_by('-temp_humi_id')[:1]
        for val in data1:
            temp_val=val.temp
        if temp_val>=28:
            arduinoserialdata.write('5')#fan ON
            arduino.write('4')#led low state
	    res=0
	    led_res="Temperature is High LED is OFF"
	    fan_res="Temperature is High FAN is ON"
        else:
            arduinoserialdata.write('6')#fan Off
            arduino.write('1')#led medium state
	    res=1
            led_res="Temperature is Low LED is ON"
	    fan_res="Temperature is LOW FAN is OFF"
        data=Temp_humi.objects.all().order_by('-temp_humi_id')[:10]
	return render(request,"blog/monitoring.html",{'data':data, 'data1':data1,'temp_val':temp_val,'res':res,'led_res':led_res,'temp1':temp1,'fan_res':fan_res})

def control(request):
        fan_result="FAN"
        water_pump_result="WATER PUMP"
        air_pump_result="AIR PUMP"
        led_result="LED LIGHT"

        if 'fan_on' in request.POST: 
                arduinoserialdata.write('5')
                fan_result='Fan is ON'            
                #return render(request,'blog/controlling.html',{'result':result,'temp1':temp1,'humidity':humidity,'res':res})
        	return render(request,'blog/controlling.html',{'led_result':led_result,'fan_result':fan_result,'air_pump_result':air_pump_result,'water_pump_result':water_pump_result})
        elif 'fan_off' in request.POST:
                arduinoserialdata.write('6')
                fan_result='Fan is OFF'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'fan_result':fan_result,'air_pump_result':air_pump_result,'water_pump_result':water_pump_result})
        elif 'water_pump_on' in request.POST:
                arduinoserialdata.write('1')
                water_pump_result='water_pump_on'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'water_pump_result':water_pump_result,'fan_result':fan_result,'air_pump_result':air_pump_result})
        elif 'water_pump_off' in request.POST:
                arduinoserialdata.write('2')
                water_pump_result='water_pump_off'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'water_pump_result':water_pump_result,'fan_result':fan_result,'air_pump_result':air_pump_result})
        elif 'air_pump_on' in request.POST:
                arduinoserialdata.write('3')
                air_pump_result='air_pump_on'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'air_pump_result':air_pump_result,'fan_result':fan_result,'water_pump_result':water_pump_result})
        elif 'air_pump_off' in request.POST:
                arduinoserialdata.write('4')
                air_pump_result='air_pump_off'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'air_pump_result':air_pump_result,'fan_result':fan_result,'water_pump_result':water_pump_result})
        elif 'led_on' in request.POST:
                arduino.write('2')
                led_result='LED On'            
        	return render(request,'blog/controlling.html',{'air_pump_result':air_pump_result,'fan_result':fan_result,'water_pump_result':water_pump_result})
        elif 'led_off' in request.POST:
                arduino.write('4')
                led_result='LED Off'            
        	return render(request,'blog/controlling.html',{'air_pump_result':air_pump_result,'fan_result':fan_result,'water_pump_result':water_pump_result})
        elif 'led_low' in request.POST:
                arduino.write('1')
                led_result='LED On'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'air_pump_result':air_pump_result,'fan_result':fan_result,'water_pump_result':water_pump_result})
        elif 'led_medium' in request.POST:
                arduino.write('2')
                led_result='LED Off'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'air_pump_result':air_pump_result,'fan_result':fan_result,'water_pump_result':water_pump_result})
        elif 'led_high' in request.POST:
                arduino.write('3')
                led_result='LED Off'            
        	return render(request,'blog/controlling.html',{'led_result':led_result,'air_pump_result':air_pump_result,'fan_result':fan_result,'water_pump_result':water_pump_result}) 
        else :
                  return render(request,'blog/controlling.html',{'led_result':led_result,'fan_result':fan_result,'water_pump_result':water_pump_result,'air_pump_result':air_pump_result})
                
        
def planth_health(request):
	data=Temp_humi.objects.all().order_by('-temp_humi_id')[:5]
	return render(request,"blog/planth_health.html", {'data':data})

        
'''
