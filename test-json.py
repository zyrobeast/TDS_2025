import ijson

def calculate_avg_temp(filepath: str = 'q-json-sensor-rollup.jsonl') -> list:
    t_sum, t_count = 0, 0

    with open(filepath, 'rb') as file:
        for item in ijson.items(file, '', multiple_values=True):
            if item.get('site') == "Plant-01" and item.get('device').startswith("boiler") and "2024-08-17 21:06:37.313Z" <= item.get('captured_at') <= "2024-08-30 21:06:37.313Z" and item.get("status") not in ("maintenance", "offline"):
                temp_metrics = item.get("metrics").get("temperature")
                t_sum += (float(temp_metrics.get("value")) - 32) * 5 / 9 if temp_metrics.get("unit") == "F" else float(temp_metrics.get("value"))
                t_count += 1

    print(f"Avergage Temperature = {t_sum / t_count if t_count > 0 else 0}")

def calculate_total_quantity(filepath: str = 'q-json-customer-flatten.jsonl') -> list:
    count = 0
    with open(filepath, 'rb') as file:
        for item in ijson.items(file, '', multiple_values=True):
            if item.get("region") == "Europe":
                for order in item.get("orders", []):
                    if "2024-01-03" <= order.get("order_date") <= "2024-02-22" and order.get("channel") == "Direct":
                        for item in order.get("items"):
                            if item.get("category") == "Security":
                                count += item.get("quantity", 0)
    
    print(f"Total Quantity = {count}")


if __name__ == "__main__":
    calculate_avg_temp()
    calculate_total_quantity()