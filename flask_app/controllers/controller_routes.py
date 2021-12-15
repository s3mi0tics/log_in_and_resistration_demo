from flask_app import app
from flask import render_template, redirect, session, request, flash


from flask_app.models import model_user #import all model tables 
@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user' : model_user.User.get_one({'id': session ['uuid']})
    }
    return render_template('success.html', **context)

#@app.errorhandler(404)
#def server_error(e):
#    print('running error function')
#    return render_template('error.html')