from app import create_app
from flask_script import Manager,Server
# creating app instance
# Creating app instance
app = create_app('app')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ ==  "__main__":
    manager.run()