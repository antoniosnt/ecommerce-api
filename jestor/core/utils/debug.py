import traceback

def format_query_for_debuging(query=None, params=None):
    try:

        formatted_query = query[:]
    
        for key, value in params.items():
            if isinstance(value, str):
                val_str = f"'{value}'"
            elif value is None:
                val_str = "NULL"
            else:
                val_str = str(value)
            formatted_query = formatted_query.replace(f"%({key})s", val_str)
    
        return formatted_query
    except Exception as e:
        print("⚠️ Ocorreu um erro ao formatar query")
        print(traceback.print_exc())