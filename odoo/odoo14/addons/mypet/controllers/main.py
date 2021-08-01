import odoo
import logging
import json

_logger = logging.getLogger(__name__)


class MyPetAIPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foo_handler(self):
        return 'Welcom to "foo" API !'

    @odoo.http.route('/bar', auth='public')
    def bar_handler(self):
        return json.dumps({
            'content': 'Welcom to "bar" API !'
        })

    # dbname is name of create database
    @odoo.http.route(['/<dbname>/pet/<id>'], type='http', auth='none', sitemap=False, cors='*', csrf=False)
    def pet_handler(self, dbname, id, **kw):
        model_name = 'my.pet'
        try:
            registry = odoo.modules.registry.Registry(dbname)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([('id', '=', int(id))], limit=1)
                response = {
                    'status': 'ok',
                    'content': {
                        'name': rec.name,
                        'nickname': rec.nickname,
                        'description': rec.description,
                        'age': rec.age,
                        'weight': rec.weight,
                        'dob': rec.dob.strftime('%d%m%Y'),
                        'gender': rec.gender
                    }
                }
        except Exception as ex:
            # print(ex)
            response = {
                'status': 'error',
                'content': 'not found'
            }
        return json.dumps(response)
