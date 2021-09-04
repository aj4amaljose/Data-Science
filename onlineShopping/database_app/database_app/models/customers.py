from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import INTEGER, FLOAT, TEXT

Base = declarative_base()


class Customers(Base):
    """
    Details of locations and people where tracking is enabled
    """
    __tablename__ = "Customers"
    customer_id = Column(TEXT, primary_key=True)
    sacc_items = Column(INTEGER)
    work_orders = Column(INTEGER)
    female_items = Column(INTEGER)
    is_newsletter_subscriber = Column(TEXT)
    male_items = Column(INTEGER)
    afterpay_payments = Column(INTEGER)
    msite_orders = Column(INTEGER)
    wftw_items = Column(INTEGER)
    mapp_items = Column(INTEGER)
    orders = Column(INTEGER)
    cc_payments = Column(INTEGER)
    curvy_items = Column(INTEGER)
    paypal_payments = Column(INTEGER)
    macc_items = Column(INTEGER)
    cancels = Column(INTEGER)
    revenue = Column(FLOAT)
    returns = Column(INTEGER)
    other_collection_orders = Column(INTEGER)
    parcelpoint_orders = Column(INTEGER)
    android_orders = Column(INTEGER)
    days_since_last_order = Column(INTEGER)
    vouchers = Column(INTEGER)
    average_discount_used = Column(FLOAT)
    shipping_addresses = Column(INTEGER)
    mftw_items = Column(INTEGER)
    days_since_first_order = Column(INTEGER)
    unisex_items = Column(INTEGER)
    home_orders = Column(INTEGER)
    desktop_orders = Column(INTEGER)
    ios_orders = Column(INTEGER)
    apple_payments = Column(INTEGER)
    wspt_items = Column(INTEGER)
    wacc_items = Column(INTEGER)
    items = Column(INTEGER)
    mspt_items = Column(INTEGER)
    devices = Column(INTEGER)
    different_addresses = Column(INTEGER)
    wapp_items = Column(INTEGER)
    other_device_orders = Column(INTEGER)
    average_discount_onoffer = Column(FLOAT)
