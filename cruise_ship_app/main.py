from ticket import *
from customer import Customer

def main():
    jeweler = Customer('Maggie May')
    cust1 = Exclusive('John Smoth', 'f')
    cust2 = PremiumPlus('Jane Jones', 's')
    cust3 = EconomyComfort('Ruth Sharp', 'c', 2)

    jeweler.add_ticket(cust1)
    jeweler.add_ticket(cust2)
    jeweler.add_ticket(cust3)

    print("Maggie's Jewelers List of Passangers")
    print('====================================\n')
    print("NOTE:  'c' -> couple; 'f' -> family; 's' -> single\n")

    tickets = jeweler.get_tickets()
    for ticket in tickets:
        print(f'{ticket.get_name():<17}{"("}{str(ticket.get_grade())}{")"}'
              f'{"    $"}{ticket.get_cost_of_ticket():>10,.2f}')

    print()
    print(f'{"Total cost of tickets: $"}{jeweler.get_total_cost_of_tickets():>10,.2f}')

    cust4 = Exclusive('Dempsey Dean', 'c')
    cust5 = EconomyComfort('Sophia Weather', 'f', 5)

    jeweler.add_ticket(cust4)
    jeweler.add_ticket(cust5)

    print()
    for ticket in tickets:
        print(f'{ticket.get_name():<17}{"("}{str(ticket.get_grade())}{")"}'
              f'{"    $"}{ticket.get_cost_of_ticket():>10,.2f}')

    print()
    print(f'{"Total cost of tickets: $"}{jeweler.get_total_cost_of_tickets():>10,.2f}')
    
main()
