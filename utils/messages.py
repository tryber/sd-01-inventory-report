def generate_return_message(name, oldest_fabricate, near_validate):
    fabricate_msg = f"Data de fabricação mais antiga: {oldest_fabricate}"
    validate_msg = f"Data de validade mais próxima: {near_validate}"
    new_name = str(name)
    new_name = new_name.split("'")[1]
    name_mg = f"Empresa com maior quantidade de produtos estocados: {new_name}"
    return [fabricate_msg, validate_msg, name_mg]
