from config import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

Base = declarative_base()


class AppointedEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type_code = db.Column(db.String(10))
    type_desc = db.Column(db.String(255))
    uen_value = db.Column(db.String(20))


class AppointedPerson(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(255))
    nationality_code = db.Column(db.String(10))
    nationality_desc = db.Column(db.String(255))
    id_type_code = db.Column(db.String(10))
    id_type_desc = db.Column(db.String(255))

    # appointed_person_entity_id = db.Column(db.Integer, db.ForeignKey('appointed_entity.id', name='appointed_person_entity_id'))
    # appointed_entity = db.relationship('AppointedEntity', backref=backref('appointed_person'), uselist=False, lazy=True)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uen_value = db.Column(db.String(20))
    withdrawal_date = db.Column(db.Date)
    reinstate_indicator = db.Column(db.String(1))
    estate_indicator = db.Column(db.String(1))
    appointed_date = db.Column(db.Date)
    position_code = db.Column(db.String(10))
    position_desc = db.Column(db.String(255))
    source = db.Column(db.Integer)
    category_code = db.Column(db.String(10))
    category_desc = db.Column(db.String(255))
    disqualification_reason_subsection_code = db.Column(db.String(10))
    disqualification_reason_subsection_desc = db.Column(db.String(255))
    withdrawal_reason_code = db.Column(db.String(10))
    withdrawal_reason_desc = db.Column(db.String(255))
    death_indicator_value = db.Column(db.String(1))
    disqualification_reason_code = db.Column(db.String(50))
    disqualification_reason_desc = db.Column(db.String(255))

    # Define the one-to-one relationship with AppointedEntity
    appointed_appointment_entity_id = db.Column(db.Integer, db.ForeignKey('appointed_entity.id', name='appointed_appointment_entity_id'))
    appointed_entity = db.relationship('AppointedEntity', backref=backref('appointment'), uselist=False, lazy=True)

    # Define the one-to-one relationship with AppointedPerson
    appointed_person_id = db.Column(db.String(20), db.ForeignKey('appointed_person.id'), name='appointed_person_id')
    appointed_person = db.relationship('AppointedPerson', backref=backref('appointment'), uselist=False, lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(10))
    country_desc = db.Column(db.String(255))
    unit_value = db.Column(db.String(20))
    purpose_value = db.Column(db.String(20))
    street_value = db.Column(db.String(255))
    addresstype = db.Column(db.String(10))
    block_value = db.Column(db.String(20))
    postal_value = db.Column(db.String(20))
    source = db.Column(db.Integer)
    address_change_date_value = db.Column(db.Date)
    floor_value = db.Column(db.String(20))
    building_value = db.Column(db.String(255))

    # Define the many-to-one relationship with AppointedPerson
    appointed_person_id = db.Column(db.String(20), db.ForeignKey('appointed_person.id', name='appointed_person_id'))
    appointed_person = db.relationship('AppointedPerson', backref='addresses', uselist=False, lazy=True)
