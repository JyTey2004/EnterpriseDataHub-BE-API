from config import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

# from sqlalchemy import Column, Integer, String, Date, ForeignKey
# from sqlalchemy.orm import relationship

Base = declarative_base()


class BN_BasicProfile(db.Model):
    __tablename__ = 'bn_basic_profile'

    activity_eff_date = db.Column(db.Date)
    entity_code = db.Column(db.String(4))
    entity_desc = db.Column(db.String(20))
    constitution_value = db.Column(db.String(30))
    constitution_code = db.Column(db.String(3))
    pri_activity_code = db.Column(db.Integer)
    pri_activity_desc = db.Column(db.String(255))
    registration_date = db.Column(db.Date)
    source = db.Column(db.Integer)
    sec_activity_code = db.Column(db.Integer)
    sec_activity_desc = db.Column(db.String(255))
    entity_name = db.Column(db.String(30))
    expiry_date = db.Column(db.Date)
    constitution_date = db.Column(db.Date)
    person_particulars_change_date = db.Column(db.Date)
    pri_activity_add_desc = db.Column(db.String(255))
    uen_status = db.Column(db.String(3))
    uen_status_desc = db.Column(db.String(20), nullable=True)
    uen = db.Column(db.String(20), primary_key=True)
    name_eff_date = db.Column(db.Date)
    entity_status_value = db.Column(db.String(10))
    entity_status_code = db.Column(db.String(10))
    entity_status_desc = db.Column(db.String(30))
    entity_long_name = db.Column(db.String(40))
    entity_status_eff_date = db.Column(db.Date)
    renewal_years = db.Column(db.Integer)
    renewal_date = db.Column(db.Date)
    renewal_mode_code = db.Column(db.Integer)
    renewal_mode_desc = db.Column(db.String(40))
    transaction_number = db.Column(db.String(40))
    fa_id_number = db.Column(db.String(40))
    fa_deregistration_date = db.Column(db.Date)
    fa_status_effective_date = db.Column(db.Date)
    fa_registration_date = db.Column(db.Date)
    fa_expiry_date = db.Column(db.Date)
    fa_status_code = db.Column(db.Integer)
    fa_status_desc = db.Column(db.String(40))
    created_date = db.Column(db.Date)
    commencement_date = db.Column(db.Date)
    issuance_agency_code = db.Column(db.String(10))
    issuance_agency_desc = db.Column(db.String(255))
    secondary_activity_add_desc = db.Column(db.String(255))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class BN_CompanyAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(10))
    country_desc = db.Column(db.String(255))
    unit_value = db.Column(db.String(255))
    purpose_value = db.Column(db.String(255))
    street_value = db.Column(db.String(255))
    addresstype = db.Column(db.String(2))
    block_value = db.Column(db.String(255))
    postal_value = db.Column(db.String(255))
    source = db.Column(db.Integer)
    address_change_date_value = db.Column(db.String(255))
    floor_value = db.Column(db.String(255))
    building_value = db.Column(db.String(255))

    # Define the one-to-one relationship with Company
    bn_basic_profile_uen = db.Column(db.String(20), db.ForeignKey('bn_basic_profile.uen', name='bn_basic_profile_uen'))
    bn_basic_profile = db.relationship('BN_BasicProfile', backref=backref('bn_company_address'), uselist=False, lazy=True)
