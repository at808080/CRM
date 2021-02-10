import pymongo
import mongoengine
from datetime import date
import datetime
#login = ZeroAlpha, levilevi


print("attempting to connect")
cluster = pymongo.MongoClient("mongodb+srv://ZeroAlpha:levi@cluster0.pn90l.mongodb.net/Jobs?retryWrites=true&w=majority")
print("connected")
db = cluster["Jobs"]
jobCollection = db["Jobs"]
contactCollection = db["Contacts"]
deviceCollection = db["Devices"]


class CustomerDoc(mongoengine.Document):
    name = mongoengine.StringField()
    company = mongoengine.StringField()
    phone = mongoengine.IntField()
    address = mongoengine.StringField()
    email = mongoengine.EmailField()
    partner = mongoengine.BooleanField()

    def json(self):
        customer_doc_dict = {
            "name": self.name,
            "company": self.company,
            "phone": self.phone,
            "address": self.address,
            "email": self.email,
            "partner": self.partner
        }
        return customer_doc_dict

    meta = {
        "indexes": ["name", "email"],
        "ordering": ["name"]
    }

    def addToMongo(self):
        contactCollection.insert_one(self.json())

class DeviceDoc(mongoengine.Document):
    type = mongoengine.StringField()
    media = mongoengine.StringField()
    serial = mongoengine.StringField()
    extras = mongoengine.StringField()
    recdate = mongoengine.DateField()
    patient = mongoengine.BooleanField()


    def json(self):
        device_doc_dict = {
            "type": self.type,
            "media": self.media,
            "serial": self.serial,
            "extras": self.extras,
            "recdate": self.recdate
        }
        return device_doc_dict

    meta = {
        "indexes": ["media", "serial"],
        "ordering": ["media"]
    }

    def addToMongo(self):
        deviceCollection.insert_one(self.json())

class JobDoc(mongoengine.Document):
    customername = mongoengine.StringField()
    devicemedia = mongoengine.StringField()
    deviceserial = mongoengine.StringField()
    quote = mongoengine.StringField()
    priority = mongoengine.StringField()
    recdate = mongoengine.DateField()
    startdate = mongoengine.DateField()
    enddate = mongoengine.DateField()
    location = mongoengine.StringField()
    notes = mongoengine.StringField()
    success = mongoengine.StringField()

    def json(self):
        job_doc_dict = {
            "customername": self.customername,
            "devicemedia": self.devicemedia,
            "deviceserial": self.deviceserial,
            "quote": self.quote,
            "priority": self.priority,
            "recdate": self.recdate,
            "startdate": self.startdate,
            "enddate": self.enddate,
            "location": self.location,
            "notes": self.notes,
            "success": self.success
        }
        return job_doc_dict
    meta = {
        "indexes": ["startdate", "priority"],
        "ordering": ["startdate"]
    }

    def addToMongo(self):
        jobCollection.insert_one(self.json())


def addNewDocument(c1, c2, c3, c4, c5, c6, d1, d2, d3, d4, d5, d6, j1, j2, j3, j4, j5, j6, j7, j8):
    c = CustomerDoc(name=c1, company=c2, phone=c3, email=c4, address=c5, partner=c6)
    d = DeviceDoc(type=d1, media=d2, serial=d3, recdate=d4, patient=d5, extras=d6)
    j = JobDoc(customername=c.name, devicemedia=d.media, deviceserial=d.serial, priority=j4, recdate=d.recdate, startdate=j5, enddate=j6, location=j7, success=j8)
    contactCollection.insert_one(c.json())
    deviceCollection.insert_one(d.json())
    jobCollection.insert_one(j.json())
    print("************\n Added to Mongo \n************")


