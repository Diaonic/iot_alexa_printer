#!/usr/bin/python
#import flask and printer libs
from flask import Flask, request
from escpos.printer import Usb

#Vars
p = Usb(0x0416, 0x5011)
app = Flask(__name__)
#index
@app.route('/')
def index():
        return 'Flask server running!'

#list
@app.route('/list')
def list():
        #capture data from web hooks
        content = request.get_data()
        #convert raw data to string
        str_content = str(content)
        #split data into seperate lines
        str_split = str_content.splitlines()
        #seperate words by comma
        newlist = []
        for word in str_split:
                word = word.split(',')
                newlist.extend(word)
        #cleanup formatting
        rmv_marks = [s.strip("b'") for s in newlist]
        #print
        p.text("Shopping List:\n")
        #iterate over list
        r = 1
        for x in rmv_marks:
                p.text(str(r) + ". " + x + "\n")
                r += 1
        return x
#runa
if __name__ == '__main__':
        app.run(host='0.0.0.0')
#import flask and printer libs
from flask import Flask, request
from escpos.printer import Usb

#Vars
p = Usb(0x0416, 0x5011)
app = Flask(__name__)
#index
@app.route('/')
def index():
        return 'Flask server running!'

#list
@app.route('/list')
def list():
        #capture data from web hooks
        content = request.get_data()
        #convert raw data to string
        str_content = str(content)
        #split data into seperate lines
        str_split = str_content.splitlines()
        #seperate words by comma
        newlist = []
        for word in str_split:
                word = word.split(',')
                newlist.extend(word)
        #cleanup formatting
        rmv_marks = [s.strip("b'") for s in newlist]
        #print
        p.text("Shopping List:\n")
        #iterate over list
        r = 1
        for x in rmv_marks:
                p.text(str(r) + ". " + x + "\n")
                r += 1
        return x
#run
if __name__ == '__main__':
        app.run(host='0.0.0.0')
