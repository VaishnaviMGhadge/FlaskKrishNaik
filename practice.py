from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Fetch values from the form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Print the values (you can process or store them as needed)
        return(f"Name: {name}, Email: {email}, Message: {message}")

        # You can add your logic to process or store the form data here

        # For now, let's just redirect to the home page
        #return redirect('/')
    else:
        # Handle other HTTP methods if needed
        return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(debug=True)
