import pymongo

data = [{
    "pens": {
        "sketchpen" : {
            "thick_nib": {
                "whiteboard_marker": {"black": "50 Rs", "blue": "50 Rs", "Red": "50 Rs"},
                "permenant_marker": {"black": "40 Rs", "blue": "40 Rs", "Red": "40 Rs"}
        },
            "thin_nib": {
                "small": {"set_of_12" : "70 Rs","set of 24" : "120 Rs"},
                "big": {"set_of_12" : "90 Rs","set of 24" : "140 Rs"
                }
        }
        },
        "gelpen" : {
            "company" : {
                "renolds": {"black": "10 Rs", "blue": "10 Rs", "Red": "10 Rs"},
                "pilot": {"black": "15 Rs", "blue": "15 Rs", "Red": "15 Rs"}
            }
        },
        "ballpen": {
            "disposable": {
                "lizz": {"black": "3 Rs", "blue": "3 Rs", "Red": "3 Rs"},
                "chi": {"black": "5 Rs", "blue": "5 Rs", "Red": "5 Rs"}
            },
            "non-disposable" : {
                "lexy": {"black": "3 Rs", "blue": "3 Rs", "Red": "3 Rs"},
                "fasttip": {"black": "5 Rs", "blue": "5 Rs", "Red": "5 Rs"}
            }
        }
    }},
    {"books": {
        "textbooks": {
            "grade-1": "250 Rs", "grade-2":"300 Rs", "grade-3":"350 Rs", "grade-4":"400 Rs", "grade-5":"500 Rs"
        },
        "diaries": {
            "travel_diary": {
                "standard": {"small": "200 Rs", "medium": "350 Rs", "large": "500 Rs"},
                "funky": {"small": "300 Rs", "medium": "450 Rs", "large": "600 Rs"}
        },
            "calender_diary": {"small":"120 Rs","big":"240 Rs"}
        },
        "notebooks" : {
            "ruled" : {
                "A3" : {"standard": "60 Rs" , "spiral_binded" : "70 Rs"},
                "A4" : {"standard": "50 Rs" , "spiral_binded" : "60 Rs"},
                "A5" : {"standard": "40 Rs" , "spiral_binded" : "50 Rs"}
        },
            "blank" : {
                "A3" : {"standard": "60 Rs" , "spiral_binded" : "70 Rs"},
                "A4" : {"standard": "50 Rs" , "spiral_binded" : "60 Rs"},
                "A5" : {"standard": "40 Rs" , "spiral_binded" : "50 Rs"}
        }
    }
    }
}]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#use database named "organisation"
mydb = myclient["products"]

#use collection named "developers"
mycol = mydb["stationery"]

#insert multiple documents
mycol.insert_many(data)

print('------Query to find All documents with category and Item in MongoDB----')
for ech_object in mycol.find():
	print(ech_object)

print('\n\n------Query to first Level documents with category and Items in MongoDB----')
for ech_obj in mycol.find({},{"_id":0}):
    print(ech_obj.values())

# Works
	
