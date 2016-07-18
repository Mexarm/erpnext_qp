# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Dummy(Document):
	def custom__check_soitem_project(self):
		soitem = frappe.get_doc('Sales Order Item',self.soitem)
		sorder=frappe.get_doc('Sales Order', soitem.parent)
		project = frappe.get_doc('Project',self.project)
		if sorder.project_name != project.name:
			frappe.throw('La pieza: ' + self.soitem +' no corresponde al Proyecto ' + project.name) 
		
	def update():
		custom__check_soitem_project()

	pass
