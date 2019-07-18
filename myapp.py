from flask import Flask, render_template

#------------------------------------1. init app ---------------------
app = Flask(__name__)


#------------------------------------2. Routers ------------------------
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/About_Us')
def About_Us():
    return render_template('about-us.html')

@app.route('/Services')
def Services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('full_website.html')


#-----------------------------------------3.start server ---------------------------------
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
