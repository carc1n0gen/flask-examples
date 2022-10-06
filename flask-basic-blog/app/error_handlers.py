from flask import render_template


def create_error_handlers(app):
    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def unknown_error(e):
        return render_template('500.html'), 500
