from app import app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand


server = Server(port=2000)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host="0.0.0.0", port=2000))

if __name__ == "__main__":
    app.debug = True
    manager.run()