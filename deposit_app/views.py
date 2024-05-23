import pickle
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Deposit

# Load the fraud detection model
with open('fraud_detection_model.pkl', 'rb') as file:
    model = pickle.load(file)


def index(request):
    return render(request, 'index.html')


def deposit(request):
    if request.method == 'POST':
        form_data = request.POST
        username = form_data['username']
        user = User.objects.filter(username=username).first()

        if not user:
            messages.error(request, 'User not found!')
            return redirect('index')

        # Prepare input for the model
        input_data = {
            'user_id': user.id,
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

        if prediction == 1:
            messages.error(request, 'Fraudulent deposit detected!')
            return redirect('index')

        new_deposit = Deposit(
            user=user,
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

        messages.success(request, 'Deposit successful!')
        return redirect('index')

    return redirect('index')
