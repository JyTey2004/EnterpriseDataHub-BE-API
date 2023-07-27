# app/controllers.py
from app.modals.BN_Modal import BN_BasicProfile, BN_CompanyAddress
from app.modals.LC_Modal import LC_BasicProfile, LC_CompanyAddress
from app.modals.Generic_Modals import Address, AppointedPerson, AppointedEntity, Appointment
from config import db
from datetime import datetime, date
from flask import jsonify

function_map = {
    'BN': BN_BasicProfile,
    'LC': LC_BasicProfile,
}

address_function_map = {
    'BN': BN_CompanyAddress,
    'LC': LC_CompanyAddress,
}


def insert_data_into_db(data, uen):
    try:
        basic_profile_data = data.get('basic-profile')
        if basic_profile_data:
            entity_type = basic_profile_data['entity-type']['code']
            basic_profile = function_map[entity_type](
                activity_eff_date=datetime.strptime(basic_profile_data['activity-eff-date']['value'],
                                                    '%Y-%m-%d').date(),
                entity_code=basic_profile_data['entity-type']['code'],
                entity_desc=basic_profile_data['entity-type']['desc'],
                **{'constitution_value': basic_profile_data['constitution']['value']} if entity_type == 'BN' else {},
                **{'constitution_code': basic_profile_data['constitution']['code']} if entity_type == 'BN' else {},
                pri_activity_code=int(basic_profile_data['primary-activity']['code']),
                pri_activity_desc=basic_profile_data['primary-activity']['desc'],
                registration_date=datetime.strptime(basic_profile_data['registration-date']['value'],
                                                    '%Y-%m-%d').date(),
                **{'country_of_incorporation_code': basic_profile_data['country-of-incorporation'][
                    'code']} if entity_type == 'LC' else {},
                **{'country_of_incorporation_desc': basic_profile_data['country-of-incorporation'][
                    'desc']} if entity_type == 'LC' else {},
                source=int(basic_profile_data['source']),
                sec_activity_code=int(basic_profile_data['secondary-activity']['code']),
                sec_activity_desc=basic_profile_data['secondary-activity']['desc'],
                **{'company_allottee_indicator': basic_profile_data['company-allottee-indicator'][
                    'value']} if entity_type == 'LC' else {},
                **{'company_conversation_indicator': basic_profile_data['company-conversion-indicator'][
                    'value']} if entity_type == 'LC' else {},
                entity_name=basic_profile_data['entity-name']['value'],
                **{'expiry_date': datetime.strptime(basic_profile_data['expiry-date']['value'],
                                                    '%Y-%m-%d').date()} if entity_type == 'BN' else {},
                **{'constitution_date': datetime.strptime(basic_profile_data['constitution-date']['value'],
                                                          '%Y-%m-%d').date()} if entity_type == 'BN' else {},
                **{'person_particulars_change_date': datetime.strptime(
                    basic_profile_data['person-particulars-change-date']['value'],
                    '%Y-%m-%d').date()} if entity_type == 'BN' else {},
                pri_activity_add_desc=basic_profile_data['primary-activity-add-desc']['value'],
                uen_status=basic_profile_data['uen-status']['code'],
                uen_status_desc=basic_profile_data['uen-status']['desc'],
                uen=basic_profile_data['uen']['value'],
                name_eff_date=datetime.strptime(basic_profile_data['name-eff-date']['value'], '%Y-%m-%d').date(),
                entity_status_value=basic_profile_data['entity-status']['value'],
                entity_status_code=basic_profile_data['entity-status']['code'],
                entity_status_desc=basic_profile_data['entity-status']['desc'],
                entity_long_name=basic_profile_data['entity-long-name']['value'],
                entity_status_eff_date=datetime.strptime(basic_profile_data['entity-status-eff-date']['value'],
                                                         '%Y-%m-%d').date(),
                **{'renewal_years': int(
                    basic_profile_data['renewal']['number-of-years']['value'])} if entity_type == 'BN' else {},
                **{'renewal_date': datetime.strptime(basic_profile_data['renewal']['renewal-date']['value'],
                                                     '%Y-%m-%d').date()} if entity_type == 'BN' else {},
                **{'renewal_mode_code': int(
                    basic_profile_data['renewal']['renewal-mode']['code'])} if entity_type == 'BN' else {},
                **{'renewal_mode_desc': basic_profile_data['renewal']['renewal-mode'][
                    'desc']} if entity_type == 'BN' else {},
                **{'transaction_number': basic_profile_data['renewal']['transaction-number'][
                    'value']} if entity_type == 'BN' else {},
                fa_id_number=basic_profile_data['filing-agent']['fa-id-number']['value'],
                fa_deregistration_date=datetime.strptime(
                    basic_profile_data['filing-agent']['deregistration-date']['value'], '%Y-%m-%d').date(),
                fa_status_effective_date=datetime.strptime(
                    basic_profile_data['filing-agent']['status-effective-date']['value'], '%Y-%m-%d').date(),
                fa_registration_date=datetime.strptime(basic_profile_data['filing-agent']['registration-date']['value'],
                                                       '%Y-%m-%d').date(),
                fa_expiry_date=datetime.strptime(basic_profile_data['filing-agent']['expiry-date']['value'],
                                                 '%Y-%m-%d').date(),
                fa_status_code=int(basic_profile_data['filing-agent']['status']['code']),
                fa_status_desc=basic_profile_data['filing-agent']['status']['desc'],
                **{'created_date': datetime.strptime(basic_profile_data['created-date']['value'],
                                                     '%Y-%m-%d').date()} if entity_type == 'BN' else {},
                **{'commencement_date': datetime.strptime(basic_profile_data['commencement-date']['value'],
                                                          '%Y-%m-%d').date()} if entity_type == 'BN' else {},
                **{'company_authorized_capital_number': basic_profile_data['company-authorized-capital-number'][
                    'value']} if entity_type == 'LC' else {},
                **{'company_number_of_members': basic_profile_data['company-number-of-members'][
                    'value']} if entity_type == 'LC' else {},
                **{'company_type_code': basic_profile_data['company-type']['code']} if entity_type == 'LC' else {},
                **{'company_type_desc': basic_profile_data['company-type']['desc']} if entity_type == 'LC' else {},
                **{'allp_indicator': basic_profile_data['allp-indicator']['value']} if entity_type == 'LC' else {},
                **{'ca_amalgamation_date': datetime.strptime(
                    basic_profile_data['company-amalgamation']['amalgamation-date']['value'],
                    '%Y-%m-%d').date()} if entity_type == 'LC' else {},
                **{'ca_transaction_number': basic_profile_data['company-amalgamation']['transaction-number'][
                    'value']} if entity_type == 'LC' else {},
                **{'ca_company_uen': basic_profile_data['company-amalgamation']['amalgamated-company-uen'][
                    'value']} if entity_type == 'LC' else {},
                **{'ca_company_name': basic_profile_data['company-amalgamation']['amalgamated-company-name'][
                    'value']} if entity_type == 'LC' else {},
                issuance_agency_code=basic_profile_data['issuance-agency']['code'],
                issuance_agency_desc=basic_profile_data['issuance-agency']['desc'],
                secondary_activity_add_desc=basic_profile_data['secondary-activity-add-desc']['value'],
            )

            db.session.add(basic_profile)

        for appointment_data in data.get('appointments', []):
            # Insert AppointedEntity data
            appointed_entity_data = appointment_data.get('appointed-entity', [])
            appointed_person_data = appointment_data.get('appointed-person', [])
            # print("appointed_entity_data:", appointed_entity_data)  # Debug print
            # print("appointed_person_data:", appointed_person_data)  # Debug print
            if appointed_entity_data is not None and len(appointed_entity_data) > 0:
                appointed_entity = AppointedEntity(
                    name=appointed_entity_data['name']['value'],
                    type_code=appointed_entity_data['type']['code'],
                    type_desc=appointed_entity_data['type']['desc'],
                    uen_value=appointed_entity_data['uen']['value']
                )
                db.session.add(appointed_entity)

            # Insert AppointedPerson data
            if appointed_person_data is not None and len(appointed_person_data) > 0:
                # entity_id = AppointedEntity.query.filter_by(uen_value=uen).first().id
                if appointed_person_data:
                    appointed_person = AppointedPerson(
                        id=appointed_person_data['id-no']['value'],
                        name=appointed_person_data['name']['value'],
                        nationality_code=appointed_person_data['nationality']['code'],
                        nationality_desc=appointed_person_data['nationality']['desc'],
                        id_type_code=appointed_person_data['id-type']['code'],
                        id_type_desc=appointed_person_data['id-type']['desc'],
                        # appointed_person_entity_id=entity_id
                    )
                    db.session.add(appointed_person)

                    # Insert Address data for AppointedPerson
                    for address_data in appointed_person_data.get('addresses', []):
                        address = Address(
                            country_code=address_data['country']['code'],
                            country_desc=address_data['country']['desc'],
                            unit_value=address_data['unit']['value'],
                            purpose_value=address_data['purpose']['value'],
                            street_value=address_data['street']['value'],
                            addresstype=address_data['addresstype'],
                            block_value=address_data['block']['value'],
                            postal_value=address_data['postal']['value'],
                            source=address_data['source'],
                            address_change_date_value=datetime.strptime(address_data['address-change-date']['value'], '%Y-%m-%d').date(),
                            floor_value=address_data['floor']['value'],
                            building_value=address_data['building']['value']
                        )
                        appointed_person.addresses.append(address)

                    db.session.add(appointed_person)

            # Insert Appointment data
            appointment = Appointment(
                uen_value=uen,
                withdrawal_date=datetime.strptime(appointment_data['withdrawal-date']['value'], '%Y-%m-%d').date(),
                reinstate_indicator=appointment_data['reinstate-indicator']['value'],
                estate_indicator=appointment_data['estate-indicator']['value'],
                appointed_date=datetime.strptime(appointment_data['appointed-date']['value'], '%Y-%m-%d').date(),
                position_code=appointment_data['position']['code'],
                position_desc=appointment_data['position']['desc'],
                source=appointment_data['source'],
                category_code=appointment_data['category']['code'],
                category_desc=appointment_data['category']['desc'],
                disqualification_reason_subsection_code=appointment_data['disqualification-reason-subsection']['code'],
                disqualification_reason_subsection_desc=appointment_data['disqualification-reason-subsection']['desc'],
                withdrawal_reason_code=appointment_data['withdrawal-reason']['code'],
                withdrawal_reason_desc=appointment_data['withdrawal-reason']['desc'],
                death_indicator_value=appointment_data['death-indicator']['value'],
                disqualification_reason_code=appointment_data['disqualification-reason']['code'],
                disqualification_reason_desc=appointment_data['disqualification-reason']['desc'],
                appointed_appointment_entity_id=AppointedEntity.query.filter_by(
                    uen_value=appointed_entity_data['uen']['value']).first().id if len(
                    appointed_entity_data) > 0 else None,
                appointed_person_id=appointed_person_data['id-no']['value'] if len(appointed_person_data) > 0 else None
            )
            db.session.add(appointment)

        # Insert Address data for BasicProfile
        for address_data in data.get('addresses', []):
            address = address_function_map[basic_profile_data['entity-type']['code']](
                country_code=address_data['country']['code'],
                country_desc=address_data['country']['desc'],
                unit_value=address_data['unit']['value'],
                purpose_value=address_data['purpose']['value'],
                street_value=address_data['street']['value'],
                addresstype=address_data['addresstype'],
                block_value=address_data['block']['value'],
                postal_value=address_data['postal']['value'],
                source=address_data['source'],
                address_change_date_value=datetime.strptime(address_data['address-change-date']['value'], '%Y-%m-%d').date(),
                floor_value=address_data['floor']['value'],
                building_value=address_data['building']['value'],
                **{f"{basic_profile_data['entity-type']['code'].lower()}_basic_profile_uen": uen}
            )
            db.session.add(address)

        db.session.commit()
        print("basic_profile data inserted successfully!")
        return True

    except Exception as e:
        db.session.rollback()
        print("Error while inserting data:", str(e))
        return False


