from odoo import http
from werkzeug.exceptions import NotFound

class MotorcycleControllers(http.Controller):

    @http.route(['/motorcycles', '/motorcycles/page/<int:page>'], auth='public', website=True)
    def index(self, page=1, **kw):
        motorcycles_ids = http.request.env['product.template'].search(
            [('detailed_type', '=', 'motorcycle')],
            offset=(page - 1) * 2,
            limit=3
        )

        total = motorcycles_ids.search_count([('detailed_type', '=', 'motorcycle')])

        pager = http.request.website.pager(
            url='/motorcycles',
            total=total,
            page=page,
            step=3,
        )

        return http.request.render('motorcycle_registry.motorcycles_view', {
            'motorcycles': motorcycles_ids,
            'pager': pager,
        })

    @http.route('/motorcycle/<model("product.template"):product>/', auth='public', website = True)
    def motorcycle_info(self, product):
        return http.request.render('motorcycle_registry.motorcycle_view', {
            'motorcycle': product
        })