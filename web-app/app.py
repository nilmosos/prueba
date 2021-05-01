from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        #API_KEY = "<IBM Cloud API key>"    #Select Account > Users, go to Manage > Access (IAM) > API keys.
        API_KEY = "GjBEDX7Pq5jMNaP97G9XbYDX_nhU2EO3HOgRvYibRFg6"
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        if( form.case.data == None and form.symptoms_start_date.data == None  and form.diagnosys_date.data == None  and 
            form.city.data == None  and form.locality.data == None  and  form.age.data == None  and  form.age_unit.data == None  and  form.sex.data == None  and 
            form.contagion_type.data == None  and  form.current_location.data == None ): 
          python_object = []
        else:
          python_object = [form.case.data, form.symptoms_start_date.data, form.diagnosys_date.data,
            form.city.data, form.locality.data, form.age.data, form.age_unit.data, form.sex.data,
            form.contagion_type.data, form.current_location.data ]
        #Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["case", "symptoms_start_date", "diagnosys_date",
          "city", "locality", "age", "age_unit", "sex", "contagion_type", "current_location" ], "values": userInput }]}

        print(payload_scoring)
        # response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/<deployment-id-goes-here>/predictions?version=<DATE>", json=payload_scoring, headers=header)
        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2aa265c9-4684-4ae6-8d75-fd998592f5b8/predictions?version=2021-04-30', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})

        output = json.loads(response_scoring.text)
        print("Salida")
        print(output)
        print("Salida")


        form.abc = ""
        if 'predictions' in output.keys():
          ab = output['predictions']
          for key in ab[0]:
            bc = ab[0][key]
          # form.abc = roundedCharge # this returns the response back to the front page
          form.abc = bc[0][0] # this returns the response back to the front page
        
        return render_template('index.html', form=form)