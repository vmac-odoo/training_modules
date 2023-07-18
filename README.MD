# TRAINING MODULES FOR INTERNSHIP

## Solutions T05:
 - Create one record from the Motorcycle Registry Model. This Registry should have more than 1000 miles and no license plate.

    ```console
    >>> env['motorcycle.registry'].create({'registry_number': 'SAMPLE', 'vin': 'SAMPLEVIN', 'first_name': 'John', 'last_name': 'Doe', 'current_mileage': 1200})
    ```

- Search for all Motorcycles Registries with less than 1000 miles.
    ```console
    >>> env['motorcycle.registry'].search_read([('current_mileage', '>', '1000')], [])
    ```

- Search for all Motorcycle Registries with a VIN Number but no License Plate. Only show the fields: registry_number, vin, license_plate, and lastname
    ```console
    >>> env['motorcycle.registry'].search_read([('vin', '!=', None), ('license_plate', '=', None)], ['registry_number', 'vin', 'license_plate', 'last_name'])
    ```
- Search for all Motorcycle Registries with a VIN Number or a License Plate.
    ```console
    >>> env['motorcycle.registry'].search_read(['|', ('vin', '!=', None), ('license_plate','!=', None)], ['registry_number', 'vin', 'license_plate', 'last_name'])
    ```
- Update the Name and Lastname of the record you created to John Wick
    ```console
    >>> moto = env['motorcycle.registry'].browse(6)
    >>> moto
    motorcycle.registry(6,)
    >>> moto.write({'first_name': 'John', 'last_name': 'Wick'})
    True
    >>> env.cr.commit()
    ```
- Delete the Record.
    ```console
    >>> moto.unlink()
    2023-07-18 19:40:14,720 27184 INFO odoo16 odoo.models.unlink: User #1 deleted motorcycle.registry records with IDs: [6] 
    True
    >>> env.cr.commit()
    ```
### TODO: Make all description