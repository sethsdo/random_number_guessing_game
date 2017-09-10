import random
from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

dev = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def user_guess():
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1, 101)
    # print "here is the random"
    # print request.form['guess']
    guess = int(request.form['guess'])

    if guess < session['rand_num']:
        session['guess'] = 'too_low'
    elif guess > session['rand_num']:
        session['guess'] = 'too_high'
    else:
        session['guess'] = "correct" 

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reload_game():
    session.clear()
    return redirect('/')

app.run(debug=dev)