def format_date(date_obj):
    if isinstance(date_obj, date):
        return date_obj.strftime("%Y-%m-%d")
    return None


def get_data_from_database(uen, data):
    try:
        basic_info_data = function_map[data.get('basic-profile')['entity-type']['code']].query.filter_by(
            uen=uen).first()

        if basic_info_data:
            data = {'basic-profile': {
                'source': basic_info_data.source,
                'uen': {'value': basic_info_data.uen},
                'entity-name': {'value': basic_info_data.entity_name},
                'entity-long-name': {'value': basic_info_data.entity_long_name},
                'name-eff-date': {'value': format_date(basic_info_data.name_eff_date)},
                'issuance-agency': {'code': basic_info_data.issuance_agency_code,
                                    'desc': basic_info_data.issuance_agency_desc},
                'entity-status': {'code': basic_info_data.entity_status_code,
                                  'desc': basic_info_data.entity_status_desc,
                                  'value': basic_info_data.entity_status_value},
                'entity-status-eff-date': {'value': format_date(basic_info_data.entity_status_eff_date)},
                'uen-status': {'code': basic_info_data.uen_status, 'desc': basic_info_data.uen_status_desc},
                'entity-type': {'code': basic_info_data.entity_code, 'desc': basic_info_data.entity_desc},
                'registration-date': {'value': format_date(basic_info_data.registration_date)},
                **({'company-type': {'code': basic_info_data.company_type_code,
                                     'desc': basic_info_data.company_type_desc},
                    'country-of-incorporation': {'code': basic_info_data.country_of_incorporation_code,
                                                 'desc': basic_info_data.country_of_incorporation_desc},
                    'allp-indicator': {'value': basic_info_data.allp_indicator},
                    'company-amalgamation': {
                        'amalgamation-date': {'value': format_date(basic_info_data.ca_amalgamation_date)},
                        'amalgamated-company-name': {'value': basic_info_data.ca_company_name},
                        'amalgamated-company-uen': {'value': basic_info_data.ca_company_uen},
                        'transaction-number': {'value': basic_info_data.ca_transaction_number},
                    },
                    'company-conversion-indicator': {'value': basic_info_data.company_conversation_indicator},
                    'company-number-of-members': {'value': basic_info_data.company_number_of_members},
                    'company-allottee-indicator': {'value': basic_info_data.company_allottee_indicator},
                    'company-authorized-capital-number': {'value': basic_info_data.company_authorized_capital_number},
                    } if basic_info_data.entity_code == 'LC' else {}),
                'primary-activity': {'code': basic_info_data.pri_activity_code,
                                     'desc': basic_info_data.pri_activity_desc},
                'primary-activity-add-desc': {'value': basic_info_data.pri_activity_add_desc},
                'secondary-activity': {'code': basic_info_data.sec_activity_code,
                                       'desc': basic_info_data.sec_activity_desc},
                'activity-eff-date': {'value': format_date(basic_info_data.activity_eff_date)},
                'filing-agent': {
                    'fa-id-number': {'value': basic_info_data.fa_id_number},
                    'deregistration-date': {'value': format_date(basic_info_data.fa_deregistration_date)},
                    'status-effective-date': {'value': format_date(basic_info_data.fa_status_effective_date)},
                    'registration-date': {'value': format_date(basic_info_data.fa_registration_date)},
                    'expiry-date': {'value': format_date(basic_info_data.fa_expiry_date)},
                    'status': {'code': basic_info_data.fa_status_code, 'desc': basic_info_data.fa_status_desc},
                },

                **({'constitution': {'value': basic_info_data.constitution_value,
                                     'code': basic_info_data.constitution_code},
                    'secondary-activity-add-desc': {'value': basic_info_data.secondary_activity_add_desc},
                    'expiry-date': {'value': format_date(basic_info_data.expiry_date)},
                    'constitution-date': {'value': format_date(basic_info_data.constitution_date)},
                    'person-particulars-change-date': {
                        'value': format_date(basic_info_data.person_particulars_change_date)},
                    'renewal': {
                        'number-of-years': {'value': basic_info_data.renewal_years},
                        'renewal-date': {'value': format_date(basic_info_data.renewal_date)},
                        'renewal-mode': {'code': basic_info_data.renewal_mode_code,
                                         'desc': basic_info_data.renewal_mode_desc},
                        'transaction-number': {'value': basic_info_data.transaction_number},
                    },
                    'created-date': {'value': format_date(basic_info_data.created_date)},
                    'commencement-date': {'value': format_date(basic_info_data.commencement_date)},
                    } if basic_info_data.entity_code == 'BN' else {})
            }, 'appointments': []}

            # Fetch related data from other tables if applicable

            appointments = Appointment.query.filter_by(uen_value=uen).all()

            if appointments:
                for appointment in appointments:
                    appointed_entity = AppointedEntity.query.get(appointment.appointed_appointment_entity_id)
                    if appointed_entity:
                        if appointment.appointed_person_id:
                            appointed_person = AppointedPerson.query.get(appointment.appointed_person_id)

                            if appointed_person:
                                address = Address.query.filter_by(appointed_person_id=appointed_person.id).first()

                                appointment_data = {
                                    "appointed-entity": {
                                        'name': {'value': appointed_entity.name},
                                        'type': {'code': appointed_entity.type_code,
                                                 'desc': appointed_entity.type_desc},
                                        'uen': {'value': appointed_entity.uen_value},
                                    },
                                    'withdrawal-date': {'value': format_date(appointment.withdrawal_date)},
                                    'reinstate-indicator': {'value': appointment.reinstate_indicator},
                                    'estate-indicator': {'value': appointment.estate_indicator},
                                    'appointed-date': {'value': format_date(appointment.appointed_date)},
                                    'position': {'code': appointment.position_code, 'desc': appointment.position_desc},
                                    'source': appointment.source,
                                    'category': {'code': appointment.category_code, 'desc': appointment.category_desc},
                                    'disqualification-reason-subsection': {
                                        'code': appointment.disqualification_reason_subsection_code,
                                        'desc': appointment.disqualification_reason_subsection_desc},
                                    'withdrawal-reason': {'code': appointment.withdrawal_reason_code,
                                                          'desc': appointment.withdrawal_reason_desc},
                                    'death-indicator': {'value': appointment.death_indicator_value},
                                    'disqualification-reason': {
                                        'code': appointment.disqualification_reason_code,
                                        'desc': appointment.disqualification_reason_desc},
                                    'appointed-person': {
                                        'name': {'value': appointed_person.name},
                                        'nationality': {'code': appointed_person.nationality_code,
                                                        'desc': appointed_person.nationality_desc},
                                        'id-no': {'value': appointed_person.id},
                                        'id-type': {'code': appointed_person.id_type_code,
                                                    'desc': appointed_person.id_type_desc},
                                        'address': {
                                            'country': {'code': address.country_code, 'desc': address.country_desc},
                                            'unit': {'value': address.unit_value},
                                            'purpose': {'value': address.purpose_value},
                                            'street': {'value': address.street_value},
                                            'addresstype': address.addresstype,
                                            'block': {'value': address.block_value},
                                            'postal': {'value': address.postal_value},
                                            'source': address.source,
                                            'address-change-date': {
                                                'value': format_date(address.address_change_date_value)},
                                            'floor': {'value': address.floor_value},
                                            'building': {'value': address.building_value},
                                        }
                                    }
                                }
                                data['appointments'].append(appointment_data)
                        else:
                            appointment_data = {
                                "appointed-entity": {
                                    'name': {'value': appointed_entity.name},
                                    'type': {'code': appointed_entity.type_code,
                                             'desc': appointed_entity.type_desc},
                                    'uen': {'value': appointed_entity.uen_value},
                                },
                                'withdrawal-date': {'value': format_date(appointment.withdrawal_date)},
                                'reinstate-indicator': {'value': appointment.reinstate_indicator},
                                'estate-indicator': {'value': appointment.estate_indicator},
                                'appointed-date': {'value': format_date(appointment.appointed_date)},
                                'position': {'code': appointment.position_code, 'desc': appointment.position_desc},
                                'source': appointment.source,
                                'category': {'code': appointment.category_code, 'desc': appointment.category_desc},
                                'disqualification-reason-subsection': {
                                    'code': appointment.disqualification_reason_subsection_code,
                                    'desc': appointment.disqualification_reason_subsection_desc},
                                'withdrawal-reason': {'code': appointment.withdrawal_reason_code,
                                                      'desc': appointment.withdrawal_reason_desc},
                                'death-indicator': {'value': appointment.death_indicator_value},
                                'disqualification-reason': {
                                    'code': appointment.disqualification_reason_code,
                                    'desc': appointment.disqualification_reason_desc},
                            }
                            data['appointments'].append(appointment_data)
                    else:
                        if appointment.appointed_person_id:
                            appointed_person = AppointedPerson.query.get(appointment.appointed_person_id)
                            address = Address.query.filter_by(appointed_person_id=appointed_person.id).first()
                            appointment_data = {
                                'withdrawal-date': {'value': format_date(appointment.withdrawal_date)},
                                'reinstate-indicator': {'value': appointment.reinstate_indicator},
                                'estate-indicator': {'value': appointment.estate_indicator},
                                'appointed-date': {'value': format_date(appointment.appointed_date)},
                                'position': {'code': appointment.position_code,
                                             'desc': appointment.position_desc},
                                'source': appointment.source,
                                'category': {'code': appointment.category_code,
                                             'desc': appointment.category_desc},
                                'disqualification-reason-subsection': {
                                    'code': appointment.disqualification_reason_subsection_code,
                                    'desc': appointment.disqualification_reason_subsection_desc},
                                'withdrawal-reason': {'code': appointment.withdrawal_reason_code,
                                                      'desc': appointment.withdrawal_reason_desc},
                                'death-indicator': {'value': appointment.death_indicator_value},
                                'disqualification-reason': {
                                    'code': appointment.disqualification_reason_code,
                                    'desc': appointment.disqualification_reason_desc},
                                'appointed-person': {
                                    'name': {'value': appointed_person.name},
                                    'nationality': {'code': appointed_person.nationality_code,
                                                    'desc': appointed_person.nationality_desc},
                                    'id-no': {'value': appointed_person.id},
                                    'id-type': {'code': appointed_person.id_type_code,
                                                'desc': appointed_person.id_type_desc},
                                    'address': {
                                        'country': {'code': address.country_code,
                                                    'desc': address.country_desc},
                                        'unit': {'value': address.unit_value},
                                        'purpose': {'value': address.purpose_value},
                                        'street': {'value': address.street_value},
                                        'addresstype': address.addresstype,
                                        'block': {'value': address.block_value},
                                        'postal': {'value': address.postal_value},
                                        'source': address.source,
                                        'address-change-date': {
                                            'value': format_date(address.address_change_date_value)},
                                        'floor': {'value': address.floor_value},
                                        'building': {'value': address.building_value},
                                    }
                                }
                            }
                            data['appointments'].append(appointment_data)

            company_address = address_function_map[data.get('basic-profile')['entity-type']['code']].query.filter_by(
                **{f"{data.get('basic-profile')['entity-type']['code'].lower()}_basic_profile_uen": uen}).all()
            company_address_list = []
            if company_address:
                for address in company_address:
                    company_address_data = {
                        'country': {'code': address.country_code, 'desc': address.country_desc},
                        'unit': {'value': address.unit_value},
                        'purpose': {'value': address.purpose_value},
                        'street': {'value': address.street_value},
                        'addresstype': address.addresstype,
                        'block': {'value': address.block_value},
                        'postal': {'value': address.postal_value},
                        'source': address.source,
                        'address-change-date': {
                            'value': format_date(address.address_change_date_value)},
                        'floor': {'value': address.floor_value},
                        'building': {'value': address.building_value},
                    }
                    company_address_list.append(company_address_data)
                data['addresses'] = company_address_list

            return data

        else:
            print("No data found for the given UEN.")
            return None

    except Exception as e:
        print("Error while fetching data from the database:", str(e))
        return None


def handle_data(uen, data):
    try:
        # Check if the company exists in the database.
        existing_company = function_map[data.get('basic-profile')['entity-type']['code']].query.filter_by(uen=uen).first()
        print(existing_company)
        if not existing_company:
            # The company does not exist, insert the data into the database.
            if insert_data_into_db(data, uen):
                return jsonify({'message': 'Data insertion successful!'}), 200
            else:
                return jsonify({'message': 'Error while inserting data'}), 500
        else:
            # The company exists, fetch data from the database.
            data = get_data_from_database(uen, data)
            if data:
                return jsonify(data)
            else:
                return jsonify({'message': 'Error fetching data from the database'}), 500

    except Exception as e:
        print("Error while processing the request:", str(e))
        return jsonify({'message': 'Error processing the request'}), 500
