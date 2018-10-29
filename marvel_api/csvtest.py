from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

database = "marvel_restapi"
collection = "marvel_heroes"
db = client[database]

print(db.list_collection_names())

posts = db[collection]
# post_data = {
#     'id': '1678',
#     'name': 'Spider-Man (Peter Parker)',
#     'IDENTITY': 'Secret Identity',
#     'ALIGN': 'Good Characters',
#     'EYE': 'Hazel Eyes',
#     'HAIR': 'Brown Hair',
#     'SEX': 'Male Characters',
#     'ALIVE': 'Living Characters',
#     'FIRST APPEARANCE': 'Aug-62',
#     'Year': '1962'
# }

# result = posts.insert_one(post_data)
# print('One post: {0}'.format(result.inserted_id))

# bills_post = posts.find({'ALIVE': 'Living Characters'})
# print(bills_post)

# for items in bills_post:
#     print(items)


