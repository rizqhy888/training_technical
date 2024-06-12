# -*- coding: utf-8 -*-
# from odoo import http


# class SanbeTraining(http.Controller):
#     @http.route('/sanbe_training/sanbe_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sanbe_training/sanbe_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sanbe_training.listing', {
#             'root': '/sanbe_training/sanbe_training',
#             'objects': http.request.env['sanbe_training.sanbe_training'].search([]),
#         })

#     @http.route('/sanbe_training/sanbe_training/objects/<model("sanbe_training.sanbe_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sanbe_training.object', {
#             'object': obj
#         })

