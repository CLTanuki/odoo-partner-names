# -*- coding: utf-8 -*-
from odoo import http

# class PartnerNames(http.Controller):
#     @http.route('/partner_additional_names/partner_additional_names/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_additional_names/partner_additional_names/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_additional_names.listing', {
#             'root': '/partner_additional_names/partner_additional_names',
#             'objects': http.request.env['partner_additional_names.partner_additional_names'].search([]),
#         })

#     @http.route('/partner_additional_names/partner_additional_names/objects/<model("partner_additional_names.partner_additional_names"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_additional_names.object', {
#             'object': obj
#         })