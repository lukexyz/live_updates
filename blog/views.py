from live_updates import app

@app.route('/')
@app.route('/login')
def login():
    return "Log in page"
