from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route('/add_two', methods=["POST"])
def add_two():
    data = request.get_json()
    x = data["x"]
    y = data["y"]
    z = x + y
    retJson = {
        "z" : z,
        "slogan" : "quality is never a consideration at CITI app support!",
        "status" : "++Mike Corbat"
    }
    return jsonify(retJson)

@app.route('/')
def hola():
    return '''
    <img src="https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2012/andromedawan.jpg">
    '''
@app.route('/tallwhites')
def tallwhites():
    return '''
    <img src="http://proofofalien.com/wp-content/uploads/2016/03/Tall-White-Aliens.jpg">
    '''
@app.route('/greys')
def greys():
    return '''
    <img src="https://www.ufointernationalproject.com/wp-content/uploads/2015/05/a1111.jpg">
    '''
@app.route('/earth')
def earth():
    return '''
    <img src="https://ak8.picdn.net/shutterstock/videos/1672888/thumb/1.jpg">
    '''
@app.route('/bye')
def bye():
    retJson = {
    'speciesA': 'Tall Whites',
    'speciesB': 'Greys',
    'galaxy': 'Andromeda',
    'myHome': 'Earth'
        }
    return jsonify(retJson)


if __name__ == "__main__":
    app.run(debug=True)
