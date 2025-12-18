"""
QUESTION:
Implement a function `extractValues` that takes a `ParsedExpArgs` structure as input and returns a subset of specific values based on the `ty` field. The `ParsedExpArgs` structure contains the following fields: `ty`, `final_t`, `char_t`, `cil_mag`, `coa_mag`, `adh_scale`, `adh_break`, `cal_mag`, `crl_one_at`, `zero_at`, and `too_close_dist`. The function should return the following values based on the `ty` field:
- If `ty` is "temperature", return `final_t` and `char_t`
- If `ty` is "magnitude", return `cil_mag`, `coa_mag`, and `cal_mag`
- If `ty` is "adhesion", return `adh_scale` and `adh_break`
- If `ty` is "distance", return `crl_one_at`, `zero_at`, and `too_close_dist`
- If `ty` does not match any of the above, return an empty array.
"""

def extractValues(parsed_exp_args):
    if parsed_exp_args.ty == "temperature":
        return [parsed_exp_args.final_t, parsed_exp_args.char_t]
    elif parsed_exp_args.ty == "magnitude":
        return [parsed_exp_args.cil_mag, parsed_exp_args.coa_mag, parsed_exp_args.cal_mag]
    elif parsed_exp_args.ty == "adhesion":
        return [parsed_exp_args.adh_scale, parsed_exp_args.adh_break]
    elif parsed_exp_args.ty == "distance":
        return [parsed_exp_args.crl_one_at, parsed_exp_args.zero_at, parsed_exp_args.too_close_dist]
    else:
        return []