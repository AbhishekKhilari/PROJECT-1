# PROJECT-1
This project contains building up a model and predict the Temperature of the Rotor of a PMSM.
Here, the dataset provided by was big (133 mb) so was not able to upload here.
The Dataset provided here was preprocessed and was scaled with the StandardScaler.
The observatiopns in this were taken in sessions (as can be noticed by profile_id column).
The first task here was to check the distribution of the features and check wheather which model is more suitable for it.
From the distributions of features it seems that linear regression won't be good model.
It was further checked from the qq plot and Kolmogorov-Smirnov test where our it proved that our intuition was correct.So, we moved towards non-parametric models.
The non-parametric models which were compared with each other for model selection were KNN , Decision Tree and Random Forest.
The Random Forest model was selected based on the values of rmse and r2 values
The Final prt of the project was deployment of the model which was done via streamlit.(you can the check the .py file attached for deployment codes)

