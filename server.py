import os.path
from bottle import route, run, request, response, static_file
from sharksay import sharksay
from StringIO import StringIO
from subprocess import check_output

PORT = name = os.environ.get('PORT', 8080)
HOSTNAME = name = os.environ.get('HOSTNAME', 'localhost')
STATIC_ROOT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'static'
    )

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, STATIC_ROOT)

@route('/')
def write():
    root = os.path.dirname(os.path.abspath(__file__))
    return static_file('write.html', STATIC_ROOT)

@route('/say')
def say():
    message = request.query.message
    if not message:
        message = check_output('/usr/games/fortune')
    image = sharksay(message)
    response.content_type='image/png'
    buf = StringIO()
    image.save(buf, 'png')
    return buf.getvalue()

run(host=HOSTNAME, port=PORT)
