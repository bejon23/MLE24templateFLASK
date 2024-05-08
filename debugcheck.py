from flask import Flask, render_template

app = Flask(__name__)

# Print out the template directory path
print("Template directory path:", app.template_folder)

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
