def generate_return_message(name, oldest_fabricate, near_validate):
    fabricate_msg = f"Data de fabricação mais antiga: {oldest_fabricate}"
    validate_msg = f"Data de validade mais próxima: {near_validate}"
    name_mg = f"Empresa com maior quantidade de produtos estocados: {name}"
    return (fabricate_msg, '\n', validate_msg, '\n', name_mg)
