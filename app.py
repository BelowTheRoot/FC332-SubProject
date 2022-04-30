from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def signin():  # put application's code here
    return render_template('Sign-in.html')

if __name__ == '__main__':
    app.run()
