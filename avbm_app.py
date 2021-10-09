import pandas as pd
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("AV_BM1.pkl")

@app.route('/')
def hi():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print(request.form.values())
    inp = [i for i in request.form.values()]

    try :
        for r in range(0,4) :
            if not isinstance(int(inp[r]), int):
                mess = "Please enter valid input"
                return render_template('index.html', prediction = mess)
    except :
        mess = "Please enter valid input"
        return render_template('index.html', prediction = mess)

    test = {"Item_Weight":inp[0],"Item_Visibility":int(inp[1]),"Item_MRP":int(inp[2]),"Age":int(inp[3])}
    print(test)
    test_df = pd.DataFrame([test])
    print(test_df)
    res = model.predict(test_df)
    print(res[0])
    #return str(res[0])
    if isinstance(res[0], float):
        mess = "Predicted Sales is {} ".format(str(res[0]))
    else:
        mess = "Please enter valid input"
    return render_template('index.html', prediction = mess)

if __name__ == "__main__":
    app.run(debug = True)
