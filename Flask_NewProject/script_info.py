
def run(projectName):
    run = """from {} import app

if __name__ == "__main__":
app.run()""".format(projectName)

    return run


def app_simple():
    return """from flask import Flask


app = Flask(__name__)

@app.route('/')
def index_page():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
"""
    
