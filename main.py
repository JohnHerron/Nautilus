from models import Client

clients = Client()
clients.insert(("Trajus","Two servers in use"))

for record in clients.read_all():
    print(record)

clients.update("Trajus", "UPDATED TEXT")
# clients.delete("Trajus")
# read_data = clients.read("Trajus")
#print(read_data)
for record in clients.read_all():
    print(record)

print ("DONE")


