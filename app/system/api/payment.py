from .enums.pay_status import PaymentStatus
from .error.internal import PSSRuntimeError
from ..models.payment import Payment as PaymentModel


class Payment:
    def __init__(self, uuid: str):
        self._model_link: PaymentModel = PaymentModel.query.filet(PaymentModel.uuid == uuid).first()

        if self._model_link is None:
            raise PSSRuntimeError("Payment Not Found!")

    @property
    def status(self) -> PaymentStatus:
        return PaymentStatus(self._model_link.status)