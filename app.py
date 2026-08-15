from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>PC Solutions NYC</h1>
    <h2>On-Site Computer & IT Support</h2>
    <p>Professional technology support in New York City.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
