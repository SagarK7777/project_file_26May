########################
# ####flask application 
########################

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api1', methods=['POST','GET'])
def api1():
    return 'API1 Running'

if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)