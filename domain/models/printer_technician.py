from domain.models.print_client import client

class technician:

    def __int__(self, id, name, last_name, phone, email, status, occupation):
        super().__init__(id, name, last_name, phone, email, status)
        self._occupation = occupation

    ## _occupation
    @property
    def occuation(self):
        return self._occupation
    @occuation.setter
    def occupation(self, occupation):
        self._occupation = occupation