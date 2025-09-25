def dictfetchall(cursor=None):
    result = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    results = [dict(zip(columns, row)) for row in result]

    return results if results else None