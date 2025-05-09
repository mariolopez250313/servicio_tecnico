class client:

    def __int__(self, id, name, last_name, phone, address, city, municipality,email, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._address = address
        self._city = city
        self._municipality = municipality
        self._email = email
        self._status = status

    ## _id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    ## _name
    @property
    def name(self):
        return self._name

    @id.setter
    def name(self, name):
        self._name = name

    ## _last_name
    @property
    def last_name(self):
        return self._last_name

    @id.setter
    def last_name(self, last_name):
        self._last_name = last_name

    ## _phone
    @property
    def phone(self):
        return self._phone

    @id.setter
    def phone(self, phone):
        self._phone = phone

    ## _address
    @property
    def address(self):
        return self._address

    @id.setter
    def address(self, address):
        self._address = address

    ## _city
    @property
    def city(self):
        return self._city

    @id.setter
    def city(self, city):
        self._city = city

    ## _municipality
    @property
    def municipality(self):
        return self._municipality

    @id.setter
    def municipality(self, municipality):
        self._municipality = municipality

    ## _email
    @property
    def email(self):
        return self._email

    @id.setter
    def email(self, email):
        self._email = email

    ## _status
    @property
    def status(self):
        return self._status

    @id.setter
    def status(self, status):
        self._status = status
