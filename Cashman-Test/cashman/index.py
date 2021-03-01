from flask import Flask, jsonify, request

from model.expenses import Expense, ExpenseSchema
from model.income import Income, IncomeSchema
from model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
  Income('Salary', 5000),
  Income('Dividends', 200),
  Expense('Food-daily', 50),
  Expense('Rock Concert', 100)
]


@app.route('/incomes', methods = ['GET'])
def get_incomes():
    schema = IncomeSchema(many = True)
    incomes = schema.dump( filter (lambda t: t.type == TransactionType.INCOME, transactions) )
    return jsonify(incomes)
    #return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return 'Added successfully', 200

@app.route('/expenses', methods = ['GET'])
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump( filter(lambda t: t.type == TransactionType.EXPENSE, transactions) )
    return jsonify(expenses)
    #return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expense():
  expense = ExpenseSchema().load(request.get_json())
  transactions.append(expense)
  return "Added Successfully", 200

if __name__ == "__main__":
    app.run(debug = True)