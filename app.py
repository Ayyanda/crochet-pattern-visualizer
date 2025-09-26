from flask import Flask
from routes.patterns import patterns_bp

app=Flask(__name__)
app.register_blueprint(patterns_bp)

if __name__ == "__main__":
    app.run(debug=True)