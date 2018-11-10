import app.data.data_parser as dp
from sklearn.externals import joblib

subjects = ["Art", "Citizenship_Education", "English", "Geography", "Health", "History", "Mathematics", "PTS",
            "Religion", "Science", "Sinhala", "Tamil"]


def get_prediction_marks(df, subject):
    xgb_regressor = joblib.load('joblibs/xgb/' + subject + '_xgb.joblib')
    return xgb_regressor.predict(df)


def get_prediction(df):
    for subject in subjects:
        df = dp.generate_dataset(df, [subject])

        return {
            "Sinhala": get_prediction_marks(df, subject),
            "Maths": get_prediction_marks(df, subject),
            "Science": get_prediction_marks(df, subject),
            "Art": get_prediction_marks(df, subject),
            "Dance": get_prediction_marks(df, subject),
            "Buddhism": get_prediction_marks(df, subject),
            "History": get_prediction_marks(df, subject),
            "Tamil": get_prediction_marks(df, subject),
            "English": get_prediction_marks(df, subject),
            "Geology": get_prediction_marks(df, subject),
            "LearningStyle": 2
        }
