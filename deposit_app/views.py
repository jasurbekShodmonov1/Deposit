import pickle
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Deposit

# Load the fraud detection model
with open('fraud_detection_model.pkl', 'rb') as file:
    model = pickle.load(file)

def welcome(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        return redirect('deposit_form', first_name=first_name, last_name=last_name)
    return render(request, 'welcome.html')

def deposit_form(request, first_name, last_name):
    return render(request, 'deposit_form.html', {'first_name': first_name, 'last_name': last_name})

def deposit(request):
    if request.method == 'POST':
        form_data = request.POST

        first_name = form_data['first_name']
        last_name = form_data['last_name']

        # Prepare input for the model
        input_data = {
            'job': form_data['job'],
            'marital': form_data['marital'],
            'education': form_data['education'],
            'default': form_data['default'],
            'housing': form_data['housing'],
            'loan': form_data['loan'],
            'contact': form_data['contact'],
            'month': form_data['month'],
            'day_of_week': form_data['day_of_week'],
            'duration': int(form_data['duration']),
            'campaign': int(form_data['campaign']),
            'pdays': int(form_data['pdays']),
            'previous': int(form_data['previous']),
            'poutcome': form_data['poutcome'],
            'amount': float(form_data['amount'])
        }

        input_df = pd.DataFrame([input_data])
        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

        prediction = model.predict(input_df)[0]

        context = {
            'first_name': first_name,
            'last_name': last_name,
        }

        if prediction == 1:
            context['result'] = 'fraud'
        else:
            new_deposit = Deposit(
                job=form_data['job'],
                marital=form_data['marital'],
                education=form_data['education'],
                default=form_data['default'],
                housing=form_data['housing'],
                loan=form_data['loan'],
                contact=form_data['contact'],
                month=form_data['month'],
                day_of_week=form_data['day_of_week'],
                duration=int(form_data['duration']),
                campaign=int(form_data['campaign']),
                pdays=int(form_data['pdays']),
                previous=int(form_data['previous']),
                poutcome=form_data['poutcome'],
                amount=float(form_data['amount'])
            )
            new_deposit.save()
            context['result'] = 'success'

        return render(request, 'result.html', context)
    return redirect('welcome')
