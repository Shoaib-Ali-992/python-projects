from flask import Flask, render_template, request

app = Flask(__name__)

# Account class
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def debit(self, amount):
        self.balance += amount
        return f"RS. {amount} was debited. Now total balance is RS. {self.balance}."

    def credit(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"RS. {amount} was credited. Now total balance is RS. {self.balance}."

    def get_balance(self):
        return self.balance

# Create a sample account
shoaib_acc = Account("shy134", 10000)


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        action = request.form.get("action")
        amount = int(request.form.get("amount", 0))

        if action == "debit":
            message = shoaib_acc.debit(amount)
        elif action == "credit":
            message = shoaib_acc.credit(amount)

    return render_template("index.html", account=shoaib_acc, message=message)


if __name__ == "__main__":
    app.run(debug=True)
