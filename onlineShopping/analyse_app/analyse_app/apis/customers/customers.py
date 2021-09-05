from database_app.models.customers import Customers as CustomerModel
from pydantic import BaseModel, ValidationError, validator, Field
from fastapi import Query
from pydantic.typing import Optional
from enum import Enum
from sqlalchemy import func, and_, or_


class Method(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'


class Customers(BaseModel):
    function: str
    action: str
    data: Optional[dict] = Query(dict())

    @property
    def allowed_actions(self):
        return ["get_info", "query"]

    @property
    def function_map(self):
        return dict(get_info=dict(total_revenue_for_credit_card=self.method_total_revenue_for_credit_card,
                                  percentage_of_customers_purchased_female_items_credit_card=self.method_percentage_of_customers_purchased_female_items_credit_card,
                                  average_revenue_for_ios_or_android_or_desktop=self.method_average_revenue_for_ios_or_android_or_desktop,
                                  subscribed_and_men_and_unisex_customers=self.method_subscribed_and_men_and_unisex_customers

                                  ))

    def validation_execution(self):
        validation_error_result = []
        for vaidation in [self.validate_function, self.validate_action]:
            validation_result = vaidation()
            if validation_result:
                validation_error_result.append(validation_result)
        return validation_error_result

    def validate_function(self):
        result = None
        function_map = self.function_map.get(self.action)
        if function_map and self.function not in function_map:
            result = "Invalid 'function'. Allowed values are {}".format(function_map.keys())
        return result

    def validate_action(self):
        result = None
        if self.action not in self.allowed_actions:
            result = "Invalid 'action'. Allowed values are {}".format(self.allowed_actions)
        return result

    def method_execution(self, session):
        method = None
        if self.action == "get_info":
            method = self.function_map.get(self.method)
        elif self.action == "query":
            raise (NotImplementedError)
        else:
            pass
        result = dict(result=None, status="ok")

        if method:
            try:
                result = dict(result=method(session=session), status="ok")
            except Exception as e:
                result = dict(result=None, status="Error", details=str(e))
        return result

    @staticmethod
    def method_total_revenue_for_credit_card(session):
        result = session.query(func.sum(CustomerModel.revenue)).filter(
            CustomerModel.cc_payments > 0
        ).all()
        if result:
            return result[0][0]

    @staticmethod
    def method_percentage_of_customers_purchased_female_items_credit_card(session):

        customer_count_result = session.query(func.count(CustomerModel.customer_id)).all()
        female_items_credit_card_result = session.query(func.count(CustomerModel.customer_id)).filter(
            and_(CustomerModel.female_items > 0, CustomerModel.cc_payments > 0)
        ).all()
        if customer_count_result and female_items_credit_card_result:
            return female_items_credit_card_result[0][0] / customer_count_result[0][0]

    @staticmethod
    def method_average_revenue_for_ios_or_android_or_desktop(session):
        result = session.query(func.sum(CustomerModel.revenue)).filter(or_(
            CustomerModel.ios_orders > 0,
            CustomerModel.android_orders > 0,
            CustomerModel.desktop_orders > 0
        )).all()
        if result:
            return result[0][0]

    @staticmethod
    def method_subscribed_and_men_and_unisex_customers(session):
        result = None
        response = session.query(func.distinct(CustomerModel.customer_id)).filter(
            and_(CustomerModel.is_newsletter_subscriber == 'Y', or_(
                CustomerModel.male_items > 0,
                CustomerModel.unisex_items > 0),
                 )
        ).all()
        if response:
            result = {res[0] for res in response}

        return result
