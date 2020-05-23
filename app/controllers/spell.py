from flask import render_template, flash, redirect, url_for, request, session
from flask_wtf import FlaskForm
from flask_login import current_user, login_user, logout_user

from werkzeug.datastructures import MultiDict

from app.models.user import User
from app.models.character import Character
from app.models._class import _Class
from app.models.spell import Spell

from app.db.db import db

from app.forms import SpellForm

from app.utils.model_helpers import *

def create_spell():
    if not current_user.is_authenticated:
        flash("Please login first!")
        return redirect(url_for('login'))

    form = SpellForm()

    if form.validate_on_submit():
        spell = insert_form(Spell, form)
        flash("Created spell!")
        return redirect(url_for('view_spell', id=spell.id))

    return render_template('form.html', form=form, title="Create Spell")

def view_spell():
    default = get_default(Spell)
    if default is None:
        flash("No spells found!")
        return redirect(url_for('create_spell'))

    spell = get_model(Spell, request.args.get('id', default = default.id, type = int))
    if not spell:
        flash("Couldn't find that spell!")
        return redirect(url_for('index'))
        

    return render_template('spell.html', spell=spell, title=spell.name)

def view_all_spells():
    spells = get_all_models(Spell)
    if not spells:
        flash("No spells found!")
        return redirect(url_for('create_spell'))

    return render_template('all_spells.html', spells=spells, title="Spells")

def edit_spell():
    if not current_user.is_authenticated:
        flash("Please login first!")
        return redirect(url_for('login'))

    spell = get_model(Spell, request.args.get('id', type = int))
    if not spell:
        flash("Couldn't find that spell!")
        return redirect(url_for('view_spell'))

    if request.method == 'GET':
        form = SpellForm(formdata=MultiDict({
            'name': spell.name,
            'level': spell.level,
            'cast_time': spell.cast_time,
            'concentration': spell.concentration,
            'ritual': spell.ritual,
            'spell_range': spell.spell_range,
            'components': spell.components,
            'duration': spell.duration,
            'school': spell.school,
            'info': spell.info,
            'from_book': spell.from_book,
            'is_bard': spell.is_bard,
            'is_cleric': spell.is_cleric,
            'is_druid': spell.is_druid,
            'is_paladin': spell.is_paladin,
            'is_ranger': spell.is_ranger,
            'is_sorcerer': spell.is_sorcerer,
            'is_warlock': spell.is_warlock,
            'is_wizard': spell.is_wizard
        }))


    else:
        form = SpellForm()

    if form.is_submitted():
        update_form(spell, form)

        flash("Updated spell!")
        return redirect(url_for('view_spell', id=spell.id))

    return render_template('form.html', form=form, title="Edit Spell")






def delete_spell():
    if not current_user.is_authenticated:
        flash("Please login first!")
        return redirect(url_for('login'))
    
    spell = get_model(Spell, request.args.get('id', type = int))
    if not spell:
        flash("Couldn't find that spell!")
        return redirect(url_for('view_spell'))

    delete_model(spell)
    
    flash("Spell deleted!")
    return redirect(url_for('view_spell')) if get_default(Spell) else redirect(url_for('index'))