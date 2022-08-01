from flask import make_response, request
import json

def index():
    
    json_file_path = "fakedatabase.json"

    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
    print(contents)
    return make_response({"message": "Api-books"},200)

def allContacts():

    def sortAlphabetic(contact):
        if phrase.lower() in contact['name'].lower():
            return True
        else:
            return False

    file = open("fakedatabase.json")
    data = json.load(file)
    file.close()
    phrase = request.args.get('phrase')
    data_sorted = sorted(data, key=lambda k: k['name'])
    phrase = request.args.get('phrase')
    if phrase == "":
        return make_response({"message": "Please, put a phrase to search"},400)
    if phrase:
        data_sorted = filter(sortAlphabetic,data_sorted)
    return make_response({"data": list(data_sorted)},200)

def getContact(contact_id):
    file = open("fakedatabase.json")
    data = json.load(file)
    file.close()
    dataContact = {}
    for contact in data:
        if contact_id == contact['id']:
            dataContact = contact
            break;
    else:
        return make_response({"message" :"The contact doesn't exist" },404)
    return make_response({"data": dataContact},200)

def deleteContact(contact_id):
    file = open("fakedatabase.json")
    data = json.load(file)
    file.close()
    count = 0
    for item in data:
        if item['id'] == contact_id:
            print("Eliminar ",item)
            data.pop(count)
        count += 1
    else:
        return make_response({"message" :"The contact doesn't exist" },404)
    json_string = json.dumps(data)
    with open("fakedatabase.json","w") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    return make_response({"data": "Delete contact"},204)
    

