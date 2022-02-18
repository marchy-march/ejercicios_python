class Car:
    _make = None 
    _model = None
    _color = None 
    _year = None
    _reg_plate= None
    def __init__(self,make_2,model_2,color_2, year_2, reg_plate_2):
        self._make = make_2
        self._model = model_2
        self._color = color_2
        self._year = year_2
        self._reg_plate = reg_plate_2
    def pay_fee(self):
        if (self._year < 2005):
            return("Models older than 2005 must pay the Yearly Registration Fee. \nYour payment is pending. \nLate fees apply.")
        else:
            return("Models older than 2005 must pay the Yearly Registration Fee. \nYour Registration Fee is up to date.")
    def set_reg_plate(self, new_plate):
        self._reg_plate = new_plate
        
    def get_salary(self):
        return(self._make)
    def get_model(self):
        return(self._model)
    def get_color(self):
        return(self._color)
    def get_year(self):
        return(self._year)
    def get_reg_plate(self):
        return(self._reg_plate)