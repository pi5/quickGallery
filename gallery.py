from flask import Flask
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

@app.route('/')
def show_gallery():
    mypath = "/Users/mozilla/Pictures/Swapnil_Ajay_Piyush_PKV/"
    files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and f[-3:].lower() == "jpg" ]
    string = "<!DOCTYPE HTML>"
    for f in files:
        string = string + "<a href='" + f + "' download='" + f +"' target='_blank'> <img style ='width:25%' src=" + f + "></a> <br>"
        
    return string 
    

if __name__ == '__main__':
        app.run()
