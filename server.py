from turtle import xcor
from flask import Flask, render_template

app = Flask(__name__)                     


# Level 1
# When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes. Please use a template to render this.
@app.route('/play')
def play():
    return render_template('index.html', num=3, color="lightblue")



# Level 2
# When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times. For example, localhost:5000/play/7 should display these blue boxes 7 times. Calling localhost:5000/play/35 would display these blue boxes 35 times. Please remember that x originally is a string, and if you want to use it as an integer, you must first convert it to integer using int(). For example int("7") returns 7.
@app.route('/play/<int:x>')
def play_num(x):
    return render_template('index.html', num=x, color="lightblue")



# Level 3
# When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color). For example, localhost:5000/play/5/green would display 5 beautiful green boxes. Calling localhost:5000/play/35/red would display 35 beautiful red boxes.
@app.route('/play/<int:x>/<string:color>')
def play_num_color(x, color):
    return render_template('index.html', num=x, color=color)  # color=color: color on the right hand side is the one that passed into route

    
if __name__=="__main__":
    app.run(debug=True) 