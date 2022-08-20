class PSSInternalError(Exception):
    def __init__(self, descriptions: str):
        self.descriptions = descriptions

    def __repr__(self):
        return f"PSSI: {self.descriptions}"

    __str__ = __repr__


class PSSRuntimeError(PSSInternalError): ...
