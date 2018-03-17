from live_updates import app

@app.route('/')
@app.route('/index')
def index():
    return "Sup cunts - Welcome to live updates"
