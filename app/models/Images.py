from app import db

class Images(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    filename = db.Column(db.String(256),nullable=False,index=True,unique=True)
    title = db.Column(db.String(256),nullable=False,index=True,unique=True)
    author = db.Column(db.String(128),nullable=False,index=True)
    booktype = db.Column(db.String(20),nullable=False,index=True)
    price = db.Column(db.Integer(),nullable=False)

    def to_dict(self):
        data={'filename': self.filename, 'title': self.title, 'author': self.author, 'booktype': self.booktype,
              'price': self.price}
        return data

    def from_dict(self,data):
        for field in ['filename','title','author','booktype','price']:
            if field in data:
                setattr(self,field,data[field])
