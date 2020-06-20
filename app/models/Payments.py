from app import db
from datetime import datetime

class Payments(db.Model):
    __bind_key__ = 'payments'
    id=db.Column(db.Integer(),primary_key=True)
    bank_account_name=db.Column(db.String(256),index=True,nullable=False)
    bank_name=db.Column(db.String(128),index=True,nullable=False)
    exact_money=db.Column(db.Integer(),nullable=False)
    transfer_datetime=db.Column(db.String(128),nullable=False,index=True)
    order_id=db.Column(db.Integer(),nullable=False)

    def to_dict(self):
        data = {'id': self.id, 'bank_account_name': self.bank_account_name, 'bank_name': self.bank_name,
                'exact_money': self.exact_money, 'transfer_datetime': self.transfer_datetime,'order_id': self.order_id}
        return data

    def from_dict(self,data):
        for field in ['bank_account_name','bank_name','exact_money','transfer_datetime','order_id']:
            if field in data:
                setattr(self,field,data[field])

