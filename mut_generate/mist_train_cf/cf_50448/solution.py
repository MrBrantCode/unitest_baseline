"""
QUESTION:
Transform the given Vega sensitivities of FX options into PnL adjustments using market data quotes. The function should take the following inputs: 
- Vega sensitivities of FX options per tenor and delta
- Changes in the implied volatility surface (∆IV) of the foreign exchange market, obtained from market quotes or option pricing models
- Risk reversals and other exotic quotes, if applicable

The function should return the PnL adjustments calculated by multiplying Vega exposures with the changes in implied volatilities (∆IV) and aggregating these values, while considering the complexities of market dynamics.
"""

def calculate_pnl_adjustments(vega_sensitivities, delta_iv):
    """
    Calculate PnL adjustments by multiplying Vega exposures with the changes in implied volatilities (∆IV) and aggregating these values.

    Args:
        vega_sensitivities (dict): Vega sensitivities of FX options per tenor and delta
        delta_iv (dict): Changes in the implied volatility surface (∆IV) of the foreign exchange market

    Returns:
        float: PnL adjustments
    """
    pnl_adjustments = 0
    for tenor, vega in vega_sensitivities.items():
        for delta, sensitivity in vega.items():
            if tenor in delta_iv and delta in delta_iv[tenor]:
                pnl_adjustments += sensitivity * delta_iv[tenor][delta]
    return pnl_adjustments