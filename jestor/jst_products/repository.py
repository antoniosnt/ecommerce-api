from django.db import connection
from jestor.core.utils.debug import format_query_for_debuging
from jestor.core.utils.querys import dictfetchall


class ProductRepository:
    def __init__(self):
        pass

    def get_products(self, sku=None, na_product=None):
        SQL = """
            SELECT *
            FROM ecm_catalogo ec
        """

        filters = []
        params = {}

        if sku:
            filters.append("ec.sku LIKE %(sku)s")
            params["sku"] = f"%{sku}%"

        if na_product:
            filters.append("ec.na_product LIKE %(na_product)s")
            params["na_product"] = f"{na_product}%"

        if filters:
            SQL += " WHERE " + " AND ".join(filters)

        with connection.cursor() as cursor:
            print(format_query_for_debuging(query=SQL, params=params))
            cursor.execute(sql=SQL, params=params)
            products = dictfetchall(cursor=cursor)

        return products if products else None

    def insert_product(self, data=None):
        SQL = """
        INSERT INTO ecm_catalogo (
            nce, 
            cd_color,
            cd_marca,
            na_product,
            na_description,
            total_vl,
            installments,
            images
        ) VALUES (
            %(nce)s, %(cd_color)s, %(cd_marca)s, %(na_product)s,
            %(na_description)s, %(total_vl)s, %(installments)s,
            %(images)s
        )
        """

        params = {
            "nce": data.get("nce"),
            "cd_color": data.get("cd_color"),
            "cd_marca": data.get("cd_marca"),
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

        return results if results else None
