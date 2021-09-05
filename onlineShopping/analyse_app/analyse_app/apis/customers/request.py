"""
Handles requests trelated o Customer
"""
from .customers import Customers
from fastapi import FastAPI, Depends, status, Response, HTTPException
from database import session_helper
from sqlalchemy.orm import Session


def entry_point(app):
    """
    Handles api requests related to Customer details

    :param app: FastApi app
    :return: Query response
    """
    @app.post("/customers")
    def calculate_revenue(customer: Customers, response: Response,
                          session: Session = Depends(session_helper.get_session)):
        validation_error_result = customer.validation_execution()

        if any(validation_error_result):
            error_message = ";".join(validation_error_result)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)

        try:
            execution_result = customer.method_execution(session)
            return execution_result

        except NotImplementedError:
            raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented. Please contact")

        except Exception as exc:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=exc)
