from bottle import route, error, run, static_file, template, request
from sys import argv

@route('/')
def index():
    return template('index')
@route('/myndir')
def myndir():
    par1=request.query.param1
    par2=request.query.param2
    return "<h1>Þú val " + par1 + " " + par2 + "</h1>"
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')
@error(404)
def error404(error):
    return 'Nothing here, sorry'
run(host='0.0.0.0', port=argv[1], debug=True, reloader=True)