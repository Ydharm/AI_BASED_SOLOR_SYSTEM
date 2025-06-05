### 📁 File: analysis.py

def estimate_roi(area_m2, panel_efficiency=0.18, price_per_watt=45):
    kw_possible = area_m2 * panel_efficiency * 0.85
    cost = kw_possible * 1000 * price_per_watt
    savings = kw_possible * 1200 * 25
    roi = savings - cost
    return round(cost, 2), round(savings, 2), round(roi, 2)