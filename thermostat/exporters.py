import pandas as pd

def metrics_to_csv(metrics, filepath):
    """ Writes metrics outputs to the file specified.

    Parameters
    ----------
    metrics : list of dict
        list of outputs from the function
        `thermostat.calculate_epa_draft_rccs_field_savings_metrics()`
    filepath : str
        filepath specification for location of output CSV file.

    Returns
    -------
    df : pd.DataFrame
        DataFrame containing data output to CSV.
    """

    columns = [
        'ct_identifier',
        'equipment_type',
        'heating_or_cooling',
        'station',
        'zipcode',

        'start_date',
        'end_date',
        'n_days_in_inputfile_date_range',
        'n_days_both_heating_and_cooling',
        'n_days_insufficient_data',
        'n_days_core_cooling_days',
        'n_days_core_heating_days',

        'percent_savings_deltaT_cooling',
        'avoided_daily_mean_core_day_runtime_deltaT_cooling',
        'avoided_total_core_day_runtime_deltaT_cooling',
        'baseline_daily_mean_core_day_runtime_deltaT_cooling',
        'baseline_total_core_day_runtime_deltaT_cooling',
        '_daily_mean_core_day_demand_baseline_deltaT_cooling',
        'mean_demand_deltaT_cooling',
        'alpha_deltaT_cooling',
        'tau_deltaT_cooling',
        'mean_sq_err_deltaT_cooling',
        'root_mean_sq_err_deltaT_cooling',
        'cv_root_mean_sq_err_deltaT_cooling',
        'mean_abs_err_deltaT_cooling',
        'mean_abs_pct_err_deltaT_cooling',

        'percent_savings_dailyavgCTD',
        'avoided_daily_mean_core_day_runtime_dailyavgCTD',
        'avoided_total_core_day_runtime_dailyavgCTD',
        'baseline_daily_mean_core_day_runtime_dailyavgCTD',
        'baseline_total_core_day_runtime_dailyavgCTD',
        'mean_demand_dailyavgCTD',
        '_daily_mean_core_day_demand_baseline_dailyavgCTD',
        'alpha_dailyavgCTD',
        'tau_dailyavgCTD',
        'mean_sq_err_dailyavgCTD',
        'root_mean_sq_err_dailyavgCTD',
        'cv_root_mean_sq_err_dailyavgCTD',
        'mean_abs_err_dailyavgCTD',
        'mean_abs_pct_err_dailyavgCTD',

        'percent_savings_hourlyavgCTD',
        'avoided_daily_mean_core_day_runtime_hourlyavgCTD',
        'avoided_total_core_day_runtime_hourlyavgCTD',
        'baseline_daily_mean_core_day_runtime_hourlyavgCTD',
        'baseline_total_core_day_runtime_hourlyavgCTD',
        'mean_demand_hourlyavgCTD',
        '_daily_mean_core_day_demand_baseline_hourlyavgCTD',
        'alpha_hourlyavgCTD',
        'tau_hourlyavgCTD',
        'mean_sq_err_hourlyavgCTD',
        'root_mean_sq_err_hourlyavgCTD',
        'cv_root_mean_sq_err_hourlyavgCTD',
        'mean_abs_err_hourlyavgCTD',
        'mean_abs_pct_err_hourlyavgCTD',

        'percent_savings_deltaT_heating',
        'avoided_daily_mean_core_day_runtime_deltaT_heating',
        'avoided_total_core_day_runtime_deltaT_heating',
        'baseline_daily_mean_core_day_runtime_deltaT_heating',
        'baseline_total_core_day_runtime_deltaT_heating',
        'mean_demand_deltaT_heating',
        '_daily_mean_core_day_demand_baseline_deltaT_heating',
        'alpha_deltaT_heating',
        'tau_deltaT_heating',
        'mean_sq_err_deltaT_heating',
        'root_mean_sq_err_deltaT_heating',
        'cv_root_mean_sq_err_deltaT_heating',
        'mean_abs_err_deltaT_heating',
        'mean_abs_pct_err_deltaT_heating',

        'percent_savings_dailyavgHTD',
        'avoided_daily_mean_core_day_runtime_dailyavgHTD',
        'avoided_total_core_day_runtime_dailyavgHTD',
        'baseline_daily_mean_core_day_runtime_dailyavgHTD',
        'baseline_total_core_day_runtime_dailyavgHTD',
        'mean_demand_dailyavgHTD',
        '_daily_mean_core_day_demand_baseline_dailyavgHTD',
        'alpha_dailyavgHTD',
        'tau_dailyavgHTD',
        'mean_sq_err_dailyavgHTD',
        'root_mean_sq_err_dailyavgHTD',
        'cv_root_mean_sq_err_dailyavgHTD',
        'mean_abs_err_dailyavgHTD',
        'mean_abs_pct_err_dailyavgHTD',

        'percent_savings_hourlyavgHTD',
        'avoided_daily_mean_core_day_runtime_hourlyavgHTD',
        'avoided_total_core_day_runtime_hourlyavgHTD',
        'baseline_daily_mean_core_day_runtime_hourlyavgHTD',
        'baseline_total_core_day_runtime_hourlyavgHTD',
        'mean_demand_hourlyavgHTD',
        '_daily_mean_core_day_demand_baseline_hourlyavgHTD',
        'alpha_hourlyavgHTD',
        'tau_hourlyavgHTD',
        'mean_sq_err_hourlyavgHTD',
        'root_mean_sq_err_hourlyavgHTD',
        'cv_root_mean_sq_err_hourlyavgHTD',
        'mean_abs_err_hourlyavgHTD',
        'mean_abs_pct_err_hourlyavgHTD',

        'total_auxiliary_heating_runtime',
        'total_emergency_heating_runtime',
        'total_core_heating_runtime',
        'total_core_cooling_runtime',

        'daily_mean_core_cooling_runtime',
        'daily_mean_core_heating_runtime',

        'baseline90_core_heating_comfort_temperature',
        'baseline10_core_cooling_comfort_temperature',

        'rhu_00F_to_05F',
        'rhu_05F_to_10F',
        'rhu_10F_to_15F',
        'rhu_15F_to_20F',
        'rhu_20F_to_25F',
        'rhu_25F_to_30F',
        'rhu_30F_to_35F',
        'rhu_35F_to_40F',
        'rhu_40F_to_45F',
        'rhu_45F_to_50F',
        'rhu_50F_to_55F',
        'rhu_55F_to_60F',

        'sw_version',
    ]

    output_dataframe = pd.DataFrame(metrics, columns=columns)
    output_dataframe.to_csv(filepath, index=False, columns=columns)
    return output_dataframe
