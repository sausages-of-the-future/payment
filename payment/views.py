from flask import Flask, request, redirect, render_template, url_for, session, flash, abort, current_app
from payment import app, forms
from urllib.parse import urlparse

def allowed_domain(return_uri):
    allowed_domains = app.config['ALLOWED_DOMAINS'].split(',')
    parsed_uri = urlparse(return_uri)
    return parsed_uri.netloc in allowed_domains

#filters
@app.template_filter('format_money')
def format_money_filter(value):
    return "{:,.2f}".format(value)

#views
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/error")
def error():
    return render_template('error.html')

@app.route("/start", methods=['POST'])
def start():
    session.clear()
    order = {
            "total": float(request.form.get('total', 0)),
            "description": request.form.get('description', ''),
            "service": request.form.get('service', 0), 
            "email":  request.form.get('email', ''),
            "return_uri": request.form.get('return_uri', '')
            }

    session['order'] = order
    return redirect(url_for('pay'))

@app.route("/method", methods=['POST', 'GET'])
def method():
    """Fake page, always send user to card payment"""
    form = forms.MethodForm(request.form)
    if request.method == 'POST':
        return redirect('pay')
    else:
        return render_template('method.html', form=form)

@app.route("/pay", methods=['POST', 'GET'])
def pay():
    order = session.get('order', False)
    if not order:
        return redirect(url_for('error'))

    form = forms.PaymentForm(request.form)

    if request.method == 'POST':
        if form.validate():
            if allowed_domain(order['return_uri']):
                return redirect(order['return_uri'])
            else:
                return redirect(url_for('error'))
    return render_template('pay.html', form=form, order=order)

