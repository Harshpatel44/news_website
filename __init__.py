from flask import render_template,Flask,jsonify
import json
app = Flask(__name__)
import content
import time
import thread
topics=['json/top','json/business','json/sports','json/tech','json/entertainment','json/politics','json/world','json/finance']
TEMPLATES_AUTO_RELOAD = True
app.config['DEBUG'] = True



def looping():     #continues in interval of 30s
     all_data2=[]
     # content.scrap_data()
     time.sleep(0.2)
     for i in topics:
         f=open(str(i)+".json",'r')
         data=json.load(f)
         content.scrap_data()
         all_data2.append(data)

         f.close()
     return all_data2

def first_time():  #for the first time when website loads
    all_data=[]
    for i in topics:
         time.sleep(0.1)
         f=open(str(i)+".json",'r')

         data=json.load(f)

         all_data.append(data)

         f.close()
    return all_data


@app.route('/responsive')
def responsive():
    return render_template('responsive.html')


@app.route('/',methods=['POST','GET'])
def main():
    print('main')

    return render_template('index.html')

@app.route('/first',methods=['GET','POST'])
def first():
    data=first_time()
    return jsonify(data)

@app.route('/top',methods=['POST','GET'])
def top():
    data=looping()
    return jsonify(data)

# @app.route('/ent',methods=['POST','GET'])
# def ent():
#     print('ent')
#     data=looping(4)
#     return jsonify(data)
#
# @app.route('/spo',methods=['POST','GET'])
# def spo():
#     print('spo')
#     data=looping(2)
#     return jsonify(data)
#
# @app.route('/tec',methods=['POST','GET'])
# def tec():
#     print('tec')
#     data=looping(3)
#     return jsonify(data)
#
# @app.route('/pol',methods=['POST','GET'])
# def pol():
#     print('pol')
#     data=looping(5)
#     return jsonify(data)
#
# @app.route('/world',methods=['POST','GET'])
# def world():
#     print('world')
#     data=looping(6)
#     return jsonify(data)
#
# @app.route('/bus',methods=['POST','GET'])
# def bus():
#     print('bus')
#     data=looping(1)
#     return jsonify(data)
#

@app.route('/page',methods=['GET'])
def page():
    return render_template('for_get_post.html')




if __name__ == '__main__':
     app.run(debug=True)
