from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app)

buildings = { [
{
  "id":1,
  "name":"Mardi Gras",
  "address":"720 W 27th Street",
  "city":"Los Angeles",
  "state":"CA",
  "zip":"90007",
  "desc": "Situated on the out-skirts, provides a perfect mix of natural living.",
  "img":"http://g.mnp0.com/gimg/34.028389/-118.27"
},

{
  "id":2,
  "name":"Nupac Apartments",
  "address":"450 W 28th Street",
  "city":"San Diego",
  "state":"CA",
  "zip":"90090",
  "desc": "Affordable Student housing within walking distance to University of Southern California",
  "img":"https://www.nupac.com/img/large-640-400/"

},

{
  "id":3,
  "name":"First Choice Hosuing",
  "address":"908 W Adams Blvd",
  "city":"Los Angeles",
  "state":"CA",
  "zip":"90247",
  "desc": "First Choice Housing Association provides quality accommodation solutions for students",
  "img":"http://stuho.com/Pictures/large/Bcode/1-"

},

{
  "id":4,
  "name":"Stuho",
  "address":"2650 Orhchard Avenue",
  "city":"Pasadena",
  "state":"CA",
  "zip":"90089",
  "desc": "We offer all types of USC Student Housing: Apartments, Houses, Rooms at affordable rates",
  "img":"http://stuho.com/Pictures/large/Bcode/1-"

},

{
  "id":5,
  "name":"Nupac Apartments",
  "address":"2656 Ellendale",
  "city":"Sacramento",
  "state":"CA",
  "zip":"90124",
  "desc": "Affordable Student housing within walking distance to University of Southern California",
  "img":"http://stuho.com/Pictures/large/Bcode/1-"

}


]
}

def abort_if_apartment_doesnt_exist(apt_id):
    if apt_id not in buildings:
        abort(404, message="Apartment {} doesn't exist".format(apt_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# shows a single todo item and lets you delete a todo item
class Apt(Resource):
    def get(self, apt_id):
        abort_if_apartment_doesnt_exist(apt_id)
        return buildings[apt_id]

# shows a list of all todos, and lets you POST to add new tasks
class AptList(Resource):
    def get(self):
        return buildings

class BuildingSearch(Resource):
    def get(self,name):
        search_results = {'status':'failure','results':[]}
        flag = 0
        for value in buildings:
            flag=1
            if name in value['id'] or name in value['title'] or name in value['desc']:
                search_results["results"].append(value)
        if flag == 1:
            search_results['status'] ='success'
        return search_results


##
api.add_resource(AptList, '/apt')
api.add_resource(Apt, '/apt/<apt_id>')
api.add_resource(BuildingSearch, '/apt/search/<name>')


if __name__ == '__main__':
    app.run(debug=True)
