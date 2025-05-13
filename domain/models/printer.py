class printer:

    def __int__(self, brand, reference, serial, counter, price, ref_toner, stock, id_category, status):
        self._brand = brand
        self._reference = reference
        self._serial = serial
        self._counter = counter
        self._price = price
        self._ref_toner = ref_toner
        self._stock = stock
        self._id_category = id_category
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

    ## _stock
    @property
    def stock(self):
        return self.stock

    @stock.setter
    def stock(self, stock):
        self.stock = stock

    ## _place_storage
    @property
    def id_category(self):
        return self._id_category

    @id_category.setter
    def id_category(self, id_category):
        self._id_category = id_category

    ## _status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
