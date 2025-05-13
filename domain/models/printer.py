class printer:

    def __int__(self, brand, reference, serial, counter, price, ref_toner, origin, place_storage, status):
        self._brand = brand
        self._reference = reference
        self._serial = serial
        self._counter = counter
        self._price = price
        self._ref_toner = ref_toner
        self._origin = origin
        self._place_storage = place_storage
        self._status = status

    ## _brand
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    ## _reference
    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    ## _serial
    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, serial):
        self._serial = serial

    ## _counter
    @property
    def counter(self):
        return self._counter

    @counter.setter
    def brand(self, counter):
        self._counter = counter

    ## _price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    ## _ref_toner
    @property
    def ref_toner(self):
        return self._ref_toner

    @ref_toner.setter
    def ref_toner(self, ref_toner):
        self._ref_toner = ref_toner

    ## _origin
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        self._origin = origin

    ## _place_storage
    @property
    def place_storage(self):
        return self._place_storage

    @place_storage.setter
    def place_storage(self, place_storage):
        self._place_storage = place_storage

    ## _status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
