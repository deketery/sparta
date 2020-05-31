#몽고를 키기위해선 cmd에서 mongod 를 해놔야함

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title':"매트릭스"})
matrix_star = target_movie["star"]  #매트릭스의 평점

db.movies.update_many({"star":matrix_star},{'$set':{'star':0}})
