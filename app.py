# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:04:41 2021

@author: VISHAL
"""

#%%

#importing libraries:
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

#%%

app=Flask(__name__)

#%%

model=pickle.load(open('white_RF.pkl','rb'))

model1=pickle.load(open('red_RF.pkl','rb'))

#%%

@app.route('/')
def home():
    return render_template('home.html')


#%%
    
@app.route("/White", methods=['GET', 'POST'])
def White():
    if request.method == 'GET':
        return render_template('white-wine.html')
    
    if request.method =='POST':
        int_features=[float(x) for x in request.form.values()]
        final_features=[np.array(int_features)]
        prediction=model.predict(final_features)
        
        data2=request.form["fixed acidity"]
        data3=request.form["volatile acidity"]
        data4=request.form["citric acid"]
        data5=request.form["residual sugar"]
        data6=request.form["chlorides"]
        data7=request.form["free sulfur dioxide"]
        data8=request.form["total sulfur dioxide"]
        data9=request.form["density"]
        data10=request.form["pH"]
        data11=request.form["sulphates"]
        data12=request.form["alcohol"]
 
        
        #create original output dict
        output_dict= dict()
        output_dict['Fixed Acidity']=data2
        output_dict['Volatile Acidity']=data3
        output_dict['Citric Acid']=data4
        output_dict['Aesidual Augar']=data5
        output_dict['Ahlorides']=data6
        output_dict['Free Sulfur Dioxid']=data7
        output_dict['Total Sulfur Dioxide']=data8
        output_dict['Density']=data9
        output_dict['pH']=data10
        output_dict['Sulphates']=data11
        output_dict['Alcohol']=data12
        
        
        return render_template('white-wine-result.html',original_input=output_dict,data=prediction)
#%%
    
@app.route("/Red", methods=['GET', 'POST'])
def Red():
    
    if request.method == 'GET':
        return render_template('red-wine.html')
    
    if request.method =='POST':
        
        int_features=[float(x) for x in request.form.values()]
        final_features=[np.array(int_features)]
        prediction=model1.predict(final_features)
        
        
        data2=request.form["fixed acidity"]
        data3=request.form["volatile acidity"]
        data4=request.form["citric acid"]
        data5=request.form["residual sugar"]
        data6=request.form["chlorides"]
        data7=request.form["free sulfur dioxide"]
        data8=request.form["total sulfur dioxide"]
        data9=request.form["density"]
        data10=request.form["pH"]
        data11=request.form["sulphates"]
        data12=request.form["alcohol"]
 
        
        #create original output dict
        output_dict= dict()
        output_dict['Fixed Acidity']=data2
        output_dict['Volatile Acidity']=data3
        output_dict['Citric Acid']=data4
        output_dict['Aesidual Augar']=data5
        output_dict['Ahlorides']=data6
        output_dict['Free Sulfur Dioxid']=data7
        output_dict['Total Sulfur Dioxide']=data8
        output_dict['Density']=data9
        output_dict['pH']=data10
        output_dict['Sulphates']=data11
        output_dict['Alcohol']=data12
        
    
        return render_template('red-wine-result.html',original_input=output_dict,data=prediction)
#%%
    
if __name__=='__main__':
    app.run(debug=True)
