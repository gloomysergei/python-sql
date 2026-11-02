def get_order_sum(conn,month):
    sql_str = """
        SELECT c.customer_name, SUM(o.total_amount) AS amount
        FROM orders AS o
        INNER JOIN customers AS c ON c.customer_id = o.customer_id
        WHERE EXTRACT(MONTH FROM o.order_date) = %s
        GROUP BY c.customer_id, c.customer_name
        ORDER BY c.customer_name;
    """
    with conn.cursor() as cur:
        cur.execute(sql_str, (month,))
        result = cur.fetchall()
        lines = [
        f'Покупатель {name} совершил покупок на сумму {int(amount)}'
        for name, amount in result
    ]
    return '\n'.join(lines)