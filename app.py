from flask import Flask, jsonify, render_template, json, redirect, request
import pandas as pd 
import webbrowser
import zmq
# Flask constructor
app = Flask(__name__)

# Data setup
table = pd.read_csv("salaries.csv")
table.fillna('', inplace=True)
table_dict = {col: list(table[col]) for col in table.columns}
headings = list(table.columns)
data = list(table.values)
#[0:10]
#print(data[0])

#Zeromq setup
context = zmq.Context()

#  Socket to talk to server
#print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")



# Homepage URL call
@app.route("/")
def home():
    return render_template("home.html", headings=headings, data=data)


@app.route('/GetPlayerInfo/<int:rowindex>')
def get_player_info(rowindex):
    #info = list(data[rowindex-1])
    
    #player_id = info[len(info)-1]
    
    #ID = player_id

    #id = str(ID)
    socket.send_string(str(rowindex))
    
    #a = "https://www.transfermarkt.com/oskar-agren/profil/spieler/"
    #b = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query="
    #url = ""
    #if ID > 0:
     #   url =  a + id
 
    #if ID == 0:
     #   name1 = str(info[0])
      #  name2 = str(info[1])
       # Name = name1 + "+" + name2
        #url = b + Name
        
        
    message = socket.recv_string()
    #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    #url = str(message)
    #print(url)
    #webbrowser.open(url)
    return message

@app.route("/", methods=["POST"])
def search():
    name = request.form.get("name")
    name2 = request.form.get("name2")
    team = request.form.get("team")
    filterdata = []
    for e in data:
        if ((name == "" or name.lower() in e[0].lower()) and
            (name2 == "" or name2.lower() in e[1].lower()) and
            (team == "" or team.lower() in e[2].lower())):
            filterdata.append(e)
    if filterdata == []:
        no_data = ["No  "]
        return render_template("home.html", headings=no_data, name=name, name2=name2, team=team)
    else:
        return render_template("home.html", headings=headings, data=filterdata,  name=name, name2=name2, team=team)

# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)