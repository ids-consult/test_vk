# -*- coding: utf-8 -*-
#################################################################################

#################################################################################
{
 'name'        : "Partner credit Limit Warning",
 'author'      : "",
 'category'    : 'Inventory',
 'summary'     : """
                Show Warning while confirm sale order if credit limit reached, or overdue invoice
 """,
 'website'     : '',
 'version'     : '16.0.1.0',
 'depends'     : ['sale','account'],
 'data'        : [
                  'views/views.xml',

                 ],
 'installable' : True,
 'application' : True,
 'auto_install': False,
}
