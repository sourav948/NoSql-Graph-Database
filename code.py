from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase("http://localhost:7474", username='neo4j', password='123456')
 

user = db.labels.create("User")
u1 = db.nodes.create(name="Sourav")
u2 = db.nodes.create(name="Taranjit")
user.add(u1,u2)
 
movie = db.labels.create("Movies")
b1 = db.nodes.create(name="Batman")
b2 = db.nodes.create(name="Spiderman")

movie.add(b1, b2)

u1.relationships.create("likes", b1)
u1.relationships.create("likes", b2)
u2.relationships.create("likes", b1)

u1.relationships.create("friends", u2)