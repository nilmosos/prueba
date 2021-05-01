from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   case = StringField('Case')
   symptoms_start_date = StringField('Symptom onset date')
   diagnosys_date = StringField('Date of Diagnosis')
   city = StringField('City')
   locality = StringField('Locality')
   age = IntegerField('Age')
   age_unit = StringField('Age unit')
   sex = StringField('Sex')
   contagion_type = StringField('Contagion type')
   current_location = StringField('Current location')
   submit = SubmitField('Predict')
   abc = "" # this variable is used to send information back to the front page
