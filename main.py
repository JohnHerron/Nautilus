from models import Client, Connection

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

connections = Connection()
connections.insert(("RDP","Trajus","TRAJUS TEST CONNECTION"))

for record in connections.read_all():
    print(record)

connections.update(1,("TEAMVIEWER","UPDATED TEST CONNECTION"))

for record in connections.read_all():
    print(record)

connections.delete(1)

print ("DONE")


