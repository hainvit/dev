from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
    return 'hello world ' + name


@app.route('/blogs/<int:post_id>')
def get_blogs_by_id(post_id):
    return 'get blogs by id: ' + str(post_id)


@app.route('/rev/<float:rev_no>')
def get_rev(rev_no):
    return 'rev no: ' + str(rev_no)


if __name__ == '__main__':
    app.run(debug=True)
