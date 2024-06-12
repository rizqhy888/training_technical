# -*- coding: utf-8 -*-
{
    "name" : "PT. Sanbe Farma - Training",
    "description" : "Pelatihan Technical Odoo V17 untuk PT. Sanbe Farma",
    "author" : "PT. Sanbe Farma, PT. Arkana Solusi Digital",
    "version" : "17.0.1.0.0",
    "category" : "Others",
    "license" : "OPL-1",
    "depends" : [
        "base", 
        "mail",
    ],
    "data" : [
        "security/ir.model.access.csv",
        "views/views.xml",
    ],
    "auto_install" : False, 
    "installable" : True,
    "application" : True,
    "external_dependencies" : {"python" : []}
}

