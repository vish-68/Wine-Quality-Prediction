# Wine-Quality-Prediction## Conclusion
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

## Data Analysi
In Iris dataset we are provided 73 features(including target 
variable) and 855969 records.

* fixed acidity
* volatile acidity
* citric acid
* residual sugar
* chlorides
* free sulfur dioxide
* total sulfur dioxide
* density
* pH
* sulphates
* alcohol
* quality (score between 0 and 10)

## Approach
Our Main goal is to know whether the wine is good or bad quality.
* Data Exploration : Exploring dataset using pandas,numpy,matplotlib and seaborn.
* Data visualization : Use Tableau Data visualizationtools and also Ploted graphs to get insights about dependend and independed variables.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : After testing all base if some of them are not working properly then we have to do model tunning
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Herokuapp 

## Technologies Used
* Jupyter notebook, Spyder, VScode Is Used For IDE.
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Herokuapp is Used For Model Deployment.
* Front End Deployment Is Done Using HTML, CSS, Bootstrap.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* os is used for creating and deleting folders.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model
* Logistic regression is used for LogisticRegression Implementation.
* SGD is used for SGDClassifier Implementation.
* K-Nearest Neighbors is used for KNeighborsClassifier Implementation.
* SVM is used for SVC Implementation.
* Decision Tree is used for DecisionTreeClassifier Implementation.
* Extra Trees is used for ExtraTreesClassifier Implementation.
* Random forest is used for RandomForestClassifier Implementation.
* Ada boost is used for AdaBoostClassifier Implementation.
* Gradient is used for GradientBoostingClassifier Implementation.
* XGboost is used for XGBClassifier Implementation
* Ensemble is used for VotingClassifier Implementation.

## Deployment
**Herokuapp Link:** https://wines-quality-predictions.herokuapp.com/
  
## Deployment
To Clone this project run
```bash
git clone https://github.com/vish-68/Wine-Quality-Prediction
```
Go to Project directory
```bash
cd Wine-Quality-Prediction
```
Install dependencies
``` bash
pip install -r requirements.txt
```  
Run the app.py
```bash
python app.py
```

## Conclusion
We have developed Wine Quality Predictive model which is capable for predicting wheater the wine is of good quality or bad quality. In this dataset we have 12 features(including target variable). 

* First step is to check wheater the dataset contain missing values or not. We have drop those Features which has more than 50% of missing values. And one who is less than 50% those variable should be treated using fillna mode(for categorical variable) and mean(for numerical variable). Second step is to do some data visualization to get some insight from given data after handling missing values. We can plot Countplot for checking imbalanced dataset, Pairplot to undestand data, Co-relation plot for auto-corelation and boxplot for outliers detection. So here we handel some outliers. Then We have to converting categorical variable to numerical variable after converting categorical to numerical we have to do scaling, we perform Standard Scalar(values lies between -3 to +3) and then we have to build ML model likes LogisticrRegression, SGDClassifier, KNeighborsClassifier, SVR, DecisionTreeRClassifier, ExtraTreesClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier, XGBClassifier. Out of all of them ExtraTeeClassifier and RandomForest was working good because Accuracy achieved – 81.67%. So here we can say RandomForest model is working good. Last step is model Deployment using Flask Framework. For model deployment we have to dump our model using pickle library and can save our model in .pkl or .sav extension