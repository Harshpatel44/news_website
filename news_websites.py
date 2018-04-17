from flask import *
import json
app = Flask(__name__)
import time
import thread
topics=['json/top','json/business','json/sports','json/tech','json/entertainment','json/politics','json/world']
TEMPLATES_AUTO_RELOAD = True
app.config['DEBUG'] = True


content=[]
def looping(index):

         f=open(str(topics[index])+".json",'r')
         data=json.load(f)
         # json.dump(top20)
         print(data)
         #print(content['headlines']['articles'][0]['title'])
        # raw_input()
         return data




@app.route('/',methods=['POST','GET'])
def main():
    return render_template('index.html')


@app.route('/top',methods=['POST','GET'])
def top():
    data=looping(0)
    return jsonify(data)

@app.route('/ent',methods=['POST','GET'])
def ent():
    data=looping(4)
    return jsonify(data)

@app.route('/spo',methods=['POST','GET'])
def spo():
    data=looping(2)
    return jsonify(data)

@app.route('/tec',methods=['POST','GET'])
def tec():
    data=looping(3)
    return jsonify(data)

@app.route('/pol',methods=['POST','GET'])
def pol():
    data=looping(5)
    return jsonify(data)

@app.route('/world',methods=['POST','GET'])
def world():
    data=looping(6)
    return jsonify(data)

@app.route('/bus',methods=['POST','GET'])
def bus():
    data=looping(1)
    return jsonify(data)

@app.route('/page',methods=['GET'])
def page():
    return render_template('for_get_post.html')




if __name__ == '__main__':
     app.run()
