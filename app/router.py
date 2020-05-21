from .controllers import home, user, character, _class

def routes(app):
    '''All Routes / Url
    This app uses an MVC pattern, hence all the url are routed here
    Just import your logics from the controllers package and route
    using the add_url_rule function

    :param app: Flask app instance
    :return: None
    '''

    # Common errors handled already for you. you can add more
    app.register_error_handler(403, home.error_pages)
    app.register_error_handler(404, home.error_pages)
    app.register_error_handler(500, home.error_pages)

    # Add your Url rules here
    app.add_url_rule('/', view_func=home.index)
    app.add_url_rule('/register', view_func=user.register, methods=['GET','POST'])
    app.add_url_rule('/login', view_func=user.login, methods=['GET','POST'])
    app.add_url_rule('/logout', view_func=user.logout)
    app.add_url_rule('/char/create', view_func=character.create_char, methods=['GET','POST'])
    app.add_url_rule('/char/edit', view_func=character.edit_char, methods=['GET','POST'])
    app.add_url_rule('/char/delete', view_func=character.delete_char, methods=['GET'])
    app.add_url_rule('/char', view_func=character.view_char, methods=['GET','POST'])
    app.add_url_rule('/class/create', view_func=_class.create_class, methods=['GET','POST'])
    app.add_url_rule('/class', view_func=_class.view_class, methods=['GET','POST'])
    app.add_url_rule('/class/edit', view_func=_class.edit_class, methods=['GET','POST'])
    app.add_url_rule('/class/delete', view_func=_class.delete_class, methods=['GET'])


