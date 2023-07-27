from config import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

Base = declarative_base()


class LC_BasicProfile(db.Model):
    __tablename__ = 'lc_basic_profile'

    activity_eff_date = db.Column(db.Date)
    entity_code = db.Column(db.String(4))
    entity_desc = db.Column(db.String(20))
    pri_activity_code = db.Column(db.Integer)
    pri_activity_desc = db.Column(db.String(255))
    registration_date = db.Column(db.Date)
    country_of_incorporation_code = db.Column(db.String(4))
    country_of_incorporation_desc = db.Column(db.String(255))
    source = db.Column(db.Integer)
    sec_activity_code = db.Column(db.Integer)
    sec_activity_desc = db.Column(db.String(255))
    company_allottee_indicator = db.Column(db.String(1))
    company_conversation_indicator = db.Column(db.String(1))
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
    fa_id_number = db.Column(db.String(40))
    fa_deregistration_date = db.Column(db.Date)
    fa_status_effective_date = db.Column(db.Date)
    fa_registration_date = db.Column(db.Date)
    fa_expiry_date = db.Column(db.Date)
    fa_status_code = db.Column(db.Integer)
    fa_status_desc = db.Column(db.String(40))
    company_authorized_capital_number = db.Column(db.Float)
    company_number_of_members = db.Column(db.Integer)
    company_type_code = db.Column(db.String(20))
    company_type_desc = db.Column(db.String(255))
    allp_indicator = db.Column(db.String(1))
    ca_amalgamation_date = db.Column(db.Date)
    ca_transaction_number = db.Column(db.String(40))
    ca_company_uen = db.Column(db.String(20))
    ca_company_name = db.Column(db.String(40))
    issuance_agency_code = db.Column(db.String(10))
    issuance_agency_desc = db.Column(db.String(255))
    secondary_activity_add_desc = db.Column(db.String(255))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class LC_CompanyAddress(db.Model):
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
    lc_basic_profile_uen = db.Column(db.String(20), db.ForeignKey('lc_basic_profile.uen', name='lc_basic_profile_uen'))
    lc_basic_profile = db.relationship('LC_BasicProfile', backref=backref('lc_company_address'), uselist=False, lazy=True)
