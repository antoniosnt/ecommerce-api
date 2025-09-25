from django.db import connection
from jestor.core.utils.debug import format_query_for_debuging
from jestor.core.utils.querys import dictfetchall


class CategoryRepository:
    def __init__(self):
        pass

    def get_categories(self, na_category=None, cd_category=None):
        SQL = """
            SELECT * FROM ecm_categorias AS ecc
        """

        filters = []
        params = {}

        if na_category:
            filters.append("ecc.na_category LIKE %(na_category)s")
            params["na_category"] = f"{na_category}%"

        if cd_category:
            filters.append("ecc.cd_category = %(cd_category)s")
            params["cd_category"] = cd_category

        if filters:
            SQL += " WHERE " + " AND ".join(filters)

        with connection.cursor() as cursor:
            print(format_query_for_debuging(query=SQL, params=params))
            cursor.execute(sql=SQL, params=params)
            categories = dictfetchall(cursor)

        return categories or None

    def insert_category(self, data=None):
        SQL = """
        INSERT INTO ecm_categorias (
            cd_category,
            na_category
        ) VALUES (
            %(cd_category)s, %(na_category)s
        )
        """

        params = {
            "cd_category": data.get("cd_category"),
            "na_category": data.get("na_category"),
        }

        with connection.cursor() as cursor:
            print(format_query_for_debuging(query=SQL, params=params))
            cursor.execute(sql=SQL, params=params)
