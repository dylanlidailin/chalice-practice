from chalice import Chalice

app = Chalice(app_name='sample-api')

@app.route('/')
def index():
    return {'hello': 'sophia'}

@app.route('/dailin')
def index():
    return {' hello': 'yourself'}
