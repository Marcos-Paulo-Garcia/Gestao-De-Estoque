from flask import request, jsonify, make_response
from src.application.service.product_service import ProductService
from config.data_base import db