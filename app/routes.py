from flask import Blueprint, request, jsonify
from .models import Patient
from . import db

main = Blueprint('main', __name__)

@main.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.order_by(Patient.priority.desc()).all()
    return jsonify([patient.to_dict() for patient in patients])

@main.route('/patients', methods=['POST'])
def add_patient():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Invalid or missing JSON payload'}), 400

        required_fields = ('name', 'age', 'condition', 'priority')
        missing = [f for f in required_fields if f not in data]
        if missing:
            return jsonify({'error': 'Missing fields', 'missing': missing}), 400

        try:
            age = int(data['age'])
            priority = int(data['priority'])
        except ValueError:
            return jsonify({'error': 'Age and priority must be valid numbers'}), 400

        if not (1 <= priority <= 5):
            return jsonify({'error': 'Priority must be between 1 and 5'}), 400

        new_patient = Patient(
            name=data['name'],
            age=age,
            condition=data['condition'],
            priority=priority
        )
        
        db.session.add(new_patient)
        db.session.commit()
        
        return jsonify(new_patient.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error adding patient: {str(e)}")
        return jsonify({'error': 'Failed to add patient'}), 500

@main.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        patient = Patient.query.get_or_404(patient_id)
        db.session.delete(patient)
        db.session.commit()
        return jsonify({'message': f'Patient {patient_id} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting patient: {str(e)}")
        return jsonify({'error': 'Failed to delete patient'}), 500