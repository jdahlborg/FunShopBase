from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, ForeignKey
from decimal import Decimal

db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category", lazy="select"
    )


class Product(db.Model):
    __tablename__= "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)

    category: Mapped["Category"] = relationship(
        "Category", back_populates="products", lazy="select"
    )


def seedData(db:SQLAlchemy):
    categorys = Category.query.all()
    if not categorys:
        c1 = Category(name='Mejeri')
        c2 = Category(name='Bakverk')
        c3 = Category(name='Frukt')
        c4 = Category(name='Grönsaker')
        c5 = Category(name='Svamp')
        c6 = Category(name='Spanmål')

        db.session.add_all([c1,c2,c3,c4,c5,c6])
        db.session.commit()

        # Produkter

        p1 = Product(name='Mjölk', price=Decimal('11.95'), category_id=c1.id)
        p2 = Product(name='Grädde', price=Decimal('29.99'), category_id=c1.id)
        p3 = Product(name='Keso', price=Decimal('23.50'), category_id=c1.id)

        p4 = Product(name='Limpa', price=Decimal('33.00'), category_id=c2.id)
        p5 = Product(name='Formfranska', price=Decimal('24.59'), category_id=c2.id)
        p6 = Product(name='Fralla', price=Decimal('8.90'), category_id=c2.id)
        p7 = Product(name='Tekaka', price=Decimal('6.45'), category_id=c2.id)

        p8 = Product(name='Äpple', price=Decimal('9.50'), category_id=c3.id)
        p9 = Product(name='Päron', price=Decimal('11.90'), category_id=c3.id)
        p10 = Product(name='Appelsin', price=Decimal('14.50'), category_id=c3.id)
        p11 = Product(name='Mango', price=Decimal('20.0'), category_id=c3.id)
        p12 = Product(name='Ananans', price=Decimal('29.50'), category_id=c3.id)

        p13 = Product(name='Tomat', price=Decimal('4.40'), category_id=c4.id)
        p14 = Product(name='Sallad', price=Decimal('12.60'), category_id=c4.id)
        p15 = Product(name='Gurka', price=Decimal('9.99'), category_id=c4.id)
        p16 = Product(name='Avokado', price=Decimal('16.79'), category_id=c4.id)

        p17 = Product(name='Champinjoner', price=Decimal('2.30'), category_id=c5.id)

        p18 = Product(name='Ris', price=Decimal('55.0'), category_id=c6.id)
        p19 = Product(name='Potatis', price=Decimal('9.50'), category_id=c6.id)
        p20 = Product(name='Pasta', price=Decimal('14.90'), category_id=c6.id)

        products = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]
        db.session.add_all(products)
        db.session.commit()