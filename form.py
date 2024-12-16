from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
def is_north(value):
    # Definition of the function that was used during training
    pass
from wtforms.validators import DataRequired

# train = pd.read_csv("Data/Train.csv", encoding='utf-8')
# val = pd.read_csv("Data/Validation.csv", encoding='utf-8')
#
# x_data = pd.concat([train, val], axis=0).drop(columns="price")


class InputForm(FlaskForm):
    airline = SelectField(
        label="AIRLINE",
        choices=[
            ('IndiGo', 'IndiGo'),
            ('Air India', 'Air India'),
            ('SpiceJet', 'SpiceJet'),
            ('Jet Airways', 'Jet Airways'),
            ('Multiple carriers', 'Multiple carriers'),
            ('Air Asia', 'Air Asia'),
            ('Vistara', 'Vistara'),
            ('GoAir', 'GoAir')
        ],
        validators=[DataRequired()]
    )
    date_of_journey = DateField(
        label="DATE OF JOURNEY",
        validators=[DataRequired()]
    )
    source = SelectField(
        label="SOURCE",
        choices=[
            ('Delhi', 'Delhi'),
            ('Mumbai', 'Mumbai'),
            ('Kolkata', 'Kolkata'),
            ('Banglore', 'Banglore'),
            ('Chennai', 'Chennai')
        ],
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="DESTINATION",
        choices=[
            ('Cochin', 'Cochin'),
            ('Hyderabad', 'Hyderabad'),
            ('Banglore', 'Banglore'),
            ('New Delhi', 'New Delhi'),
            ('Kolkata', 'Kolkata'),
            ('Delhi', 'Delhi')
        ],
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        label="DEPARTURE TIME",
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="ARRIVAL TIME",
        validators=[DataRequired()]
    )
    duration = IntegerField(
        label="DURATION",
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        label="TOTAL STOPS",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="ADDITIONAL INFORMATION",
        choices=[
            ('No Info', 'No Info'),
            ('In-flight meal not included', 'In-flight meal not included'),
            ('No check-in baggage included', 'No check-in baggage included'),
            ('Change airports', 'Change airports'),
            ('1 Long layover', '1 Long layover'),
            ('1 Short layover', '1 Short layover'),
            ('Business class', 'Business class'),
            ('2 Long layover', '2 Long layover')
        ],
        validators=[DataRequired()]
    )
    Class = SelectField(
        label="CLASS",
        choices=[
            ('Economy', 'Economy'),
            ('Premium economy', 'Premium economy'),
            ('Business', 'Business')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField("PREDICT")

