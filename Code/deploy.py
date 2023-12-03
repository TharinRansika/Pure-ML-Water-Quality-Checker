from flask import Flask , render_template , request
import pickle #Importing the relevant Libraries
import joblib as joblib
import os



app = Flask(__name__ ) #Create Flask application Instance


# file_path = os.path.join(os.getcwd(), 'saved_model.pkl')
 
# file_path1 =os.path.join(os.getcwd(), 'saved.sav') 
# model = pickle.load(open(file_path, 'rb'))#Loading the model

# model = pickle.load(open('saved_model.pkl' , 'rb'))
# model = joblib.load('saved_model1.pkl')
with open('saved_model1.pkl', 'rb') as file:
    model = pickle.load(file)



# model = pickle.load(open('/home/Romold123/mysite/saved_model.sav', 'rb'))




@app.route('/') #Flask route to render Home page
def home():
    
  
    return render_template('Home.html', **locals())

@app.route('/Form.html') #Flask route to render Form
def form():
    
    
    return render_template('Form.html')

@app.route('/portability' , methods = ['POST' , 'GET']) #Flask route to render form result 
def portability():
    
    ph = float(request.form['ph']) #converting form field data to floating point numbers
    hardness = float(request.form['hardness'])
    solids = float(request.form['solids'])
    chloramines = float(request.form['chloramines'])
    sulfate = float(request.form['sulfate'])
    conductivity = float(request.form['conductivity'])
    organic_carbon = float(request.form['organic_carbon'])
    trihalomethanes = float(request.form['trihalomethanes'])
    turbidity = float(request.form['turbidity'])
    
    #Making prediction based on input feature values
    result = model.predict([[ph , hardness , solids , chloramines , sulfate , conductivity , organic_carbon , trihalomethanes , turbidity]])
    
    if result == 1: #If result == 1 render portable success page 
        
        return render_template('potablesuccess.html')
    else:
        return render_template('potableunsuccess.html')
    
@app.route('/Tips.html') #Flask route to render Tips
def tips():
    
    return render_template('Tips.html')

@app.route('/Home.html') #Flask route to return to Home page
def home1():
    
    return render_template('Home.html')

if __name__ == '__main__': #Start the flask application with debugging
    
    app.run(debug=True)
    
    

