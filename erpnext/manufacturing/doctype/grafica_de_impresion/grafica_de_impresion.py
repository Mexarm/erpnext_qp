# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class GraficadeImpresion(Document):

        def validate(self):
                total=0
                for spool_entry in self.archivos_spool:
                        total += spool_entry.cantidad_de_registros
                self.total=total
		if (not self.priority) and self.project:
			self.priority=frappe.db.get_value("Project",self.project,"priority")
			

