from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1><i>Post your concern hereee!!!</i></h1>'

@app.route('/food')
def my_favorite_food():
	    return 'My favorite food is pizza!'

@app.route('/user/<user_name>')
def show_user_name(user_name):
	return (user_name)

operator= (+,-,*,/)

@app.route('/calculator/num1,num2,operator')
def calculator(num1,num2,operator):
	result=""
	if operator == '*':
		result  = num1*num2
	else 
		return result



