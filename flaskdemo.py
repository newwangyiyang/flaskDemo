"""
    第一份python  Web代码
"""

from app import create_app, register_blueprint

app = create_app()
register_blueprint(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=app.config['DEBUG'])







