using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GetEmbed_Consumer
{
    namespace Project
    {
        public class RootObject
        {
            public string description { get; set; }
            public string properties { get; set; }
            public string organisation { get; set; }
            public string name { get; set; }
            public string programme_id { get; set; }
            public string project_type { get; set; }
            public string updated_at { get; set; }
            public string type_of { get; set; }
            public string project_id { get; set; }
            public string project_code { get; set; }
            public string href { get; set; }
            public string created_at { get; set; }
        }

        namespace Entity
        {
            //public class TechnologyIcons
            //{
            //    public bool small_hydros { get; set; }
            //    public bool wind_turbines { get; set; }
            //    public bool ventilation_systems { get; set; }
            //    public bool cavity_wall_insulation { get; set; }
            //    public bool photovoltaics { get; set; }
            //    public bool chps { get; set; }
            //    public bool solar_thermals { get; set; }
            //    public bool heat_pumps { get; set; }
            //    public bool solid_wall_insulation { get; set; }
            //}

            public class PropertyData
            {
                public string project_summary { get; set; }
                public string built_form { get; set; }
                public string design_strategy { get; set; }
                public string property_type { get; set; }
                public string project_phase { get; set; }
                //public TechnologyIcons technology_icons { get; set; }
                public string project_team { get; set; }
                public string address_country { get; set; }
                public string terrain { get; set; }
                public string monitoring_policy { get; set; }
                public string monitoring_hierarchy { get; set; }
            }

            public class CalculatedFieldsLastCalc
            {
            }

            public class CalculatedFieldsLabels
            {
            }

            public class CalculatedFieldsValues
            {
            }

            public class UserMetadata
            {
            }

            public class Reading
            {
                public object min { get; set; }
                public string unit { get; set; }
                public UserMetadata user_metadata { get; set; }
                public object accuracy { get; set; }
                public string sensor_id { get; set; }
                public object frequency { get; set; }
                public object corrected_unit { get; set; }
                public string type { get; set; }
                public object correction_factor { get; set; }
                public string upper_ts { get; set; }
                public object correction { get; set; }
                public object resolution { get; set; }
                public string alias { get; set; }
                public double median { get; set; }
                public object status { get; set; }
                public object max { get; set; }
                public string lower_ts { get; set; }
                public object correction_factor_breakdown { get; set; }
                public string period { get; set; }
                public bool synthetic { get; set; }
                public string device_id { get; set; }
                public bool actual_annual { get; set; }
            }

            public class Device
            {
                public string description { get; set; }
                public List<Reading> readings { get; set; }
                public string name { get; set; }
                public string privacy { get; set; }
                public object metering_point_id { get; set; }
                public object parent_id { get; set; }
                public string entity_id { get; set; }
                public bool synthetic { get; set; }
                public string device_id { get; set; }
                public object location { get; set; }
                public object metadata { get; set; }
            }

            public class ProfileData
            {
                public string number_of_storeys { get; set; }
                public string gross_internal_area { get; set; }
                public string used_passivehaus_principles { get; set; }
                public string air_tightness_rate { get; set; }
                public string total_volume { get; set; }
                public string space_heating_requirement { get; set; }
                public string flat_heat_loss_corridor { get; set; }
                public string primary_energy_requirement { get; set; }
                public string profile_comfort { get; set; }
                public string renewable_contribution_elec { get; set; }
                public string profile_needs { get; set; }
                public string controls_strategy { get; set; }
                public string heat_storage_present { get; set; }
                public string modelling_software_methods_used { get; set; }
                public string profile_air_in_summer { get; set; }
                public string co_heating_loss { get; set; }
                public string intention_ofpassvhaus { get; set; }
                public string profile_bus_report_url { get; set; }
                public string orientation { get; set; }
                public string footprint { get; set; }
                public string sap_version_year { get; set; }
                public string annual_heating_load { get; set; }
                public string profile_temperature_in_summer { get; set; }
                public string renewable_contribution_heat { get; set; }
                public string profile_design { get; set; }
                public string ter { get; set; }
                public string roof_rooms_present { get; set; }
                public string flat_floors_in_block { get; set; }
                public string sap_rating { get; set; }
                public string ber { get; set; }
                public string profile_temperature_in_winter { get; set; }
                public string bedroom_count { get; set; }
                public string occupancy_total { get; set; }
                public string fabric_energy_efficiency { get; set; }
                public string profile_air_in_winter { get; set; }
                public string external_perimeter { get; set; }
                public string heat_loss_parameter_hlp { get; set; }
                public string event_type { get; set; }
                public string profile_bus_summary_index { get; set; }
                public string electricity_storage_present { get; set; }
                public string water_saving_strategy { get; set; }
                public string habitable_rooms { get; set; }
                public string profile_lightning { get; set; }
                public string total_rooms { get; set; }
                public string flat_floor_position { get; set; }
                public string profile_health { get; set; }
                public string profile_noise { get; set; }
            }

            public class VentilationSystem
            {
                public string controls { get; set; }
                public string ventilation_type { get; set; }
                public string ductwork_type { get; set; }
                public string operational_settings { get; set; }
                public string approach { get; set; }
            }

            public class Wall
            {
                public string construction { get; set; }
            }

            public class Roof
            {
                public string construction { get; set; }
            }

            public class LowEnergyLight
            {
                public string light_type_other { get; set; }
                public string light_type { get; set; }
            }

            public class HeatingSystem
            {
                public string controls_make_and_model { get; set; }
                public string boiler_type_other { get; set; }
                public string fuel { get; set; }
                public string boiler_type { get; set; }
                public string heating_type { get; set; }
            }

            public class Floor
            {
                public string construction { get; set; }
            }

            public class DoorSet
            {
                public string door_type { get; set; }
            }

            public class Biomass
            {
                public string model { get; set; }
                public string capacity { get; set; }
                public string biomass_type { get; set; }
            }

            public class HotWaterSystem
            {
                public string dhw_type { get; set; }
                public string fuel { get; set; }
                public string cylinder_capacity { get; set; }
                public string immersion { get; set; }
                public string fuel_other { get; set; }
            }

            public class WindowSet
            {
                public string frame_type { get; set; }
                public string window_type { get; set; }
                public string area { get; set; }
                public string percentage_glazing { get; set; }
            }

            public class Profile
            {
                public List<object> thermal_images { get; set; }
                public ProfileData profile_data { get; set; }
                public List<object> small_hydros { get; set; }
                public List<object> wind_turbines { get; set; }
                public List<VentilationSystem> ventilation_systems { get; set; }
                public List<Wall> walls { get; set; }
                public List<object> photovoltaics { get; set; }
                public List<Roof> roofs { get; set; }
                public List<object> conservatories { get; set; }
                public List<object> chps { get; set; }
                public List<object> solar_thermals { get; set; }
                public List<object> storeys { get; set; }
                public List<object> heat_pumps { get; set; }
                public List<object> airflow_measurements { get; set; }
                public List<object> extensions { get; set; }
                public List<LowEnergyLight> low_energy_lights { get; set; }
                public List<HeatingSystem> heating_systems { get; set; }
                public object user_id { get; set; }
                public string profile_id { get; set; }
                public List<Floor> floors { get; set; }
                public string entity_id { get; set; }
                public List<object> roof_rooms { get; set; }
                public List<DoorSet> door_sets { get; set; }
                public string timestamp { get; set; }
                public List<Biomass> biomasses { get; set; }
                public List<HotWaterSystem> hot_water_systems { get; set; }
                public List<WindowSet> window_sets { get; set; }
            }

            public class Entity
            {
                public object address_county { get; set; }
                public object public_access { get; set; }
                public object address_street_two { get; set; }
                public bool editable { get; set; }
                public PropertyData property_data { get; set; }
                public object retrofit_completion_date { get; set; }
                public object name { get; set; }
                public string programme_name { get; set; }
                public string property_code { get; set; }
                public string programme_id { get; set; }
                public List<object> csv_uploads { get; set; }
                public CalculatedFieldsLastCalc calculated_fields_last_calc { get; set; }
                public CalculatedFieldsLabels calculated_fields_labels { get; set; }
                public CalculatedFieldsValues calculated_fields_values { get; set; }
                public object address_country { get; set; }
                public List<object> documents { get; set; }
                public List<object> photos { get; set; }
                public string profile_data_event_type { get; set; }
                public object address_region { get; set; }
                public List<Device> devices { get; set; }
                public List<Profile> profiles { get; set; }
                public string entity_id { get; set; }
                public string project_id { get; set; }
                public object metering_point_ids { get; set; }
                public string project_name { get; set; }
            }

            public class RootObject
            {
                public int total_hits { get; set; }
                public int page { get; set; }
                public List<Entity> entities { get; set; }
            }
        }
    }
}
