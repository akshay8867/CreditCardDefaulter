import os
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
from predictFromModel import prediction

from flask import Flask, request, render_template
from flask import Response
from flask_cors import CORS, cross_origin

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')
app = Flask(__name__)

CORS(app)
@app.route("/predict",methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.json is not None:
            path=request.json['filepath']
            pred_val=pred_validation(path)
            pred_val.prediction_validation()
            pred=prediction(path)
            path=pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)
        else:
            return Response("invalid file path")
    except ValueError:
        return Response("Error occured {}".format(ValueError))
    except KeyError:
        return Response("Error occured {}".format(KeyError))
    except Exception as e:
        return Response("Error occured {}".format(e))


@app.route("/train",methods=["POST"])
@cross_origin()
def trainRouteClient():
    try:
        if request.json is not None:
            path=request.json['filepath']
            train_valObj=train_validation(path)
            train_valObj.train_validation()
            trainModelObj = trainModel()
            trainModelObj.trainingModel()
            return Response('Successful End of Training')
        else:
            return Response("Invalid filepath")
    except ValueError:
        return Response("Error occured {}".format(ValueError))
    except KeyError:
        return Response("Error occured {}".format(KeyError))
    except Exception as e:
        return Response("Error occured {}".format(e))



port = int(os.getenv("PORT",5001))
if __name__ == "__main__":
    app.run(port=port,debug=True)
