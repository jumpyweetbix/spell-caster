from app.db.db import db
from app.models.character import Character
from app.models._class import _Class


class Slots(db.Model):
    char_id = db.Column(db.Integer, db.ForeignKey('character.id', ondelete="CASCADE"), primary_key=True)
    lvl_1 = db.Column(db.Integer)
    lvl_2 = db.Column(db.Integer)
    lvl_3 = db.Column(db.Integer)
    lvl_4 = db.Column(db.Integer)
    lvl_5 = db.Column(db.Integer)
    lvl_6 = db.Column(db.Integer)
    lvl_7 = db.Column(db.Integer)
    lvl_8 = db.Column(db.Integer)
    lvl_9 = db.Column(db.Integer)


    def __init__(self, character):
        self.char_id = character.id
        self.character = character
        self.lvl_1,self.lvl_2,self.lvl_3,self.lvl_4,self.lvl_5,self.lvl_6,self.lvl_7,self.lvl_8,self.lvl_9 = self.get_slots()

    def __repr__(self):
        return '<Slots {}>'.format(self.character.name)


    def reset_slots(self):
        self.lvl_1,self.lvl_2,self.lvl_3,self.lvl_4,self.lvl_5,self.lvl_6,self.lvl_7,self.lvl_8,self.lvl_9 = self.get_slots()


    def get_slots(self):
        lvl = int(self.character.level)
        if lvl <= 1:
            return [2,0,0,0,0,0,0,0,0]
        
        if lvl == 2:
            return [3,0,0,0,0,0,0,0,0]

        if lvl == 3:
            return [4,2,0,0,0,0,0,0,0]
        
        if lvl == 4:
            return [4,3,0,0,0,0,0,0,0]

        if lvl == 5:
            return [4,3,2,0,0,0,0,0,0]
        
        if lvl == 6:
            return [4,3,3,0,0,0,0,0,0]
        
        if lvl == 7:
            return [4,3,3,1,0,0,0,0,0]

        if lvl == 8:
            return [4,3,3,2,0,0,0,0,0]

        if lvl == 9:
            return [4,3,3,3,1,0,0,0,0]

        if lvl == 10:
            return [4,3,3,3,2,0,0,0,0]

        if lvl == 11:
            return [4,3,3,3,2,1,0,0,0]
        
        if lvl == 12:
            return [4,3,3,3,2,1,0,0,0]

        if lvl == 13:
            return [4,3,3,3,2,1,1,0,0]
        
        if lvl == 14:
            return [4,3,3,3,2,1,1,0,0]

        if lvl == 15:
            return [4,3,3,3,2,1,1,1,0]

        if lvl == 16:
            return [4,3,3,3,2,1,1,1,0]

        if lvl == 17:
            return [4,3,3,3,2,1,1,1,1]

        if lvl == 18:
            return [4,3,3,3,3,1,1,1,1]

        if lvl == 19:
            return [4,3,3,3,3,2,1,1,1]
        
        if lvl >= 20:
            return [4,3,3,3,3,2,2,1,1]
