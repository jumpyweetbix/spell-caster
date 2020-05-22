from flask import render_template, flash, redirect, url_for, request, session
from flask_wtf import FlaskForm
from flask_login import current_user, login_user, logout_user

from werkzeug.datastructures import MultiDict

from app.models.user import User
from app.models.character import Character
from app.models._class import _Class
from app.models.note import Note

from app.db.db import db

from app.forms import NoteForm, PickNoteForm

from app.utils.model_helpers import *
from app.utils.character_helpers import *




def create_note():
    # check user is authenticated
    if not is_user_logged_in:
        return redirect(url_for('login'))

    # check user has characters
    if not user_has_characters():
        flash("Please create a character first!")
        return redirect(url_for('create_char'))
        
    # check user has a selected character
    if not is_char_id_set():
        flash("Please select a character first!")  
        return redirect(url_for('view_char'))

    char = get_current_char()

    form = NoteForm()

    # insert the created note into the database after the user has submitted the form
    if form.is_submitted():
        note = Note(form.title.data,form.body.data, char.id)
        insert_obj(note, "note")
        return redirect(url_for('view_note'))

    return render_template('form.html', form=form, title="Create Spell")

def view_note():
    # check user is authenticated
    if not is_user_logged_in:
        return redirect(url_for('login'))

    # check user has characters
    if not user_has_characters():
        flash("Please create a character first!")
        return redirect(url_for('create_char'))
        
    # check user has a selected character
    if not is_char_id_set():
        flash("Please select a character first!")  
        return redirect(url_for('view_char'))

    char = get_current_char()

    # check character has notes
    if not character_has(Note):
        flash("Please create a note first!")
        return redirect(url_for('create_note'))

    # get a default note in case url parameter is missing
    default = get_char_child_default(Note)

    # check the default obj exists. This is only a sanity check
    # at this point, user will have a note
    if not is_default(default, "note"):
        return redirect(url_for('create_note'))

    # get the note selected via url parameter, so long as it is owned by the current character
    note = get_char_child(Note, request.args.get('id', default = default.id, type = int))

    # check the selected note exists
    if not is_obj(note, "note"):
        return redirect(url_for('index'))

    # if the form isn't being submitted, the SelectField should show the currently selected note
    if request.method == 'GET':
        form = PickNoteForm(formdata=MultiDict({'note_id': note.id}))
    else:
        form = PickNoteForm()

    # get a list of all notes owned by the current character
    notes = get_all_char_child(Note, 'title')

    # fill the SelectField with all notes owned by the current character
    form.note_id.choices = [(g.id, g.title) for g in notes]

    
    if form.is_submitted():
        return redirect(url_for('view_note', id=form.note_id.data))

    return render_template('note.html', form=form, note=note, char=char, title=note.title)

def edit_note():
    # check user is authenticated
    if not is_user_logged_in:
        return redirect(url_for('login'))

    # check user has characters
    if not user_has_characters():
        flash("Please create a character first!")
        return redirect(url_for('create_char'))
        
    # check user has selected a character
    if not is_char_id_set():
        flash("Please select a character first!")  
        return redirect(url_for('view_char'))

    # get default note in case url parameter is not set
    default = get_char_child_default(Note)

    # sanity check for default note object
    if not is_default(default, "note"):
        return redirect(url_for('create_note'))

    # get the note owned by the current character, selected by url parameter
    note = get_char_child(Note, request.args.get('id', default = default.id, type = int))

    # check note exists
    if not is_obj(note, "note"):
        return redirect(url_for('view_note'))

    # if the form is being loaded, form should be filled with current note values
    if request.method == 'GET':
        form = NoteForm(formdata=MultiDict({
            'title': note.title,
            'body': note.body
        }))
    else:
        form = NoteForm()

    if form.is_submitted():
        note.title = form.title.data
        note.body = form.body.data
        db.session.commit()

        flash("Updated note!")
        return redirect(url_for('view_note', id=note.id))

    return render_template('form.html', form=form, title="Edit Note")