from models import Client

clients = Client()

for record in clients.read_all():
    print(record)

# clients.insert(("Trajus","Two servers in use"))
clients.delete("Trajus")

for record in clients.read_all():
    print(record)

print ("DONE")


