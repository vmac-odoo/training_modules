from odoo import http

class MotorcycleControllers(http.Controller):
    
    @http.route('/motorcycles/', auth='public', website = True)
    def index(self):
        motorcycles = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
        return http.request.render('motorcycle_registry.motorcycles_view', {
            'motorcycles': motorcycles
        })
        
    @http.route('/motorcycle/<model("product.template"):product>/', auth='public', website = True)
    def motorcycle_info(self, product):
        return http.request.render('motorcycle_registry.motorcycle_view', {
            'motorcycle': product
        })