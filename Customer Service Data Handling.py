# 2. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:
    

def new_service_ticket(tix,ticket_num,customer,issue,status):
    if ticket_num not in tix:
        tix[ticket_num] = {"Customer": customer, "Issue": issue, "Status": status}
        print (f"Customer '{customer}' has been added with ticket number: {ticket_num}." )
    else:
        print (f"Customer '{customer}' is already in the system with ticket number '{ticket_num}. ")
    
def update_status(tix,ticket_num,status):
    if ticket_num in tix:
        tix[ticket_num]["Status"] = status
        print(f"{ticket_num} updated to {status}")
    else:
        print(f"{ticket_num} was not found")

def display_ticket(tix, ticket_number):
    if ticket_number in tix:
        ticket = tix[ticket_number]
        print(f"{ticket_number} \nCustomer: {ticket['Customer']}\nIssue: {ticket["Issue"]}\nStatus: {ticket['Status']}")
    else:
        print(f"{ticket_number} not found")

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

new_service_ticket(service_tickets, "Ticket003", "Kyle", "No audio", "open")
update_status(service_tickets,"Ticket003","closed")
display_ticket(service_tickets, "Ticket003")