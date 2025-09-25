from django.db import connection
from jestor.core.utils.debug import format_query_for_debuging
from jestor.core.utils.querys import dictfetchall


class CategoryRepository:
    def __init__(self):
        pass

    def get_categories(self):
        SQL = """
        SELECT * FROM ecm_categorias;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql=SQL)
            categories = dictfetchall(cursor=cursor)

        return categories if categories else None

    def insert_category(self, data=None):
        pass

    def get_category_by_cd_category(self, cd_category=None):
        pass
