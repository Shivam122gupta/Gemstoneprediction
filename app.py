# from flask import Flask,request,render_template
# import numpy as np
# import pandas as pd

# from sklearn.preprocessing import StandardScaler
# from src.pipeline.predict_pipeline import CustomData,PredictPipeline

# application =  Flask(__name__)
# app = application

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_datapoint():
#     if request.method=='GET':
#         return render_template('home.html')
#     else:
#         data = CustomData(
#             carat = float(request.form.get('carat')),
#             depth = float(request.form.get('depth')),
#             table = float(request.form.get('table')),
#             x = float(request.form.get('x')),
#             y = float(request.form.get('y')),
#             z = float(request.form.get('z')),
#             cut = request.form.get('cut'),
#             color= request.form.get('color'),
#             clarity = request.form.get('clarity')
#         )
#         pred_df = data.get_data_as_dataframe()
        
#         print(pred_df)

#         predict_pipeline = PredictPipeline()
#         pred = predict_pipeline.predict(pred_df)
#         results = round(pred[0],2)
#         return render_template('home.html',results=results,pred_df = pred_df)
    
# if __name__=="__main__":
#     app.run(host="0.0.0.0",debug=True)

from flask import Flask, request, render_template
import traceback

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    try:
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )

        pred_df = data.get_data_as_dataframe()

        print(pred_df)

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)

        results = round(pred[0], 2)

        return render_template(
            'home.html',
            results=results,
            pred_df=pred_df
        )

    except Exception:
        # Temporary debugging
        return f"<pre>{traceback.format_exc()}</pre>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)