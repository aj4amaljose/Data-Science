from .customers import Customers
from fastapi import FastAPI, Depends, status, Response, HTTPException
from analyse_app.analyse_app.database import session_helper
from sqlalchemy.orm import Session


def entry_point(app):
    @app.post("/customers")
    def calculate_revenue(customer: Customers, session: Session = Depends(session_helper.get_session)):
        try:
            return customer.method_execution(session)
        except Exception as exc:
            print(exc)