from django.db import connection
from ecommerce.core.utils.debug import format_query_for_debuging, dictfetchall


class ProductRepository:
    def __init__(self):
        pass

    def get_products(self):
        SQL = """
        SELECT * FROM ecm_catalogo;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql=SQL)
            products = dictfetchall(cursor=cursor)

        return products if products else None

    def insert_product(self, data=None):
        SQL = """
        INSERT INTO ecm_catalogo (
            nce, 
            fk_color,
            na_product,
            na_description,
            total_vl,
            installments,
            images
        ) VALUES (
            %(nce)s, %(fk_color)s, %(na_product)s,
            %(na_description)s, %(total_vl)s, %(installments)s,
            %(images)s
        )
        """

        params = {
            "nce": data.get("nce"),
            "fk_color": data.get("fk_color"),
            "na_product": data.get("na_product"),
            "na_description": data.get("na_description"),
            "total_vl": data.get("total_vl"),
            "installments": data.get("installments"),
            "images": data.get("images"),
        }

        with connection.cursor() as cursor:
            print(format_query_for_debuging(query=SQL, params=params))
            cursor.execute(sql=SQL, params=params)

    def get_product_by_sku(self, sku=None):
        SQL = """
        SELECT * FROM ecm_catalogo ec WHERE ec.sku LIKE '%(sku)s'
        """

        params = {"sku": "%" + sku + "%"}

        with connection.cursor() as cursor:
            print(format_query_for_debuging(query=SQL, params=params))
            cursor.execute(sql=SQL, params=params)
            results = dictfetchall(cursor=cursor)

        return results[0] if results else None
