from flask import jsonify

def exception_handler(exception):
    return jsonify({'message': str(exception)}), 500

def unknown_exception():
    return jsonify({'message': 'An unknown error occurred'}), 500

def server_error():
    return jsonify({'message': 'Server error'}), 500

def bad_request():
    return jsonify({'message': 'Bad request'}), 400

def not_found():
    return jsonify({'message': 'Not found'}), 404

def method_not_allowed():
    return jsonify({'message': 'Method not allowed'}), 405
