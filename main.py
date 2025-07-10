from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {k: request.form[k] for k in ['name','phone','company','invoice','amount','date']}
        message = (
            f"Hi {data['name']},\n\n"
            "Thank you for your payment! 🙏\n\n"
            f"✅ Payment Successful\n"
            f"🧾 Invoice Number: {data['invoice']}\n"
            f"💰 Amount Paid: ₹{data['amount']}\n"
            f"📅 Date: {data['date']}\n\n"
            f"- {data['company']}"
        )
        encoded = urllib.parse.quote(message)
        phone = data['phone'].strip().replace("+91","").replace(" ","")
        return redirect(f"https://wa.me/91{phone}?text={encoded}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
