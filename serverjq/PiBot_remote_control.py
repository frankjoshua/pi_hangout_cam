#!/usr/bin/python3

"""
Simple example to show how to use cherrypy with jquery and jquery mobile.
"""

import cherrypy

import time

import serial
import threading
arduino = serial.Serial('/dev/arduino', 115200)
print("Connecting to Arduino")
time.sleep(0)
##while 1:
  ##  value = arduino.read();
    ##print value
    #time.sleep(0)
class HelloWorld:
    """ Sample request handler class. """
    @cherrypy.expose
    def index(self):
        return '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0;" />
        <meta name="viewport" content="width=device-width"/>
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <title>
        </title>
        <link rel="stylesheet" href="static/jquery.mobile-1.0.1.min.css" />
        <style>
            /* App custom styles */
        </style>
        <script src="static/jquery.min.js">
        </script>
        <script src="static/jquery.mobile-1.0.1.min.js">
        </script>
        <script type="text/javascript">
        $(document).ready(function() {
            //stop the page from doing a stretch from the top when dragged ;
            document.ontouchmove = function(event){ event.preventDefault(); };
            //move beyond the address  bar to hide ;
            window.scrollTo(0, 1);
            //start button click code;
            $("#fl").click(function () {$.post('/request',{key_pressed:"FORWARD LEFT"})});
            $("#f").click(function () {$.post('/request',{key_pressed:"FORWARD"})});
            $("#fr").click(function () {$.post('/request',{key_pressed:"FORWARD RIGHT"})});
	    $("#l").click(function () {$.post('/request',{key_pressed:"LEFT"})});
            $("#s").click(function () {$.post('/request',{key_pressed:"STOP"})});
            $("#r").click(function () {$.post('/request',{key_pressed:"RIGHT"})});
	    $("#sf").click(function () {$.post('/request',{key_pressed:"FASTER"})});
            $("#b").click(function () {$.post('/request',{key_pressed:"BACKWARDS"})});
            $("#ss").click(function () {$.post('/request',{key_pressed:"SLOWER"})});
	    $("#plu").click(function () {$.post('/request',{key_pressed:"PAN LEFT UP"})});
            $("#pu").click(function () {$.post('/request',{key_pressed:"PAN UP"})});
            $("#pru").click(function () {$.post('/request',{key_pressed:"PAN RIGHT UP"})});
            $("#pl").click(function () {$.post('/request',{key_pressed:"PAN LEFT"})});
	    $("#cc").click(function () {$.post('/request',{key_pressed:"CENTER"})});
            $("#pr").click(function () {$.post('/request',{key_pressed:"PAN RIGHT"})});
            $("#pld").click(function () {$.post('/request',{key_pressed:"PAN LEFT DOWN"})});
            $("#pd").click(function () {$.post('/request',{key_pressed:"PAN DOWN"})});
            $("#prd").click(function () {$.post('/request',{key_pressed:"PAN RIGHT DOWN"})});

	    $("#power").change(function () {$.post('/request',{key_pressed:"power_"+$(this).val()})});
        });
        </script>
    </head>
<body onload="doOnload();">
    <body style="overflow: hidden;overflow-x:hidden;">
        <div data-role="page" data-theme="a" id="page1">
            <div data-theme="a" data-role="header" data-position="">
                <h5>
                    PiBot Remote
                </h5>
            </div>
<table>
<tr<td align=center>
<!--
<img src="http://192.168.254.52:8080/?action=stream" width="320" height="240">
-->
   </td>
</tr>
</tr>
            <div data-role="content">
                <div class="ui-grid-b">
                    <div class="ui-block-a">
                        <button type="button" id="fl" data-role="button" data-transition="fade" >
                            *
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="f" data-role="button" data-transition="fade">
                            ^
                        </button>
                    </div>
                    <div class="ui-block-c">
                        <button type="button" id="fr" data-role="button" data-transition="fade">
                            *
                        </button>
 		    </div>

 		    <div class="ui-block-a">
                        <button type="button" id="l" data-role="button" data-transition="fade" >
                            <
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="s" data-role="button" data-transition="fade">
                            STOP
                        </button>
                    </div>
                    <div class="ui-block-c">
                        <button type="button" id="r" data-role="button" data-transition="fade">
                            >
                        </button>
		    </div>

 		    <div class="ui-block-a">
                        <button type="button" id="sf" data-role="button" data-transition="fade" >
                            +
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="b" data-role="button" data-transition="fade">
                            v
                        </button>
                    </div>
                    <div class="ui-block-c">

                        <button type="button" id="ss" data-role="button" data-transition="fade">
                            -
                        </button>
                    </div>
                    <div class="ui-block-a">
                        <button type="button" id="fplu" data-role="button" data-transition="fade" >
                            *
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="pu" data-role="button" data-transition="fade">
                            ^
                        </button>
                    </div>
                    <div class="ui-block-c">
                        <button type="button" id="pru" data-role="button" data-transition="fade">
                            *
                        </button>
 		    </div>
 		    <div class="ui-block-a">
                        <button type="button" id="pl" data-role="button" data-transition="fade" >
                            <
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="cc" data-role="button" data-transition="fade">
                            +
                        </button>
                    </div>
                    <div class="ui-block-c">
                        <button type="button" id="pr" data-role="button" data-transition="fade">
                            >
                        </button>
		    </div>

 		    <div class="ui-block-a">
                        <button type="button" id="pld" data-role="button" data-transition="fade" >
                            *
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="pd" data-role="button" data-transition="fade">
                            v
                        </button>
                    </div>
                    <div class="ui-block-c">
                        <button type="button" id="prd" data-role="button" data-transition="fade">
			    *
                        </button>
                    </div>
            </div>
        </div>
        <script>
            //App custom javascript
        </script>
    </body>
</html>
'''
    @cherrypy.expose
    def request(self, **data):
        # Then to access the data do the following
        #print data
        key = data['key_pressed'].upper()
        if key == "FORWARD LEFT":
	    arduino.write('FL2Q')
        elif key == "FORWARD":
            arduino.write('u')
        elif key == "FORWARD RIGHT":
            arduino.write('FR2Q')
        elif key == "LEFT":
            arduino.write('l')
        elif key == "STOP":
            arduino.write('STOPQ')
        elif key == "RIGHT":
            arduino.write('r')
        elif key == "FASTER":
            arduino.write('F+Q')
        elif key == "BACKWARDS":
            arduino.write('d')
        elif key == "SLOWER":
            arduino.write('F-Q')

        elif key == "PAN LEFT UP":
            arduino.write('PLUQ')
        elif key == "PAN UP":
            arduino.write('UUQ')
        elif key == "PAN RIGHT UP":
            arduino.write('PRUQ')
 	elif key == "PAN LEFT":
            arduino.write('LLQ')
        elif key == "CENTER":
            arduino.write('CCQ')
        elif key == "PAN RIGHT":
            arduino.write('RRQ')
        elif key == "PAN LEFT DOWN":
            arduino.write('PLDQ')
        elif key == "PAN DOWN":
            arduino.write('DDQ')
        elif key == "PAN RIGHT DOWN":
            arduino.write('PLDQ')
        else:
            print key

import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(HelloWorld(), config=tutconf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(HelloWorld(), config=tutconf)
