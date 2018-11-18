from flask import jsonify, Flask, request
import os



app = Flask(__name__,template_folder='template')




@app.route("/run", methods=["GET"])
def gege():
    os.system("python image.py")
    return "d"






if __name__ == "__main__":
    """
    this is run when the script is started.
    """

    # this is how we run the flask server, once the script is run
    app.run(host='0.0.0.0',port=7575, threaded=True)