import app.data.data_parser as dp
from sklearn.externals import joblib
import app.analytics.learning_prediction as lp

subjects = ["Mathematics", "Art", "Science", "Sinhala", "Citizenship_Education", "English", "Geography", "Health", "History", "PTS",
            "Religion"]


def get_prediction_marks(df, subject):
    xgb_regressor = joblib.load('app/analytics/joblibs/xgb/' + subject + '_xgb.joblib')
    return xgb_regressor.predict(df)


def get_prediction(df):
    dict = {}
    for subject in subjects:
        df1 = dp.generate_dataset(df, [subject])
        dict[subject] = get_prediction_marks(df1, subject)

        dict["learning_style"] = lp.get_learning_styles(df)

        print(dict)

    return dict
