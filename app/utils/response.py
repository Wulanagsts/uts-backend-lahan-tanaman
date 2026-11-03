from flask import jsonify


def success_response(data=None, message="Berhasil", code=200):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), code


def fail_response(errors, code=400):
    return jsonify({
        "status": "fail",
        "errors": errors
    }), code


def error_response(message="Terjadi kesalahan pada server", code=500):
    return jsonify({
        "status": "error",
        "message": message
    }), code