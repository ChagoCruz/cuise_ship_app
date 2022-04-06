class Ticket:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_cost_of_ticket(self):
        return 0

class Exclusive(Ticket):
    def __init__(self, name, grade):
        self.__name = name       
        self.__grade = grade

    def set_name(self, name):
        self.__name = name  

    def set_grade(self, grade):
        self.__grade = grade     
            
    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_cost_of_ticket(self):
        if self.__grade == 's':
            return 10000
        elif self.__grade == 'c':
            return 12000
        elif self.__grade == 'f':
            return 13000

class PremiumPlus(Ticket):
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_cost_of_ticket(self):
        if self.__grade == 's':
            return 6000
        elif self.__grade == 'c':
            return 8500 
        elif self.__grade == 'f':
            return 9500


class EconomyComfort(Ticket):
    def __init__(self, name, grade, tix_num):
        self.__name = name
        self.__grade = grade
        self.__tix_num = tix_num

    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_cost_of_ticket(self):
        return (int(self.__tix_num)*1200)
