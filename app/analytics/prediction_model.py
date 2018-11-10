import app.data.data_parser as dp
from sklearn.externals import joblib

subjects = ["Mathematics", "Art", "Science", "Sinhala", "Citizenship_Education", "English", "Geography", "Health", "History", "PTS",
            "Religion"]


def get_prediction_marks(df1, df2, subject):
    xgb_regressor = joblib.load('app/analytics/joblibs/xgb/' + subject + '_xgb.joblib')
    adb_classifier = joblib.load('app/analytics/joblibs/adb_clf/' + subject + '_adb.joblib')
    rnd_classifier = joblib.load('app/analytics/joblibs/adb_clf/' + subject + '_rnd.joblib')
    
    thresold = 55
    
    if(xgb_regressor.predict(df1)>thresold):
        return (xgb_regressor.predict(df1),rnd_classifier.predict(df2))
    else:
        return (xgb_regressor.predict(df1),adb_classifier.predict(df2))


def get_prediction(df):
    dict = {}
    for subject in subjects:
        df1 = dp.generate_dataset(df, [subject])
        df2 = dp.generate_dataset(df, [subject], discretize='yes')
        dict[subject] = get_prediction_marks(df1,df2,subject)

    return dict
