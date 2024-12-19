from models import Client, Connection


clients = Client()
connections = Connection()
clients.insert(("Trajus","Two servers in use"))


for record in clients.read_all():
    print(record)


clients.update("Trajus", "UPDATED TEXT")


for record in clients.read_all():
    print(record)


connections.insert(("RDP","Trajus","TRAJUS TEST CONNECTION"))


for record in connections.read_all():
    print(record)


connections.update(1,("TEAMVIEWER","UPDATED TEST CONNECTION"))


for record in connections.read_all():
    print(record)


clients.delete("Trajus")

print("PRINTING CLIENTS:")
for record in clients.read_all():
    print(record)
print("PRINTING CONNECTIONS")
for record in connections.read_all():
    print(record)

print ("DONE")


