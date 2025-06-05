"""
Solar Industry Utility Functions
Contains standard calculations and constants used in solar analysis
"""

# Solar Industry Constants
STANDARD_PANEL_WATTAGE = 300  # Watts per panel
STANDARD_PANEL_AREA = 17.5    # Square feet per panel
INSTALLATION_COST_PER_WATT = 3.0  # $/W installed
SYSTEM_EFFICIENCY = 0.85      # Overall system efficiency
PEAK_SUN_HOURS_DEFAULT = 5.0  # Average peak sun hours
ELECTRICITY_RATE_DEFAULT = 0.12  # $/kWh

class SolarCalculator:
    """Solar industry calculation utilities"""
    
    @staticmethod
    def calculate_panel_count(usable_area_sqft):
        """Calculate number of panels that can fit on roof"""
        return int(usable_area_sqft // STANDARD_PANEL_AREA)
    
    @staticmethod
    def calculate_system_size(panel_count):
        """Calculate system size in kW"""
        return (panel_count * STANDARD_PANEL_WATTAGE) / 1000
    
    @staticmethod
    def calculate_annual_production(system_size_kw, peak_sun_hours=PEAK_SUN_HOURS_DEFAULT):
        """Calculate annual energy production in kWh"""
        daily_production = system_size_kw * peak_sun_hours * SYSTEM_EFFICIENCY
        return daily_production * 365
    
    @staticmethod
    def calculate_installation_cost(system_size_kw):
        """Calculate total installation cost"""
        return system_size_kw * 1000 * INSTALLATION_COST_PER_WATT
    
    @staticmethod
    def calculate_annual_savings(annual_production_kwh, electricity_rate=ELECTRICITY_RATE_DEFAULT):
        """Calculate annual electricity bill savings"""
        return annual_production_kwh * electricity_rate
    
    @staticmethod
    def calculate_payback_period(installation_cost, annual_savings):
        """Calculate simple payback period in years"""
        if annual_savings <= 0:
            return float('inf')
        return installation_cost / annual_savings
    
    @staticmethod
    def calculate_roi(annual_savings, installation_cost):
        """Calculate return on investment percentage"""
        if installation_cost <= 0:
            return 0
        return (annual_savings / installation_cost) * 100
    
    @staticmethod
    def assess_roof_suitability(roof_data):
        """
        Assess roof suitability based on various factors
        Returns score from 1-10
        """
        score = 5  # Base score
        
        # Adjust based on orientation (south-facing is best)
        if roof_data.get('south_facing', False):
            score += 2
        elif roof_data.get('east_west_facing', False):
            score += 1
        
        # Adjust for shading
        shade_level = roof_data.get('shading', 'medium')  # low, medium, high
        if shade_level == 'low':
            score += 2
        elif shade_level == 'high':
            score -= 2
        
        # Adjust for roof condition
        roof_condition = roof_data.get('condition', 'good')  # poor, fair, good, excellent
        if roof_condition == 'excellent':
            score += 1
        elif roof_condition == 'poor':
            score -= 2
        elif roof_condition == 'fair':
            score -= 1
        
        # Adjust for tilt angle (30-45 degrees is optimal)
        tilt = roof_data.get('tilt_angle', 30)
        if 25 <= tilt <= 45:
            score += 1
        elif tilt < 15 or tilt > 60:
            score -= 1
        
        # Ensure score is within 1-10 range
        return max(1, min(10, score))

def get_maintenance_schedule():
    """Return standard solar maintenance requirements"""
    return [
        "Annual system inspection",
        "Panel cleaning (2-4 times per year)",
        "Inverter monitoring and maintenance",
        "Electrical connection checks",
        "Performance monitoring",
        "Warranty compliance checks"
    ]

def get_installation_requirements():
    """Return typical installation requirements"""
    return [
        "Structural engineering assessment",
        "Electrical permit and inspection",
        "Utility interconnection agreement",
        "Local building permits",
        "HOA approval (if applicable)",
        "Professional installation by certified technicians"
    ]

def estimate_carbon_offset(annual_production_kwh):
    """Calculate estimated CO2 offset in pounds per year"""
    # Average CO2 emissions: 0.85 lbs per kWh from grid electricity
    co2_offset_lbs = annual_production_kwh * 0.85
    return co2_offset_lbs

def get_federal_tax_credit():
    """Return current federal solar tax credit information"""
    return {
        "percentage": 30,
        "description": "Federal Solar Investment Tax Credit (ITC)",
        "valid_through": "2032 (then steps down)",
        "note": "Consult tax professional for eligibility"
    }