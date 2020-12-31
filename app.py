import pymongo
from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static2')


# Времени хватило лишь на вывод списка произведения вместе с картинками и авторами, на информацию не хватило
@app.route('/')
def index():
    collection = mongo()
    cursor = list(collection.find({}))
    for i in range(len(cursor)):
        try:
            cursor[i]['data']['images']
        except:
            cursor[i]['data']['images'] = ''
        try:
            cursor[i]['data']['authors']
        except:
            cursor[i]['data']['authors'] = ''
        else:
            cursor[i]['data']['authors'] = ", ".join(cursor[i]['data']['authors'])

    return render_template('index.html', cursor=cursor, len=len(cursor))


@app.route('/about')
def about():
    return render_template('about.html')


def mongo():
    client = pymongo.MongoClient('mongodb://st:askldjwq@185.93.109.237:27019/?authSource=goscatalog')
    db = client.goscatalog
    collection = db.things
    return collection
