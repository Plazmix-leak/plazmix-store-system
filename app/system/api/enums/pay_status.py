from enum import Enum


class PaymentStatus(Enum):
    CREATE = "create"
    WAIT = "wait"
    PAID = "paid"
    FAIL = "fail"
    CLOSE = "close"
