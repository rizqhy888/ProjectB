# -*- coding: utf-8 -*-
# from odoo import http


# class CapriTraining(http.Controller):
#     @http.route('/capri_training/capri_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capri_training/capri_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('capri_training.listing', {
#             'root': '/capri_training/capri_training',
#             'objects': http.request.env['capri_training.capri_training'].search([]),
#         })

#     @http.route('/capri_training/capri_training/objects/<model("capri_training.capri_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capri_training.object', {
#             'object': obj
#         })

