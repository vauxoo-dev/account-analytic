# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Programmed by: Nhomar Hernandez <nhomar@vauxoo.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Configure account analytic plans",
    "version": "0.1",
    "author": "Vauxoo",
    "website": "www.vauxoo.com",
    "category": "Generic Modules/Projects & Services",
    "license": "AGPL-3",
    "depends": [
        "project",
        "account_accountant",
        "account_analytic_plans",
        "purchase_analytic_plans",
        "sale_analytic_plans",
    ],
    "data": [
    ],
    "demo": [
        "demo/aap_demo.xml",
        #"demo/invoice_demo.xml",
    ],
    "test": [
        #"test/test_purchase_invoice_plan.yml",
    ],
    "active": False,
    "installable": True,
    "description": """
Pre-Config Account Analytic Plans
=================================

This modules is a helper module (only data) to understand how configure
account analytic plans.

This module is and attem to explain throught non-update examples how such
module must be configured.

Other Objective of this module is to be used to make unit testing of this
important module to ensure a secured evolution.

Use Case:
---------

I have a company which need to control all the expenses related with his Human
resources (employees) but some of those expenses needs to be paid by some
specific customer to mantain correctly pointed the revenue of the company, the
it needs to be reported on this way.

The first expense to be controlled is buy two iMac to manage the Marketing in
the company, the "Income" that will pay this Expense, one time
the project finish this iMacs will be owned by the Employee with a 40% of
discount and they will represent part of them payments, meaning that they will
be invoiced to employees with this discount.

To comply with this theretical situation, we will buy the computer and we will
set the analytic accounting to look like this:

- 50% goes to Employee A
- 50% goes to Employee B
- 100% goes to Project X
    """,
}
