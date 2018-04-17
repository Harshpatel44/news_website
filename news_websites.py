from flask import *
import json
app = Flask(__name__)
import time
import thread
topics=['json/top','json/business','json/sports','json/tech','json/entertainment']
TEMPLATES_AUTO_RELOAD = True
app.config['DEBUG'] = True


content=[]
def looping():
    for i in topics:
         f=open(str(i)+".json",'r')
         data=json.load(f)
         # json.dump(top20)
         content.append(data)
         print(content)
         #print(content['headlines']['articles'][0]['title'])
    # raw_input()
    return content




@app.route('/',methods=['POST','GET'])
def main():
    return render_template('index.html')


@app.route('/data',methods=['POST','GET'])
def data():
    data=looping()
    return jsonify(data)

@app.route('/page',methods=['GET'])
def page():
    return render_template('for_get_post.html')




if __name__ == '__main__':
     app.run()
