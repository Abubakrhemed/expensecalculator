from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_expenses(rent, food, wifi, misc):
    expenses = [rent, food, wifi, misc]
    sum_total = sum(expenses)
    return sum_total

def calculate_savings(income, savings):
    savings_total = float(income) + float(savings)
    return savings_total

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        income = float(request.form['income'])
        savings = float(request.form['savings'])
        rent = float(request.form['rent'])
        food = float(request.form['food'])
        wifi = float(request.form['wifi'])
        misc = float(request.form['misc'])

        total_expenses = calculate_expenses(rent, food, wifi, misc)
        total_savings = calculate_savings(income, savings)
        remaining_money = total_savings - total_expenses

        if total_expenses > total_savings:
            message = "You should probably consider not moving out."
        else:
            message = "You can consider moving out."

        return render_template('index.html', 
                               total_expenses=total_expenses,
                               total_savings=total_savings,
                               remaining_money=remaining_money,
                               message=message)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
