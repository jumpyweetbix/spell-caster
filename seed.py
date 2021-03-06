import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app.app import create_app, register_extensions
from app.config.config import DevelopmentConfig
from app.db.db import db

from app.db.seeds.spell_seeder import SpellSeeder
from app.db.seeds.class_seeder import ClassSeeder
from app.db.seeds.monster_seeder import MonsterSeeder
from app.db.seeds.char_seeder import CharSeeder


app = create_app(DevelopmentConfig)
register_extensions(app)
manager = Manager(app)
migrate = Migrate(app, db)
c_seeder = ClassSeeder(app)
s_seeder = SpellSeeder(app)
m_seeder = MonsterSeeder(app)
ch_seeder = CharSeeder(app)

@manager.command
def all():
	c_seeder.run()
	s_seeder.run()
	m_seeder.run()
	ch_seeder.run()
    

@manager.command
def _class():
	c_seeder.run()

@manager.command
def spell():
	s_seeder.run()

@manager.command
def monster():
	m_seeder.run()

@manager.command
def guh():
	ch_seeder.run()

if __name__ == '__main__':
	manager.run()