import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # adds directory above to path

from flask_script import Manager, Server
from live_updates import app

manager = Manager(app)

manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080))
    )
)

if __name__ == '__main__':
    manager.run()
