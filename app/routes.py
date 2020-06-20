from flask import url_for,request,jsonify
from app import app,db
from app.models.Payments import Payments
from app.errors import bad_request

@app.route('/payments/<int:order_id>',methods=['GET'])
def get_payment(order_id):
    data = Payments.query.filter_by(order_id=order_id).first_or_404()
    return jsonify(data.to_dict())

@app.route('/payments/all',methods=['GET'])
def get_payments():
    payments = Payments.query.all()
    data={'Results':[]}
    for payment in payments:
        data['Results'].append(payment.to_dict())
    return jsonify(data)

@app.route('/payments/',methods=['POST'])
def post_payment():
    data = request.get_json() or {}
    if 'bank_account_name' not in data or 'bank_name' not in data or 'exact_money' not in data or 'transfer_datetime' not in data or\
        'order_id' not in data:
        return bad_request('Transfer Payment Proof needs to be in data')
    payment = Payments()
    payment.from_dict(data)
    db.session.add(payment)
    db.session.commit()
    response=jsonify(payment.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('get_payment',order_id=payment.order_id)
    return response

@app.route('/payments/<int:order_id>',methods=['DELETE'])
def delete_payment(order_id):
    payment = Payments.query.filter_by(order_id=order_id).first_or_404()
    data = payment.to_dict()
    response=jsonify(data)
    response.status_code = 200
    response.headers['Location'] = url_for('get_payment',order_id=payment.order_id)
    db.session.delete(payment)
    db.session.commit()
    return response

