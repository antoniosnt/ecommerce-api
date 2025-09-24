from django.db import connection
from core.utils.debug import format_query_for_debuging

class ProductRepository():
    def __init__(self):
        pass

    def get_products(self):
        SQL = """
        SELECT * FROM ecm_catalogo;
        """

        with connection.cursor() as cursor:
            result = cursor.execute(sql=SQL)
        
        result if result else None
    
