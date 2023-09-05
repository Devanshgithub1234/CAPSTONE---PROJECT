from flask import Flask , render_template , request
import titanicmodel
app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])

def basic():
    if request.method == 'POST':
        passenger_class = request.form['pclass']
        age = request.form['age']
        gender = request.form['gender']
        if gender == 'male':
            male = 1
            female = 0
        else:
            female = 1
            male = 0
        x_predict = [[passenger_class , age , female , male]]
        imported_model = titanic_model.trained_model()
        y_predict = imported_model,predict(x_predict)
        if y_predict == 0:
            flash('SORRY PASSENGER DID NOT SURVIVED' , 'danger')
        else:
            flash('CONGRATULATIONS PASSENGER IS SURVIVED' ,'success')
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'YOUR SECRET KEY'
    app.run(debug = True)