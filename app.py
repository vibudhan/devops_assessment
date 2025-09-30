# app.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# A secret key is needed to use flash messages
app.secret_key = 'some_random_string_for_security'

@app.route('/user', methods=['GET', 'POST'])
def user_page():
    if request.method == 'POST':
        # Get the name from the form
        name = request.form['new_name']
        
        # Flash a success message
        flash(f"Success! Name changed to {name}.", 'success')
        
        # Redirect back to the user page (as a GET request)
        return redirect(url_for('user_page'))
    
    # This part only runs for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
