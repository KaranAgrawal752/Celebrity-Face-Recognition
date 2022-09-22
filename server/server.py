from flask import Flask, jsonify, request
import util

app=Flask(__name__)

@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    image_data=request.form['image_data']
    response=jsonify(util.classify_image(image_data))
    #response=jsonify(util.classify_image(util.get_b64_test_image_for_virat(),None))
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__=="__main__":
    print("Starting Python Flask Server for Sports celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)