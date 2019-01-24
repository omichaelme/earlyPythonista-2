from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def showBoxes():
    return render_template("play.html", phrase="Welcome!", times=3)

@app.route('/play/<num>')
def showBoxes1(num):
    return render_template("play.html", phrase="Welcome!", times=int(num))

@app.route('/play/<num>/<color>')
def showBoxes2(num,color):
    return render_template("play.html", phrase="Welcome!", times=int(num),box_color=color)

if __name__=="__main__":
    app.run(debug=True)
