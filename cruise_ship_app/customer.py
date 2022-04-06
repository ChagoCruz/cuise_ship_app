class Customer:
    def __init__(self, name):
        self.__name = name
        self.__tickets = []
        #self.__total_cost = 0

    def get_name(self):
        return self.__name

    def get_tickets(self):
        return self.__tickets

    def add_ticket(self, name):
        self.__tickets.append(name)

    def get_total_cost_of_tickets(self):
        cost = 0
        for i in self.__tickets:
            cost += i.get_cost_of_ticket()
        return cost
