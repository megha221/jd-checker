from flask import Flask, render_template,jsonify

app = Flask(__name__)
@app.route('/')
def index():
        user_name = "Alice"
        return render_template('index.html', name=user_name)

@app.route('/health')
def health():
        return jsonify({"Ok":True})

if __name__ == '__main__':
        app.run(debug=True,port=8000)